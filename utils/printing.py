import math


def print_2d_arr(arr, rows, columns=None, width=(2, 0)):
    """
    Prints 2D arrays / matrices. Use 'None' for empty values.
    Usage: print_2d_arr([1, 2, 3, 4, None, 6, 7, 8, 9], 3, 3, (3, 4))
    Parameters,
        arr (array): a simple python array
        rows (integer): number of rows in matrix
        *columns (integer): number of columns in matrix/2d_array,
                calculated automatically from matrix/2d_array length
                and number of rows
                default: None
        *width ((integer, integer)): (total_width, decimal_precision)
                identical to python's float formatter
                default: (2, 0)
    * - optional parameters
    """
    if arr is None or rows is None:
        return False
    if columns is None:
        columns = math.ceil(len(arr)/rows)
    for i in range(rows):
        print('[', end='')
        for j in range(columns):
            index = (i*columns) + j
            line_end = ', '
            if j+1 == columns:
                line_end = ''
            if index < len(arr) and arr[index] is not None:
                item = float(arr[index])
                format_str = '{:' + str(width[0]) + '.' + str(width[1]) + 'f}'
                print(format_str.format(item), end=line_end)
            else:
                print(' '*width[0], end=line_end)
        print('', end=']\n')
    return True


if __name__ == '__main__':
    arr_3x3 = [1, 2, 3, 4, None, 6, 7, 8, 9]
    print('3x3 :', f'(array: {arr_3x3})')
    print_2d_arr(arr_3x3, rows=3, width=(4, 2))

    arr_4x2 = [2, 4, 6, 8, 10, 14, 18]
    print('\n4x2 :', f'array: {arr_4x2}')
    print_2d_arr(arr_4x2, rows=4)
