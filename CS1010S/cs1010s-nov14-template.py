#!/usr/bin/env python3
## CS1010S Nov14 Template

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

## Question 1F
"""
Answer here.
"""

# The following is given but not provided, so I made the hardcoded version.
def staircases(n):
    provided = [[],
                [(1, 2)],
                [(1, 3)],
                [(1, 4), (2, 3)],
                [(1, 2, 3), (1, 5), (2, 4)],
                [(1, 2, 4), (1, 6), (2, 5), (3, 4)],
                [(1, 2, 5), (1, 3, 4), (1, 7), (2, 6), (3, 5)],
                [(1, 2, 6), (1, 3, 5), (1, 8), (2, 3, 4), (2, 7), (3, 6), (4, 5)]
                ]
    try:
        return provided[n-2]
    except:
        print("Don't use this number, try n between 2 and 9 inclusive instead")
        return provided[0]

## Question 2A
def widest(n):
    pass # remove this line

## Question 2B
def shortest(n):
    pass # remove this line

## Question 2C
def can_reach(h, n):
    pass # remove this line

## Question 2D
def better_stairs(max_gap, n):
    pass # remove this line

## Question 2E
def is_pyramid(steps):
    pass # remove this line

## Question 2F
def is_symmetric(s):
    pass # remove this line

class SecretMessage:
## Question 3A
## Answer here.
    def __init__(): # add the parameter(s), if any
        pass # remove this line

## Question 3B
    def read(): # add the parameter(s), if any
        pass # remove this line
    
## Question 3C
    def encrypt(): # add the parameter(s), if any
        pass # remove this line

## Question 3D
    def decrypt(): # add the parameter(s), if any
        pass # remove this line

## Question 3E
    def copy(): # add the parameter(s), if any
        pass # remove this line

## Provided for Question 4A
def get_terms(series, n):
    result = []
    for i in range(n):
        result.append(series.get())
    return result

class NaturalNumbers:
    def __init__(self):
        self.count = 0

    def get(self):
        self.count += 1
        return self.count

## Question 4A
class Series:
    pass # remove this line

## Provided for Question 4B
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

## Question 4B
fibs = None # replace with your answer

## Question 4C
"""
Time :
Space :
"""

## Question 4D
class Fibs:
    pass # remove this line

## Question 4E
class FilterSeries:
    pass # remove this line

## Question 4F
class LimitedSeries:
    pass # remove this line

## Appendix
def sum(term, a, next, b):
    if (a>b):
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)

def fold(op, f, n):
    if n==0:
        return f(0)
    else:
        return op(f(n), fold(op, f, n-1))

def enumerate_interval(low, high):
    return tuple(range(low,high+1))

def filter(pred, seq):
    if seq == ():
        return ()
    elif pred(seq[0]):
        return (seq[0],) + filter(pred, seq[1:])
    else:
        return filter(pred, seq[1:])

def accumulate(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))

def is_prime(x):
    import math
    if x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x) + 1)):
            if x%i == 0:
                return False
        return True

## Test Cases
def compare(number,got,expected):
    if got == expected:
        print(f'Test {number} : Passed!')
    else:
        print(f'Test {number} : Failed!')
        print(f'Expected {expected}, got {got}')
    print()

# Pro tip : drag all the lines that you want to comment/uncomment and press Alt+3/4

def test_q2a():
    print('Testing Question 2A...')
    print('='*20)
    compare(1,widest(5),2)
    compare(2,widest(7),3)

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    compare(1,shortest(6),3)
    compare(2,shortest(7),4)

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    compare(1,can_reach(5,7),True)
    compare(2,can_reach(3,7),False)

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)
    compare('X',better_stairs(2,9),[(1, 3, 5), (2, 3, 4), (4, 5)])

def test_q3(): # the sample execution is sufficient without adding/modifying more objects in this case :)
    print('Testing Question 3...')
    print('='*20)
    try:
        m1 = SecretMessage("Congrats on surviving CS1010S!")
        compare(1,m1.read(),"Congrats on surviving CS1010S!")
        compare(2,m1.encrypt(12345),m1)
        compare(3,m1.read(),"*ENCRYPTED*")
        m2 = m1.copy()
        compare(4,m1.decrypt(54321),m1)
        compare(5,m1.read(),"*GARBLED*")
        compare(6,m2.read(),"*ENCRYPTED*")
        compare(7,m2.decrypt(12345),m2)
        compare(8,m2.read(),"Congrats on surviving CS1010S!")
        compare(9,m2.encrypt(54321),m2)
        compare(10,m2.read(),"*ENCRYPTED*")
        compare(11,m2.encrypt(12345),m2)
        compare(12,m2.read(),"*ENCRYPTED*")
        m3 = m2.copy()
        compare(13,m2.decrypt(12345),m2)
        compare(14,m2.read(),"*ENCRYPTED*")
        compare(15,m2.decrypt(54321),m2)
        compare(16,m2.read(),"Congrats on surviving CS1010S!")
        compare(17,m2.decrypt(11111),m2)
        compare(18,m2.read(),"Congrats on surviving CS1010S!")
        compare(19,m3.decrypt(54321),m3)
        compare(20,m3.read(),"*GARBLED*")
    except Exception as e:
        print(e)
        print('Error occured. Make sure all methods are well-defined.\n')

def test_q4a():
    print('Testing Question 4A...')
    print('='*20)
    try:
        even_nums = Series(lambda x: 2*x)
        compare(1,get_terms(even_nums,5),[2,4,6,8,10])
        compare(2,get_terms(even_nums,5),[12,14,16,18,20])
    except Exception as e:
        print(e)
        print('Error occured. Make sure all methods are well-defined.\n')

def test_q4b():
    print('Testing Question 4B...')
    print('='*20)
    try:
        compare('X',get_terms(fibs,10),[0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    except Exception as e:
        print(e)
        print('Error occured. Make sure all methods are well-defined.\n')

def test_q4d():
    print('Testing Question 4D...')
    print('='*20)
    try:
        faster_fibs = Fibs()
        compare(1,get_terms(faster_fibs,5),[0, 1, 1, 2, 3])
        compare(2,get_terms(faster_fibs,5),[5, 8, 13, 21, 34])
    except Exception as e:
        print(e)
        print('Error occured. Make sure all methods are well-defined.\n')

def test_q4e():
    print('Testing Question 4E...')
    print('='*20)
    try:
        primes = FilterSeries(is_prime,NaturalNumbers())
        compare('X',get_terms(primes,10),[2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    except Exception as e:
        print(e)
        print('Error occured. Make sure all methods are well-defined.\n')

def test_q4f():
    print('Testing Question 4F...')
    print('='*20)
    try:
        first5 = LimitedSeries(NaturalNumbers(),5)
        compare('X',get_terms(first5,8),[1, 2, 3, 4, 5, None, None, None])
    except Exception as e:
        print(e)
        print('Error occured. Make sure all methods are well-defined.\n')

test_q2a()
test_q2b()
test_q2c()
test_q2d()
test_q3()
test_q4a()
test_q4b()
test_q4d()
test_q4e()
test_q4f()
