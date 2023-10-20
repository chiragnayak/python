import time
from functools import wraps

from misc.LearningPy.pyvmomi_projects.ref_git.vmware_pyvmomi_community_samples.my_code import global_config

pylogger = global_config.pylogger


def retry(exceptions=Exception, tries=5, delay=5, backoff=2, logger=None):
    """ Retry calling the decorated function given number of times

    :param exceptions: can be a single exception or a tuple. By default it would retry for all the exceptions
    :param tries: Max retries count in secs
    :param delay: Delay in secs to wait before the next retry is done
    :param backoff: backoff multiplier e.g. value of 2 will double the delay for each retry.
    Keep the value as 1 if the same delay should be used for each retry
    :param logger: logger to use, if not provided pylogger would be used
    :return:
    """
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except Exception as error:
                    msg = "{}, Retrying in {} seconds....".format(str(error), mdelay)
                    if logger:
                        logger.error(msg)
                    else:
                        pylogger.error(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)
        return f_retry
    return deco_retry
