# Write a function revstring(mystr) that uses a stack to reverse the characters in a string.

#from test import testEqual
from pythonds.basic import Stack


def revstring(mystr):
    s = Stack()
    for i in mystr:
        s.push(i)
    #s1 = Stack()
    s1 = ''
    while not s.isEmpty():
        s1 += s.pop()
    return s1


a = "apple"
print(revstring(a))
'''testEqual(revstring('apple'), 'elppa')
testEqual(revstring('x'), 'x')
testEqual(revstring('1234567890'), '0987654321')'''
