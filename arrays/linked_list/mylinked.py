class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # matlb ya ek empty linked list
        self.n = 0  # ya bta rha h ki kitna node ha linked list ma

    def __len__(self):
        # length of the linked list is no. of node in linked list
        return self.n

    def __str__(self):
        # create a pointer
        conn = self.head

        result = ""

        while conn != None:
            result += str(conn.data) + "->"
            conn = conn.next
        return result[:-2]

    def __getitem__(self, index):
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            pos += 1
            curr = curr.next

        raise IndexError("Index out of range")

    def insert_head(self, value):
        # Create a new node
        new_node = Node(value)

        # create connection
        new_node.next = self.head

        # update the head
        self.head = new_node

        # update the count
        self.n += 1

    def append(self, value):
        # create a new node
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n += 1
            return

        # create a connection
        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = new_node
        self.n += 1

    def insert_after(self, after, value):
        # create a new node
        new_node = Node(value)

        # create a connection
        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            print("item not found")

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return

        self.head = self.head.next
        self.n -= 1

    def pop(self):

        if self.head == None:
            return "Empty"

        curr = self.head

        if curr.next == None:
            return self.delete_head()

        while curr.next.next != None:
            curr = curr.next

        # curr -> second last node
        curr.next = None
        self.n -= 1

    def remove(self, value):
        curr = self.head

        if curr == None:
            return "Empty"

        if curr.data == value:
            return self.delete_head()

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next

        if curr.next == None:
            return "Not Found"
        else:
            curr.next = curr.next.next
            self.n -= 1

    def search(self, item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos += 1
        return "Not Found"

    def replace_max(self, value):
        temp = self.head
        max = temp

        while temp != None:
            if temp.data > max.data:
                max = temp
            temp = temp.next

        max.data = value

    def odd_sum(self):
        curr = self.head  # 0
        pos = 0
        sum = 0
        while curr != None:
            if pos % 2 != 0:
                sum += curr.data
            pos += 1
            curr = curr.next
        return sum
