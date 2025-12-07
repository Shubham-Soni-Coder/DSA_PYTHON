class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        Use to add element in read or end of the queue
        """
        new_node = Node(value)

        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = self.rear.next

    def dequeue(self):
        """
        Use to remove element from front of the queue
        """
        if self.front == None:
            return "empty"
        else:
            self.front = self.front.next

    def traverse(self):
        temp = self.front

        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next

    def is_empty(self):
        return self.front == None

    def size(self):
        temp = self.front
        counter = 0
        while temp != None:
            counter += 1
            temp = temp.next
        return counter

    def front_item(self):
        if self.front == None:
            return "empty"
        else:
            return self.front.data

    def rear_item(self):
        if self.rear == None:
            return "empty"
        else:
            return self.rear.data

    def clear(self):
        self.front = None
        self.rear = None
