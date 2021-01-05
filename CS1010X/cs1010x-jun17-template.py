#!/usr/bin/env python3
## CS1010X Jun17 Template

## Question 1A
"""
Answer here.
"""

## Question 1B
"""
Answer here.
"""

## Question 1C
"""
Answer here.
"""

## Question 1D
"""
Answer here.
"""

## Question 1E
"""
Answer here.
"""

## Question 2A
def is_fibonacci(n):
    pass # remove this line

## Question 2B
"""
Time :
Space :
"""

## Question 2C
def make_memo_fib():
    pass # remove this line

## Question 2D
def make_no_consecutive_filter():
    pass # remove this line

## Question 2E
def combine(f1,f2):
    pass # remove this line

## Question 2F
"""
Answer here.
"""

## Question 3A
def chain(seq,n):
    pass # remove this line

## Question 3B
def count_links(chain):
    pass # remove this line

## Question 3C
"""
Answer here.
"""

## Question 3D
def copy_chain(chain):
    pass # remove this line

## Question 3E
def find_fault(chain):
    pass # remove this line

## Question 4A
def reverse_sort(lst,n):
    pass # remove this line

## Question 4B
"""
Time :
Space :
"""

## Question 4C
"""
Answer here.
"""

## Question 4D
def print_AP(start,stop,step):
    pass # remove this line

## Question 4E
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

a = [1,2,4,1,11,6,7,8,23,5,8,13]

def test_q2a():
    print('Testing Question 2A...')
    print('='*20)
    compare('X',list(filter(is_fibonacci,a)),[1, 2, 1, 8, 5, 8, 13])

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    compare('X',list(filter(make_memo_fib(),a)),[1, 2, 1, 8, 5, 8, 13])

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)
    a = [1,1,2,1,11,1,2,2,2,6,7,7,8,23,8]
    compare('X', list(filter(make_no_consecutive_filter(),a)),[1, 2, 1, 11, 1, 2, 6, 7, 8, 23, 8])

def test_q2e():
    print('Testing Question 2E...')
    print('='*20)
    a = [1,1,2,4,1,11,1,2,2,6,7,7,8,23,5,8,13]
    f = combine(lambda x: x%2==0, lambda x: x<6)
    compare('X', list(filter(f,a)),[2, 4, 2, 2])

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    a = [1,2]
    a += [a]
    b = [4]
    b += [b]
    compare(1,chain((1,2),1),a)
    compare(2,chain((1,2),3),[1,2,[1,2,a]])
    compare(3,chain((4,),4),[4,[4,[4,b]]])

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)
    compare(1,count_links(chain((1,2),1)),1)
    compare(2,count_links(chain([3,2],2)),2)
    compare(3,count_links(chain((4,),4)),4)

def test_q3d():
    print('Testing Question 3D...')
    print('='*20)
    a = chain((1,2),4)
    try:
        a[2][2][0] = 5
        b = copy_chain(a)
        test = [1,2]
        test += [test]
        compare('X',b,[1,2,[1,2,[5,2,test]]])
    except:
        print('Error! Complete question 3A first!\n')

def test_q3e():
    print('Testing Question 3E...')
    print('='*20)
    a = chain((1,2),4)
    try:
        a[2][2][0] = 5
        test = [1,2]
        test += [test]
        compare(1,a,[1,2,[1,2,[5,2,test]]])
        compare(2,find_fault(a),5)
    except:
        print('Error! Complete question 3A first!\n')

def test_q4a():
    print('Testing Question 4A...')
    print('='*20)
    a = [4,12,-1,5,7,2,-5,11,8]
    b = [-4,2,-1,5,17,2,-3,11,8]
    reverse_sort(a,9)
    reverse_sort(b,9)
    compare(1,a[:9],[12, 11, 8, 7, 5, 4, 2, -1, -5])
    compare(2,b[:9],[17, 11, 8, 5, 2, 2, -1, -3, -4])

def test_q4d():
    print('Testing Question 4A...')
    print('='*20)
    compare(1,print_AP(1,5,1),[1, 2, 3, 4])
    compare(2,print_AP(1,9,2),[1, 3, 5, 7])
    compare(3,print_AP(2,10,3),[2, 5, 8])
    compare(4,print_AP(3,16,4),[3,7,11,15])

test_q2a()
test_q2c()
test_q2d()
test_q2e()
test_q3a()
test_q3b()
test_q3d()
test_q3e()
test_q4a()
test_q4d()
