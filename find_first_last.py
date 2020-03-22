from time import thread_time_ns


def find_first(input, target):
    input_len = len(input)
    if input_len == 0:
        return None
    elif input_len == 1 and input[0] != target:
        return None
    mid = int((input_len - 1) / 2)
    if input[mid] == target:
        if mid-1 < 0:
            return mid
        if input[mid-1] == target:
            return find_first(input[:mid], target)
        else:
            return mid
    elif input[mid] > target:
        return find_first(input[:mid], target)
    else:
        ans = find_first(input[mid+1:], target)
        if ans is not None:
            return ans + mid + 1
        else:
            return None


def find_last(input, target):
    input_len = len(input)
    if input_len == 0:
        return None
    elif input_len == 1 and input[0] != target:
        return None
    mid = int((input_len - 1) / 2)
    if input[mid] == target:
        if mid+1 > input_len-1:
            return mid
        if input[mid+1] == target:
            return mid + 1 + find_last(input[mid+1:], target)
        else:
            return mid
    elif input[mid] > target:
        return find_last(input[:mid], target)
    else:
        ans = find_last(input[mid+1:], target)
        if ans:
            return ans + mid + 1
        else:
            return None


def timed(func):
    def timed_function(*args):
        old_time = thread_time_ns()
        result = func(*args)
        new_time = thread_time_ns()
        print('Time taken for test to conclude: '
              f'{float((new_time - old_time)/(10**6))} (in milliseconds)',
              end='\n\n')
        return result
    return timed_function


@timed
def test(arr, target):
    print('Target:', target)

    first, last = find_first(arr, target),\
        find_last(arr, target)

    if first is None or last is None:
        print('does not occur')
    else:
        print(f'First: {first}, Last: {last}')


def conduct_timed_tests(targets, mul):
    array_1 = [2]*20*mul + [3]*25*mul + [5]*25*mul + [8]*5*mul + [9]*25*mul
    print('Sequence size:', len(array_1))
    print('-' * 80)
    for target in targets:
        test(array_1, target)


if __name__ == '__main__':
    conduct_timed_tests(targets=[8, 5, 2, 4, 9, 1, 10, 3], mul=1)
