

class Helpers:
    def l_child(i) -> int:
        return 2 * i + 1

    def r_child(i) -> int:
        return 2 * i + 2

    def parent(self, i) -> int:
        return (i-2) / 2

    def fix_up(self, arr, i) -> None:
        """Performs a fix up operation"""
        while self.parent(i) is not None and arr[self.parent(i)] < arr[i]:
            arr[i], arr[self.parent(i)] = arr[self.parent(i)], arr[i]
            i = self.parent(i)

    def fix_down(self, arr, n, i) -> None:
        while arr[self.l_child(i)] is not None and arr[self.r_child(i)] is not None:
            j = self.l_child(i)
            if arr[j] < arr[j + 1] and j is not n - 1:
                j += 1
            if arr[i] >= arr[j]:
                break
            arr[i], arr[j] = arr[j], arr[i]
            i = j
