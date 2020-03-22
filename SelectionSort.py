def selection_sort(items):
    """Sorts a list ascendingly using selection sort."""
    for i in range(len(items)):
        pos = i
        for j in range(i+1, len(items)):
            if items[pos] > items[j]:
                pos = j
        swap = items[i]
        items[i] = items[pos]
        items[pos] = swap
