#!/usr/bin/env python3
## CS1010X Jun16 Template

## Question 1A
def triple(*args):
    pass # remove this line

## Question 1B
def add_one(*args):
    pass # remove this line

## Question 1C
def filter_odd(*args):
    pass # remove this line

## Question 1D
def composen(f,g):
    return f # remove this line

## Question 1E
"""
Answer here.
"""

## Question 1F
def wrapper(f):
    return f # remove this line

## Question 2A
def deep_copy(lst):
    return lst # remove this line

## Question 2B
def deep_copy_check(lst1,lst2):
    pass # remove this line

## Question 2C
def deep_replace(lst,a,b):
    pass # remove this line

## Question 2D
def counting_deep_replace(lst,a,b):
    pass # remove this line

## Question 3A
def paths(m,n):
    pass # remove this line

## Question 3B
"""
Time :
Space :
"""

## Question 3C
def blocked_paths(m,n,blocks):
    pass # remove this line

## Question 3D
def broken_paths(m,n,blocks):
    pass # remove this line

## Question 3E
def dp_broken_paths(m,n,blocks):
    pass # remove this line

## Question 4A
"""
Answer here.
"""

## Question 4B
def quicksort(lst):
    pass # remove this line

## Question 4C
"""
Time :
Space :
"""

## Question 4D
"""
Answer here.
"""

## Question 4E
"""
Answer here.
"""

## Question 4F
"""
Answer here.
"""

## Test Cases
def compare(number,got,expected):
    if got == expected:
        print(f'Test {number} : Passed!')
    else:
        print(f'Test {number} : Failed!')
        print(f'Expected {expected}, got {got}')
    print()

# Pro tip : drag all the lines that you want to comment/uncomment and press Alt+3/4

def test_q1a():
    print('Testing Question 1A...')
    print('='*20)
    compare(1,triple(1,2),(3,6))
    compare(2,triple(1,2,3),(3,6,9))

def test_q1b():
    print('Testing Question 1B...')
    print('='*20)
    compare(1,add_one(2,3),(3,4))
    compare(2,add_one(1,2,3),(2,3,4))
    
def test_q1c():
    print('Testing Question 1C...')
    print('='*20)
    compare(1,filter_odd(1,2,3),(1,3))
    compare(2,filter_odd(2,4,6),())

def test_q1d():
    print('Testing Question 1D...')
    print('='*20)
    alpha = composen(triple,add_one)
    beta = composen(add_one,triple)
    gamma = composen(alpha,beta)
    compare(1,alpha(1,2,3),(6,9,12))
    compare(2,beta(1,2,3),(4,7,10))
    compare(3,gamma(1,2,3),(15,24,33))

def test_q1e():
    print('Testing Question 1E...')
    print('='*20)
    alpha = composen(triple,add_one)
    beta = composen(add_one,triple)
    delta = composen(alpha,composen(filter_odd,beta))
    print('delta(1,2,3,4,5) =',delta(1,2,3,4,5))
    print()

def test_q1f():
    print('Testing Question 1F...')
    print('='*20)
    new_triple = wrapper(triple)
    new_add_one = wrapper(add_one)
    compare('X',new_add_one(new_triple(1,2,3)),(4,7,10))

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    a = [[[1],2],3,4]
    b = deep_copy(a)
    compare(1,deep_copy_check(a,b),True)
    b[0][0] = a[0][0]
    compare(2,deep_copy_check(a,b),False)
    b[0] = a[0]
    compare(3,deep_copy_check(a,b),True)
    c = deep_copy(b)
    compare(4,deep_copy_check(a,c),True)
    d = c.copy()
    compare(4,deep_copy_check(c,d),False)

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    a = [[[1],2],3,4]
    deep_replace(a,2,3)
    compare(1,a,[[[1], 3], 3, 4])
    deep_replace(a,3,5)
    compare(2,a,[[[1], 5], 5, 4])
    deep_replace(a,5,1)
    compare(3,a,[[[1], 1], 1, 4])
    deep_replace(a,1,9)
    compare(4,a,[[[9], 9], 9, 4])

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)
    a = [[[1],2],3,4]
    compare(1,counting_deep_replace(a,2,3),1)
    compare(2,a,[[[1], 3], 3, 4])
    compare(3,counting_deep_replace(a,2,3),0)
    compare(4,counting_deep_replace(a,3,5),2)
    compare(5,a,[[[1], 5], 5, 4])
    compare(6,counting_deep_replace(a,5,1),2)
    compare(7,a,[[[1], 1], 1, 4])
    compare(8,counting_deep_replace(a,1,9),3)
    compare(9,a,[[[9], 9], 9, 4])

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    compare(1,paths(1,1),2)
    compare(2,paths(2,2),6)
    compare(3,paths(3,1),4)
    compare(4,paths(3,2),10)
    compare(5,paths(3,3),20)

def test_q3c():
    print('Testing Question 3C...')
    print('='*20)
    compare(1,blocked_paths(1,1,((0,0),)),0)
    compare(2,blocked_paths(1,1,((1,0),)),1)
    compare(3,blocked_paths(1,1,((0,1),)),1)
    compare(4,blocked_paths(1,1,((1,1),)),0)
    compare(5,blocked_paths(2,2,((1,1),)),2)
    compare(6,blocked_paths(2,2,((1,1),(0,1))),1)

def test_q3d():
    print('Testing Question 3D...')
    print('='*20)
    compare(1,broken_paths(1,1,((1,1,1,0),)),1)
    compare(2,broken_paths(1,1,((1,1,0,1),)),1)
    compare(3,broken_paths(1,1,((1,0,0,0),)),1)
    compare(4,broken_paths(1,1,((0,1,0,0),)),1)
    compare(5,broken_paths(2,2,((0,1,0,0),)),3)
    compare(6,broken_paths(2,2,((1,1,0,1),)),4)
    compare(7,broken_paths(2,2,((1,1,0,1),(1,1,1,0))),2)

def test_q3e():
    print('Testing Question 3E...')
    print('='*20)
    compare(1,dp_broken_paths(1,1,((1,1,1,0),)),1)
    compare(2,dp_broken_paths(1,1,((1,1,0,1),)),1)
    compare(3,dp_broken_paths(1,1,((1,0,0,0),)),1)
    compare(4,dp_broken_paths(1,1,((0,1,0,0),)),1)
    compare(5,dp_broken_paths(2,2,((0,1,0,0),)),3)
    compare(6,dp_broken_paths(2,2,((1,1,0,1),)),4)
    compare(7,dp_broken_paths(2,2,((1,1,0,1),(1,1,1,0))),2)

def test_q4():
    print('Testing Question 3E...')
    print('='*20)
    a = [4,2,56,23,12,1,32,5,7]
    quicksort(a)
    compare('sort',a,[1, 2, 4, 5, 7, 12, 23, 32, 56])
    test = [9,8,7,6,5,4,3,2,1]
    quicksort(test)
    compare('dummy list',test,sorted(test))

test_q1a()
test_q1b()
test_q1c()
test_q1d()
test_q1e()
test_q1f()
test_q2b()
test_q2c()
test_q2d()
test_q3a()
test_q3c()
test_q3d()
test_q3e()
test_q4()
