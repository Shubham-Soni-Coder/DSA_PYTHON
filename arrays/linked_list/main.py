from mylinked import LinkedList


L = LinkedList()

L.insert_head(10)
L.insert_head(20)
L.insert_head(30)

print(L)
L.append(60)
print(L)
L.insert_after(20, 25)
print(L)

L.clear()
print(L.__len__())
