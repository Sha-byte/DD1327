#!/usr/bin/python
# -*- coding: <utf-8> -*-

def fakultet(n):
    f = 1
    if type(n) != int:
        return
    elif n == 0:
        return 1
    elif n >= 1 and type(n) == int:
        for i in range(1, n+1):
            f *= i
        return f
    else:
        return


assert fakultet(5) == 5*4*3*2
assert fakultet(0) == 1
assert fakultet(4) == 4*3*2
assert fakultet([2, 3, 27378]) == None
assert fakultet('hh') == None
assert fakultet(1.234) == None
assert fakultet(True) == None

print('fungerar')
