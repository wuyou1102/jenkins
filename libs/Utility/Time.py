import time


def get_timestamp(time_fmt='%Y_%m_%d-%H_%M_%S', t=None):
    t = t if t else time.time()
    return time.strftime(time_fmt, time.localtime(t))


def convert_timestamp(str, time_fmt='%Y_%m_%d-%H_%M_%S'):
    return time.mktime(time.strptime(str, time_fmt))
