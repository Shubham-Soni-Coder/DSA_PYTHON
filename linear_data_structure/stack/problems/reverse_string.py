import sys
import os

# get the Parent dic
parent_dir = os.path.dirname(os.path.dirname(__file__))
# join the path
sys.path.append(os.path.join(parent_dir, "stack_linkedlist"))

from stack_linked import stock


""" 
We need to reverse the string using stack 
1. push the element into the string 
2. print the first element in the string , when the isempty is true
3. pop the element from the string 
"""

st = stock()


def reverse_string(string: str) -> str:
    for i in string:
        st.push(i)

    while st.isempty() == False:
        print(st.peak(), end="")
        st.pop()
    return ""


print(reverse_string("hello"))
