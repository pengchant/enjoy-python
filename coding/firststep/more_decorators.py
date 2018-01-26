from time import sleep
from functools import wraps
import  logging

logging.basicConfig()
log = logging.getLogger('retry')


# 定义retry
def retry(f):
    @wraps(f)
    def wrapped_f(*args,**kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1,MAX_ATTEMPTS+1):
            try:
                return f(*args,**kwargs)
            except:
                log.exception("Attempt %s/%s failed: %s",
                              attempt,
                              MAX_ATTEMPTS,
                              (args,kwargs))
                # 休眠
                sleep(10*attempt)
        log.critical('All is %s attempts failed:%s',
                     MAX_ATTEMPTS,
                     (args,kwargs))

    return wrapped_f


counter = 0


@retry
def save_to_database(arg):
    print('write to a database or make a net work call or etc.')
    print('this will be automatically retried if exceptions is thrown.')
    global counter
    counter += 1
    if counter < 2:
        raise ValueError(arg)


if __name__ == "__main__":
    save_to_database("some bad value")