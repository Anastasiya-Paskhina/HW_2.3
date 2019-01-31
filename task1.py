from datetime import datetime


def dec_log(path):
    def w_logger(foo):
        def info(*args, **kwargs):
            result = foo(*args, **kwargs)
            with open(path + 'result.txt', 'a', encoding='utf-8') as f:
                f.write('{} {} {} {} {}\n'.format(datetime.now(), foo.__name__, args, kwargs, result))
            print(datetime.now(), foo.__name__, args, kwargs, result)
            return result
        return info
    return w_logger


@dec_log('C:\\Users\\Александр\\PycharmProjects\\HW 2.3\\')
def example(*args, multi=2):
    return args * multi


example('H', 'B', multi=1)