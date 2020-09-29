#!/usr/bin/env python
"""
Written by Chris Hupman
Github: https://github.com/chupman/
Example: Get guest info with folder and host placement

"""
from __future__ import print_function

import time

import logging
from pyVmomi import vim

from pyVim.connect import SmartConnectNoSSL, Disconnect

import argparse
import atexit
import getpass
import json

from LearningPy.pyvmomi_projects.ref_git.vmware_pyvmomi_community_samples.my_code import global_config

data = {}

pylogger = global_config.pylogger


def GetArgs():
    """
    Supports the command-line arguments listed below.
    """
    parser = argparse.ArgumentParser(description="get all hosts and their respective VMs")
    parser.add_argument('--host', default='10.79.65.101')
    parser.add_argument('--user', default='userchi@vsphere.local')
    parser.add_argument('--password', default='Admin!23Admin!23')
    parser.add_argument('--port', default='443')
    parser.add_argument('--disable_ssl_verification', default=True)
    parser.add_argument('--host_ip_to_restart', default="10.79.65.109")
    args = parser.parse_args()
    return args


def getNICs(summary, guest):
    nics = {}
    for nic in guest.net:
        if nic.network:  # Only return adapter backed interfaces
            if nic.ipConfig is not None and nic.ipConfig.ipAddress is not None:
                nics[nic.macAddress] = {}  # Use mac as uniq ID for nic
                nics[nic.macAddress]['netlabel'] = nic.network
                ipconf = nic.ipConfig.ipAddress
                i = 0
                nics[nic.macAddress]['ipv4'] = {}
                for ip in ipconf:
                    if ":" not in ip.ipAddress:  # Only grab ipv4 addresses
                        nics[nic.macAddress]['ipv4'][i] = ip.ipAddress
                        nics[nic.macAddress]['prefix'] = ip.prefixLength
                        nics[nic.macAddress]['connected'] = nic.connected
                i = i + 1
    return nics


def vmsummary(summary, guest):
    vmsum = {}
    config = summary.config
    net = getNICs(summary, guest)
    vmsum['mem'] = str(config.memorySizeMB / 1024)
    vmsum['diskGB'] = str("%.2f" % (summary.storage.committed / 1024 ** 3))
    vmsum['cpu'] = str(config.numCpu)
    vmsum['path'] = config.vmPathName
    vmsum['ostype'] = config.guestFullName
    vmsum['state'] = summary.runtime.powerState
    vmsum['annotation'] = config.annotation if config.annotation else ''
    vmsum['net'] = net

    return vmsum


def vm2dict(dc, cluster, host, vm, summary):
    # If nested folder path is required, split into a separate function
    vmname = vm.summary.config.name
    data[dc][cluster][host][vmname]['folder'] = vm.parent.name
    data[dc][cluster][host][vmname]['mem'] = summary['mem']
    data[dc][cluster][host][vmname]['diskGB'] = summary['diskGB']
    data[dc][cluster][host][vmname]['cpu'] = summary['cpu']
    data[dc][cluster][host][vmname]['path'] = summary['path']
    data[dc][cluster][host][vmname]['net'] = summary['net']
    data[dc][cluster][host][vmname]['ostype'] = summary['ostype']
    data[dc][cluster][host][vmname]['state'] = summary['state']
    data[dc][cluster][host][vmname]['annotation'] = summary['annotation']
    print(data[dc][cluster][host][vmname])


def data2json(data, args):
    with open("json_data.json.json", 'w') as f:
        json.dump(data, f)


