from aardee_utils.decorators import timed
from aardee_utils.printing import print_2d_arr
import time


@timed(scale=3)
def tableaufy(arr, m, n):
    time.sleep(1.5)


def main():
    m, n = 4, 4
    t_arr = []
    tableaufy(t_arr, m, n)


if __name__ == '__main__':
    main()
