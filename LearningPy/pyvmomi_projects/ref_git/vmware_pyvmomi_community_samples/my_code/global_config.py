import logging
import tempfile
import os
import sys
import tests.common.test_logger as logger

DEFAULT_LOG_PATH = "%stmp%sarkin_tests%s" % (os.path.sep, os.path.sep, os.path.sep)
LOG_FILE = "sdm_replays"

TRACE_LEVEL_NUM = 9
logging.addLevelName(TRACE_LEVEL_NUM, "TRACE")
MOCK_VC_NSX_DATA = False
LOG_FILE_NAME = "log_file.log"
MULTIPLE_LABS = False


def get_log_file_path(file_name=None, prefix=None):
    file_path = os.environ.get("LOG_DIR_PATH")
    if not file_path:
        file_path = DEFAULT_LOG_PATH

    if not file_name:
        file_name = os.environ.get("LOG_FILE_NAME_SUFFIX")
        if file_name:
            file_name = "{}{}".format(prefix, file_name)

    if not file_name:
        tmp_file = tempfile.mktemp(prefix=(prefix, "")[prefix is None],
                                   dir=file_path,
                                   suffix=".log")
    else:
        tmp_file = "%s%s%s" % (file_path, os.sep, file_name)

    dpath = make_directory(tmp_file)
    return tmp_file


def configure_logger(file_name=None):
    # set up logging to file - see previous section for more details
    # coloredlogs.install()
    tmp_file = get_log_file_path(file_name, prefix="python_tests_")
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-20s: %(levelname)-8s: %(message)s',
                        datefmt='%m-%d %H:%M:%S',
                        filename=tmp_file,
                        filemode='w')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    # console.setLevel(logging.INFO)

    # set a format which is simpler for console use
    formatter = logging.Formatter('%(asctime)s:  %(filename)-15s: %(lineno)-4d %(levelname)-8s: %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger().addHandler(console)
    pylogger = logging.getLogger()

    pylogger.critical("Log file Name: %s", tmp_file)

    return pylogger




logging.Logger.trace = trace
pylogger = configure_logger()
