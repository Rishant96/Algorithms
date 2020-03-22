from time import thread_time_ns


def timed(scale=0):
    """
    Calculates execution time of a function.
    Usage: @timed(scale=3)
    Parameters,
        time_scale (int, 0-9): sets the precision, where,
            0 - seconds,
            1 - deciseconds,
            2 - centiseconds,
            3 - milliseconds,
            6 - microseconds,
            9 - nanoseconds
        default - 0
    """
    def timer_decorator(func):
        def timed_function(*args, **kwargs):
            old_time = thread_time_ns()
            result = func(*args, **kwargs)
            new_time = thread_time_ns()
            fraction = 9 - scale
            fraction_switcher = {
                0: 'seconds',
                1: 'deciseconds',
                2: 'centiseconds',
                3: 'milliseconds',
                6: 'microseconds',
                9: 'nanoseconds',
            }
            time_desc = fraction_switcher.get(scale,
                                              '10**'+str(scale))
            print('Time taken for test to conclude: '
                  f'{float((new_time - old_time)/(10**fraction))} '
                  '(in ' + time_desc + ')',
                  end='\n\n')
            return result
        return timed_function
    return timer_decorator
