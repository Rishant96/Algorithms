def merge_sort(items):
    if len(items) > 1:
        pivot = len(items) // 2
        left = items[:pivot]
        right = items[pivot:]

        merge_sort(left)
        merge_sort(right)

        x, y, z = 0, 0, 0
        while len(left) > x and len(right) > y:
            if left[x] <= right[y]:
                items[z] = left[x]
                x += 1
            else:
                items[z] = right[y]
                y += 1
            z += 1

        while len(left) > x:
            items[z] = left[x]
            x += 1
            z += 1

        while len(right) > y:
            items[z] = right[y]
            y += 1
            z += 1
