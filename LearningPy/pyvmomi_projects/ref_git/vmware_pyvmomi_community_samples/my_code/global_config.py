import logging
import tempfile
import os
import sys


DEFAULT_LOG_PATH = "%stmp%sarkin_tests%s" % (os.path.sep, os.path.sep, os.path.sep)
LOG_FILE = "sdm_replays"

TRACE_LEVEL_NUM = 9
logging.addLevelName(TRACE_LEVEL_NUM, "TRACE")
MOCK_VC_NSX_DATA = False
LOG_FILE_NAME = "log_file.log"
MULTIPLE_LABS = False



def configure_logger(file_name=None):
    # set up logging to file - see previous section for more details
    # coloredlogs.install()
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-20s: %(levelname)-8s: %(message)s',
                        datefmt='%m-%d %H:%M:%S',
                        filename="Logging",
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

    pylogger.critical("Log file Name: %s", "Logging")

    return pylogger


def trace(self, message, *args, **kws):
    # Yes, logger takes its '*args' as 'args'.
    if self.isEnabledFor(TRACE_LEVEL_NUM):
        self._log(TRACE_LEVEL_NUM, message, args, **kws)

logging.Logger.trace = trace
pylogger = configure_logger()
