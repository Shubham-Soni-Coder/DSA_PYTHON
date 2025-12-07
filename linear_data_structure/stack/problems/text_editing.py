"""
In this problem we given a string and also a pattron of undo and redo
when the pattron is u than it means we need to pop the element in the string
when the pattron is r than it means we need to add last poped element in the string

For this problem we use 2 stack the first that have all the element of the string
second is empty
when undo use we pop the element from the first stack and push it in the second stack
when redo use we pop the element from the second stack and push it in the first stack

"""

import sys
import os

# get the Parent dic
parent_dir = os.path.dirname(os.path.dirname(__file__))
# join the path
sys.path.append(os.path.join(parent_dir, "stack_linkedlist"))

from stack_linked import stock


def text_editor(string: str, pattron: str):
    a = stock()
    b = stock()

    for i in string:
        a.push(i)

    for i in pattron:
        if i == "u":
            data = a.pop()
            b.push(data)
        elif i == "r":
            data = b.pop()
            a.push(data)

    res = ""

    while not a.isempty():
        res = a.pop() + res

    return res


print(text_editor("abc", "uurrurur"))