def main():
    """
    Iterate through all datacenters and list VM info.
    """
    args = GetArgs()
    outputjson = True
    logging.info("Connecting VC..")
    if args.password:
        password = args.password
    else:
        password = getpass.getpass(prompt='Enter password for host %s and '
                                          'user %s: ' % (args.host, args.user))

    si = SmartConnectNoSSL(host=args.host,
                           user=args.user,
                           pwd=password,
                           port=int(args.port))
    if not si:
        print("Could not connect to the specified host using specified "
              "username and password")
        return -1

    # atexit.register(Disconnect, si) # throws exception not sure why
    logging.info("Retrieving Content..")
    content = si.RetrieveContent()
    children = content.rootFolder.childEntity
    for child in children:  # Iterate though DataCenters
        dc = child
        data[dc.name] = {}  # Add data Centers to data dict
        clusters = dc.hostFolder.childEntity
        for cluster in clusters:  # Iterate through the clusters in the DC
            # Add Clusters to data dict
            data[dc.name][cluster.name] = {}
            hosts = cluster.host  # Variable to make pep8 compliance
            for host in hosts:  # Iterate through Hosts in the Cluster
                hostname = host.summary.config.name
                if hostname != args.host_ip_to_restart:
                    continue
                # Add VMs to data dict by config name
                data[dc.name][cluster.name][hostname] = {}
                all_vms = host.vm

                vms = [m for m in all_vms if m.runtime.powerState == "poweredOn"]

                if len(vms) == 0:
                    break

                # for vm in vms:  # Iterate through each VM on the host
                #     vmname = vm.summary.config.name
                #     data[dc.name][cluster.name][hostname][vmname] = {}
                #     summary = vmsummary(vm.summary, vm.guest)
                #     vm2dict(dc.name, cluster.name, hostname, vm, summary)

                logging.info("Powering Off all VMs on host {}".format(host.name))
                for vm in vms:  # Iterate through each VM on the host
                    power_down(vm)

                host_enter_maintenance_mode(host)
                host_reboot(host)
                host_exit_maintenance_mode(host)

                logging.info("Powering ON all VMs on host {}".format(host.name))
                for vm in vms:  # Iterate through each VM on the host
                    power_up(vm)

    # print(json.dumps(data, sort_keys=True, indent=4))
    #
    # data2json(data, args)


def host_reboot(host):
    if host.runtime.inMaintenanceMode:
        logging.info("Rebooting host %s" % (host.name))
        task = host.RebootHost_Task(False)

        while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
            time.sleep(10)
            logging.info("Reboot task state is %s " % task.info.state)

        logging.info("Wait for sometime before checking connection status...")
        time.sleep(60)

        while host.runtime.connectionState != "connected":
            logging.info("Waiting for host to come up. Current Host state is [%s] " % host.runtime.connectionState)
            time.sleep(10)

        if task.info.state is vim.TaskInfo.State.error:
            raise Exception("Could not perform Reboot task on host  %s " % (host.name))
    else:
        logging.error("Host %s is NOT in Maintenance Mode state, Cannot Do Restart!" % host.name)


def host_exit_maintenance_mode(host):
    if host.runtime.inMaintenanceMode:
        logging.info("Switching to Exit Maintenance Mode for host %s" % (host.name))
        task = host.ExitMaintenanceMode_Task(0)
        while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
            time.sleep(10)
            logging.info("Exit Maintenance task state is %s " % task.info.state)
        if task.info.state is vim.TaskInfo.State.error:
            raise Exception("Could not perform Exit maintenance mode task on host  %s " % (host.name))
    else:
        logging.error("Host %s is already NOT in Maintenance Mode state!" % host.name)


def host_enter_maintenance_mode(host):
    if not host.runtime.inMaintenanceMode:
        logging.info("Enter Maintenance Mode for host %s" % host.name)
        task = host.EnterMaintenanceMode_Task(0)
        while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
            time.sleep(10)
            logging.info("Maintenance task state is %s " % task.info.state)
        if task.info.state is vim.TaskInfo.State.error:
            raise Exception("Could not perform Enter maintenance mode task on host {}".format(host.name))
    else:
        logging.error("Host %s is already in Maintenance Mode state!" % host.name)


def power_up(vm):
    if vm.runtime.powerState != vim.VirtualMachinePowerState.poweredOn:
        logging.info("Powering on VM %s" % (vm.name))
        task = vm.PowerOn()
        while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
            time.sleep(10)
            logging.info("PowerOn task state is %s " % task.info.state)
        if task.info.state is vim.TaskInfo.State.error:
            raise Exception("Could not power on vm  %s " % (vm.name))
    else:
        logging.error("VM %s is already in PowerOn state!" % vm.name)


def power_down(vm):
    if vm.runtime.powerState == vim.VirtualMachinePowerState.poweredOn:
        logging.info("Powering Off VM %s" % (vm.name))
        task = vm.PowerOff()
        while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
            time.sleep(10)
            logging.info("PowerOff VM task state is %s " % task.info.state)
        if task.info.state is vim.TaskInfo.State.error:
            raise Exception("Could not powerOff vm  %s " % (vm.name))
    else:
        logging.error("VM %s is already in PowerOff state!" % vm.name)
    return vm


# Start program
if __name__ == "__main__":
    main()
