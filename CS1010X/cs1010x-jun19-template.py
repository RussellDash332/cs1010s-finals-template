#!/usr/bin/env python3
## CS1010X Jun19 Template

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
def ways(m,n):
    pass # remove this line

## Question 2B
def blocked_ways(m,n,blocked):
    pass # remove this line

## Question 2C
"""
Time :
Space :
"""

## Question 2D
def memoized_blocked(m,n,blocked):
    pass # remove this line

## Question 2E
def cheapest_path(m,n,blocked):
    pass # remove this line

## Question 3A
"""
Answer here.
"""

## Question 3B
"""
Our MultiSet class implements the following methods:
1. add(item) adds new item to the multiset.
2. extend(seq) adds all the elements of a specified sequence seq to the multiset.
3. contains(item) returns True if the multiset contains the specified item. Returns
False, otherwise.
4. count(item) returns the number of instances of the specified item in the multiset.
"""
class MultiSet:
    def __init__(self):
        self.stuff = []
        
    def add(self,item):
        pass # <T1>
    
    def extend(self,seq):
        pass # <T2>
    
    def contains(self,item):
        pass # <T3>
    
    def count(self,item):
        pass # <T4>

## Question 3C
    def __eq__(self,other):
        pass # remove this line

## Question 3D
class Set(MultiSet):
    pass # remove this line

## Question 3E
class Multiset:
    pass # remove this line

## Question 3F
class Multiset:
    pass # remove this line

## Question 4A
def pancake_sort(a):
    for i in range(len(a)-1):
        cur_small = i
        for j in range(i, len(a)):
            if a[j] < a[cur_small]:
                cur_small = j
        a = a[:cur_small] + reverse(a[cur_small:])
        a = a[:i] + reverse(a[i:])
    return a

def reverse(lst):
    return lst # remove this line

## Question 4B
# Write your code here

## Question 4C
"""
Answer here.
"""

## Question 4D
"""
Answer here.
"""

## Question 4E
"""
Time :
Space :
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

# Feel free to add your own multiset! Not making a function here to add flexibility when adding objects.
print('Testing Question 3E...')
print('='*20)
try:
    s1 = MultiSet()
    s1.add(1)
    s2 = MultiSet(s1)
    s2.extend((2,))
    s2.extend(s1)
    compare(1,s2.count(1),2)
    compare(2,s2.count(2),1)
except:
    print('Complete question 3E properly.\n')
    
def test_q4a():
    print('Testing Question 4A...')
    print('='*20)
    a = [5,3,2,1,6,7,4]
    compare('sort',pancake_sort(a),[1,2,3,4,5,6,7])
    
test_q4a()
