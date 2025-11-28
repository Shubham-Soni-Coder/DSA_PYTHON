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

    def insert_head(self, value):
        # Create a new node
        new_node = Node(value)

        # create connection
        new_node.next = self.head

        # update the head
        self.head = new_node

        # update the count
        self.n += 1

    def __str__(self):
        # create a pointer
        conn = self.head

        result = ""

        while conn != None:
            result += str(conn.data) + "->"
            conn = conn.next

        return result[:-2]
