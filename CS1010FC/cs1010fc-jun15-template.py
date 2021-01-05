#!/usr/bin/env python3
## CS1010FC Jun15 Template

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
def num_sum(n):
    pass # remove this line

## Question 2B
def sum_set(n):
    pass # remove this line

## Question 2C
def sum_set_product(n):
    pass # remove this line

## Question 2D
def has_prime_sum(n):
    pass # remove this line

## Question 3A
"""
Answer here.
"""

## Question 3B
"""
Time :
Space :
"""

## Question 3C
def bar(lst):
    pass # remove this line

## Question 3D
# Put your code here

## Question 3E
"""
Answer here.
"""

## Question 3F
"""
Answer here.
"""

## Question 4A
# Not provided, giveaway for 4B

## Question 4B
# Put your code here

## Question 4C
# Put your code here

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

def test_q2a():
    print('Testing Question 2A...')
    print('='*20)
    compare(1,num_sum(2),1)
    compare(2,num_sum(3),2)
    compare(3,num_sum(4),4)
    compare(4,num_sum(5),6)

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    compare(1,sum_set(2),[[1, 1]])
    compare(2,sum_set(3),[[1, 1, 1], [2, 1]]
)
    compare(3,sum_set(4),[[1, 1, 1, 1], [2, 1, 1], [2, 2], [3, 1]])
    compare(4,sum_set(5),[[1, 1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1], [3, 1, 1], [3, 2], [4, 1]])
    compare(5,sum_set(6),[[1, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1], [2, 2, 1, 1], [2, 2, 2], [3, 1, 1, 1], [3, 2, 1], [3, 3], [4, 1, 1], [4, 2], [5, 1]])

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    compare(1,sum_set_product(2),[1])
    compare(2,sum_set_product(3),[1,2]
)
    compare(3,sum_set_product(4),[1,2,3,4])
    compare(4,sum_set_product(5),[1,2,3,4,6])
    compare(5,sum_set_product(6),[1,2,3,4,5,6,8,9])

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)
    compare(1,has_prime_sum(2),False)
    compare(2,has_prime_sum(3),False)
    compare(3,has_prime_sum(4),True)
    compare(4,has_prime_sum(5),True)
    compare(5,has_prime_sum(6),True)
    compare(6,has_prime_sum(11),False)

def test_q3c():
    print('Testing Question 3C...')
    print('='*20)
    test_lst = [9,8,7,6,5,4,3,2,1,2]
    compare("modify",bar(test_lst),test_lst) # Does it modify test_lst?
    compare("sort",test_lst,[1,2,2,3,4,5,6,7,8,9]) # Does it sort test_lst?

test_q2a()
test_q2b()
test_q2c()
test_q2d()
test_q3c()
