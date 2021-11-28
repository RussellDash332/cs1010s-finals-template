## CS1010FC Jun14 Template

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

## Question 2A
"""
Answer here.
"""

## Question 2B
"""
Answer here.
"""

## Question 3A
def mapf(fns, val):
    pass # remove this line, uncomment the next line and replace <T1> and <T2>
    #return list(map(<T1>,<T2>))

## Question 3B
def mapv(fns, v):
    pass # remove this line

## Question 3C
def mapf_oneline(fns, val):
    pass # remove this line

## Question 3D
def filterl(fns, lst):
    pass # remove this line

## Question 3E
def vectorize(f):
    return f # remove this line

filterlv = vectorize(filterl)

## Question 4A
def first_denomination(kinds_of_coins):
    pass # remove this line

## Question 4B
# Replace <T3>, <T4> and <T5>
def cc_iter(a,d):
    to_do = [[a,d]]
    count = 0

    while to_do:
        a,d = to_do.pop()

        if a<0 or d==0:
            pass # <T3>
        elif a == 0:
            pass # <T4>
        else:
            pass # <T5>
    return count

## Question 4C
def trace(f):
    def helper(*args):
        count = [0]
        if args[0] == "count":
            return count[0]
        else:
            count[0] += 1
            return f(*args)
    return helper
"""
Answer here.
"""

## Question 4D
"""
Answer here.
"""

## Question 4E
"""
Answer here.
"""

## Question 5A
def fib(a,b,c,d,n):
    pass # remove this line

## Question 5B
"""
Time :
Space :
"""

## Question 5C
"""
Answer here.
"""

## Question 5D
"""
Answer here.
"""

## Appendix
def cc(amount, kinds_of_coins):
    if amount == 0:
        return 1
    elif amount < 0 or kinds_of_coins == 0:
        return 0
    else:
        return cc(amount, kinds_of_coins-1) + cc(amount - first_denomination(kinds_of_coins), kinds_of_coins)

def count_change(amount):
    return cc(amount,5)

## Test Cases
def compare(number,got,expected):
    if got == expected:
        print(f'Test {number} : Passed!')
    else:
        print(f'Test {number} : Failed!')
        print(f'Expected {expected}, got {got}')
    print()

# Pro tip : drag all the lines that you want to comment/uncomment and press Alt+3/4

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    compare(1,mapf([lambda x: x*2, lambda x: x*x], 4),[8, 16])
    compare(2,mapf([lambda x: x*2, lambda x: x*x, lambda x: x/3], 3),[6, 9, 1.0])

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)
    compare(1,mapv([lambda x: x*2, lambda x: x*x], [4]),[[8, 16]])
    compare(2,mapv([lambda x: x*2, lambda x: x*x], [4, 2]),[[8, 16], [4, 4]])
    compare(3,mapv([lambda x: x, lambda x: x*x, lambda x: x**3], [1,2,3]), [[1, 1, 1], [2, 4, 8], [3, 9, 27]])

def test_q3c():
    print('Testing Question 3C...')
    print('='*20)
    compare(1,mapf_oneline([lambda x: x*2, lambda x: x*x], 4),[8, 16])
    compare(2,mapf_oneline([lambda x: x*2, lambda x: x*x, lambda x: x/3], 3), [6, 9, 1.0])

def test_q3d():
    print('Testing Question 3D...')
    print('='*20)
    compare(1,filterl(lambda x: x<5,[1,20,2,3,11]),[1, 2, 3])
    compare(2,filterl([lambda x: x<5, lambda x: x%2 == 1], [1,20,2,3,11]),[1,3])
    compare(3,filterl([lambda x: x<5, lambda x: x%2 == 1, lambda x: x%2 != 1], [1,20,2,3,11]),[])

def test_q3e():
    print('Testing Question 3E...')
    print('='*20)
    compare(1,filterlv(lambda x: x<5,[[1,20,2,3,11]]),[[1, 2, 3]])
    compare(2,filterlv(lambda x: x<5,[[1,20,2,3,11],[1,5,8]]),[[1, 2, 3], [1]])
    compare(3,filterlv([lambda x: x<5, lambda x: x%2 == 1], [[1,20,2,3,11]]),[[1, 3]])
    compare(4,filterlv([lambda x: x<5, lambda x: x%2 == 1, lambda x: x%2 != 1],[[1,20,2,3,11],[1,2]]),[[], []])

def test_q4b():
    print('Testing Question 4B...')
    print('='*20)
    compare("X",cc_iter(100,5),343)

test_q3a()
test_q3b()
test_q3c()
test_q3d()
test_q3e()
test_q4b()
