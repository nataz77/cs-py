def quick_sort_range(arr, first, last):
    """
    Quick sort implementation
    Runs in O(n log n) and uses constant space but it' not stable
    """
    if last < first:
        return

    pivot = arr[last]
    i = first
    for j in range(first, last):
        if arr[j] < pivot:
            # move it to the back
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1

    arr[i], arr[last] = arr[last], arr[i]
    # recurse on the two partition
    # left side
    quick_sort_range(arr, first, i - 1)
    # right side
    quick_sort_range(arr, i + 1, last)


# wrapper function
def quick_sort(arr):
    """Performs a quick sort"""
    if len(arr) == 1:
        return arr
    quick_sort_range(arr, 0, len(a)-1)


a = [9, 12, 5, 7, 11]
quick_sort(a)
print(a)
