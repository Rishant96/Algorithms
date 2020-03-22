def insertion_sort(items):
    """Sorts a list ascendingly using insertion sort."""
    for i in range(1, len(items)):
        val = items[i]

        j = i - 1
        while j >= 0 and val < items[j]:
            items[j+1] = items[j]
            j -= 1
        items[j+1] = val
