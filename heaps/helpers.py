def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def parent_index(i):
    return (i-2) / 2


def swap(a, b):
    temp = a
    a = b
    b = temp


def fix_up(arr, i):
    while parent_index(i) is not None and arr[parent_index(i)] < arr[i]:
        swap(arr[i], arr(parent_index(i)))
        i = parent_index(i)


def fix_down(arr, n, i):
    while arr[left_child(i)] is not None and arr[right_child(i)] is not None:
        j = left_child(i)
        if arr[j] < a[j + 1] and j is not n -1:
            j += 1
        if arr[i] >= a[j]:
            break
        swap(arr[i], arr[j])
        i = j
