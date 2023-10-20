#!/usr/bin/env python
from __future__ import print_function

import time

import logging
from pyVmomi import vim

from pyVim.connect import SmartConnectNoSSL

import argparse
import getpass

from misc.LearningPy.pyvmomi_projects.ref_git.vmware_pyvmomi_community_samples.my_code import global_config
from misc.LearningPy.pyvmomi_projects.ref_git.vmware_pyvmomi_community_samples.my_code.retry import retry

data = {}

pylogger = global_config.pylogger


def GetArgs():
    """
    Supports the command-line arguments listed below.
    """
    parser = argparse.ArgumentParser(description="get all hosts and their respective VMs")
    parser.add_argument('--vcip', default='10.79.65.101')
    parser.add_argument('--user', default='userchi@vsphere.local')
    parser.add_argument('--password', default='Admin!23Admin!23')
    parser.add_argument('--port', default='443')
    parser.add_argument('--disable_ssl_verification', default=True)
    parser.add_argument('--host_ip_to_restart', default="10.79.65.108")
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


def main():
    """
    Iterate through all datacenters and list VM info.
    """
    args = GetArgs()
    logging.info("Connecting VC..")
    if args.password:
        password = args.password
    else:
        password = getpass.getpass(prompt='Enter password for host %s and '
                                          'user %s: ' % (args.host, args.user))

    si = SmartConnectNoSSL(host=args.vcip,
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
    container = content.rootFolder  # starting point to look into
    viewType = [vim.HostSystem]
    recursive = True

    containerView = content.viewManager.CreateContainerView(container,
                                                            viewType,
                                                            recursive)
    children = containerView.view
    for host in children:  # Iterate through Hosts in the Cluster
        hostname = host.summary.config.name
        if hostname != args.host_ip_to_restart:
            continue

        all_vms = host.vm

        vms = [m for m in all_vms if m.runtime.powerState == "poweredOn"]
        vms_ips = [m.name for m in all_vms if m.runtime.powerState == "poweredOn"]

        logging.info("VMs IN POWERED ON state {} ".format(vms_ips))

        if len(vms) == 0:
            break

        logging.info("Powering Off all VMs on host {}".format(host.name))
        for vm in vms:  # Iterate through each VM on the host
            power_down(vm)

        host_enter_maintenance_mode(host)
        host_reboot(host)
        host_exit_maintenance_mode(host)

        logging.info("Powering ON all VMs on host {}".format(host.name))
        for vm in vms:  # Iterate through each VM on the host
            power_up(vm)


@retry(tries=10)
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
        time.sleep(15)
        if task.info.state is vim.TaskInfo.State.error:
            raise Exception("Could not perform Reboot task on host  %s " % (host.name))
    else:
        logging.error("Host %s is NOT in Maintenance Mode state, Cannot Do Restart!" % host.name)


@retry(tries=10)
def host_exit_maintenance_mode(host):
    if host.runtime.inMaintenanceMode:
        logging.info("Switching to Exit Maintenance Mode for host %s" % (host.name))
        task = host.ExitMaintenanceMode_Task(0)
        while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
            time.sleep(10)
            logging.info("Exit Maintenance task state is %s " % task.info.state)
        time.sleep(15)
        if task.info.state is vim.TaskInfo.State.error:
            raise Exception("Could not perform Exit maintenance mode task on host  %s " % (host.name))
    else:
        logging.error("Host %s is already NOT in Maintenance Mode state!" % host.name)


@retry(tries=10)
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


@retry(tries=10)
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


@retry(tries=10)
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
