import ctypes


class MeraList:
    def __init__(self):
        self.size = 1  # Aap kitna items ko store kr skta ho
        self.n = 0  # Aabi kitna items hai

        # Create a C type array witht size = self.size
        self.A = self.__make_array__(self.size)

    def __make_array__(self, capacity):
        # Create a C type array with size capacity
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self.n

    def __str__(self):
        # [1,2,3]
        result = ""
        for i in range(self.n):
            result += str(self.A[i]) + ","
        return "[" + result[:-1] + "]"

    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index < self.n:
                return self.A[index]
            else:
                raise IndexError("Index out of bounds")
        elif isinstance(index, slice):
            # [1:2:3]
            start = index.start
            stop = index.stop
            step = index.step
            return self.A[start:stop:step]
        else:
            raise TypeError("Invalid index type")

    def __delitem__(self, index):
        # delete
        if index < 0 or index >= self.n:
            raise IndexError("Index out of bounds")
        for i in range(index, self.n - 1):
            self.A[i] = self.A[i + 1]
        self.n -= 1

    def __resize__(self, new_capacity):
        B = self.__make_array__(new_capacity)
        self.size = new_capacity

        # copy the content to new array
        for i in range(self.n):
            B[i] = self.A[i]

        # reassign A
        self.A = B

    def __setitem__(self, index, item):
        if index < 0 or index >= self.n:
            raise IndexError("Index out of bounds")
        self.A[index] = item

    def append(self, item):
        if self.n == self.size:
            self.__resize__(self.size * 2)

        # append
        self.A[self.n] = item  # item ko append krta ha
        self.n += 1  # items ko badha rha ha

    def pop(self):
        if self.n == 0:
            raise IndexError("pop from empty list")
        print(self.A[self.n - 1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def index(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "Value Error - not in list"

    def insert(self, index, item):
        if index < 0 or index > self.n:
            raise IndexError("Index out of bounds")
        if self.n == self.size:
            self.__resize__(self.size * 2)
        for i in range(self.n, index, -1):
            self.A[i] = self.A[i - 1]

        self.A[index] = item
        self.n += 1

    def remove(self, item):
        index = self.index(item)
        if type(index) == int:
            self.__delitem__(index)
        else:
            raise ValueError("Value not in list")

    def sort(self):
        from merge_sort import mergesort

        merge_object = mergesort()

        return merge_object.merge_sort(self.A, 0, self.n - 1)
