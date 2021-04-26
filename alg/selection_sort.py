def selection_sort(arr, arr_len):
    """
    Perform a selection sort on an array.
    Runs in O(n^2) so it's not so good
    """
    for i in range(len(arr)):
        min_val = i
        for j in range(i+1, len(arr)):
            if arr[j] < a[min_val]:
                min_val = j
        # swap the items
        arr[i], arr[min_val] = arr[min_val], arr[i]
    return arr


a = [9, 12, 5, 7, 11]
print(selection_sort(a, len(a)))
