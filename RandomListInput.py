from random import shuffle


def getList(n):
    list = []
    for i in range(n):
        list.append(i+1)
    shuffle(list)
    return list


if __name__ == '__main__':
    print('Testing getList,')
    for i in range(3, 6):
        print(f'{i}:', getList(i))
