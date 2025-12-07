from mystack import Stack

s = Stack(3)

s.push(3)
s.push(4)
s.push(5)

print(s.traverse())

s.pop()
print(s.traverse())

s.pop()
print(s.traverse())

s.pop()
print(s.traverse())
