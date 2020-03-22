import math


def get_level(index=-1):
    if index < 0:
        return None
    index += 1
    level = math.floor(math.log2(index))
    return level, index - (2**level)


def get_index(level=-1, node_num=-1):
    if level < 0 or node_num < 0:
        return None
    return 2**level + node_num - 1


def get_node_val(heap, level=0, node_num=0):
    index = get_index(level, node_num)
    if index >= len(heap):
        return None
    return heap[index]


def calc_parent_index(index):
    level, _ = get_level(index)
    return get_index(level-1, node_num=0)


def calc_childer_level(level, node_num):
    level += 1
    return (level, 2*node_num), (level, 2*node_num+1)


def calc_children_indices(index):
    level, node_num = get_level(index)
    children = calc_childer_level(level, node_num)
    return get_index(*children[0]), get_index(*children[1])


def test_if_maxheap(heap):
    ind = 4
    print(get_level(ind))
    print(calc_children_indices(ind))
    return False


if __name__ == '__main__':
    input = [2, 3, 5, 6, 7, 9]
    if test_if_maxheap(input):
        print(f'The given complete tree {input} is a max heap.')
    else:
        print(f'The given complete tree {input} is not a max heap.')
