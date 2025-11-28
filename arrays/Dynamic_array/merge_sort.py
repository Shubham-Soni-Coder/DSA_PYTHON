class mergesort:
    """
    merge sort:
    1. divide the array into two parts until arrray have 1 element left
    2. merge the array in sorted order
    """

    def merge_sort(self, A, start, end):
        if start < end:
            mid = start + (end - start) // 2
            self.merge_sort(A, start, mid)  # left half
            self.merge_sort(A, mid + 1, end)  # right half

            return self.merge(A, start, mid, end)

        else:
            return A

    def merge(self, A, start, mid, end):
        temp = []
        i = start
        j = mid + 1

        while i <= mid and j <= end:
            if A[i] <= A[j]:
                temp.append(A[i])
                i += 1
            else:
                temp.append(A[j])
                j += 1

        while i <= mid:
            temp.append(A[i])
            i += 1
        while j <= end:
            temp.append(A[j])
            j += 1

        for k in range(len(temp)):
            A[start + k] = temp[k]

        return A


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 1]
    merge_object = mergesort()
    print(merge_object.merge_sort(A, 0, len(A) - 1))
