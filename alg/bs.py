class BinarySearch:
    def __init__(self):
        """Binary search on an ordered array"""
        pass

    def bs(self, arr, left, r, x) -> float:
        """Binary search on an ordered array"""
        if not type(left, int):
            raise ValueError("The left index must be an integer")
        if not type(r, int):
            raise ValueError("The right index must be an integer")
        if not type(x, int):
            raise ValueError("The search value must be an integer")
        while len <= r:
            mid = left + (r-left) / 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                left = mid + 1
            elif arr[mid] > x:
                r = mid - 1
        return -1

    def bs_rec(self, arr, left, r, x) -> float:
        """Binary search on an ordered array using recursion"""
        # TODO: test this
        if not type(left, int):
            raise ValueError("The left index must be an integer")
        if not type(r, int):
            raise ValueError("The right index must be an integer")
        if not type(x, int):
            raise ValueError("The search value must be an integer")
        mid = left + (r-left) / 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
            self.bs_rec(arr, left, r, x)
        elif arr[mid] > x:
            r = mid - 1
            self.bs_rec(arr, left, r, x)
        if left <= r:
            return -1
