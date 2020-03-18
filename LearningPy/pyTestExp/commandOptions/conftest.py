import csv

import pytest


def pytest_addoption(parser):
    print ("** This is addoption")
    parser.addoption(
        "--testDirPath", action="store", default="type1", help="directory path in which we need to fetch test info"
    )


@pytest.fixture()
def printTests(request):
    return request.config.getoption("--testDirPath")


def pytest_runtest_setup(item):
    print ("** This is  pytest_runtest_setup", item)


def pytest_collection_modifyitems(session, config, items):
    print("** This is python_collection_modifyitems")
    path = config.getoption('testDirPath')

    if path:
        # open file
        with open(path, mode='w') as fd:
            writer = csv.writer(fd)
            writer.writerow(["title", "description", "markers"])

            for item in items:
                title = item.nodeid
                writer.writerow([title])
