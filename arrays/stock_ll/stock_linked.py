class nodes:
    def __init__(self, value):
        self.data = value
        self.next = None


class stock:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None

    def push(self, value):
        newnode = nodes(value)
        newnode.next = self.top
        self.top = newnode

    def traverse(self):
        temp = self.top

        while temp != None:
            print(temp.data, end="=>")
            temp = temp.next

    def peak(self):
        if self.isempty():
            return None
        return self.top.data

    def pop(self):
        if self.top == None:
            return None
        else:
            self.top = self.top.next
