"""
We have a 2x2 matrix and we need to find the celebrity in the matrix
celebrity is a person who is known to all and he dont know any one


we use stack , push all the element in the stack and pop the element one by one and check if the
popped element is celebrity or not

"""

from stock_linked import stock

L = [[0, 0, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]


def find_the_cel(L: list[list[int]]):
    s = stock()

    for i in range(len(L)):
        s.push(i)

    while s.size() >= 2:
        i = s.pop()
        j = s.pop()

        if L[i][j] == 0:
            # i j ko nhi janta mtlb j is not celebrity
            s.push(i)
        else:
            # i j janta mtlb i is not celebrity
            s.push(j)

    # at the end of the loop we will have only one element in the stack
    # that element is the celebrity
    celeb = s.pop()

    # check if the celebrity is known to all and dont know any one
    for i in range(len(L)):
        if i != celeb:
            if L[i][celeb] == 0 or L[celeb][i] == 1:
                print("No cel found")
                return

    print("The celeb is ", celeb)


find_the_cel(L)
