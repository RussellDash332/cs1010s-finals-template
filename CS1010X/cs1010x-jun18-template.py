#!/usr/bin/env python3
## CS1010X Jun18 Template

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

## ADT for Question 2
def make_node(entry, left, right):
    return [entry, left, right]

def entry(tree):
    return tree[0]

def get_left(tree):
    return tree[1]

def get_right(tree):
    return tree[2]

def set_left(tree,x):
    tree[1]=x
    
def set_right(tree,x):
    tree[2]=x

## Question 2A
def make_tree(lst):
    pass # remove this line

## Question 2B
def insert_tree(tree, e):
    pass # remove this line

## Question 2C
"""
Average
Time :
Space :

Worst
Time :
Space :
"""

## Question 2D
# Draw or type here.

## Question 2E
def depth(tree):
    pass # remove this line

## Question 2F
def flatten(tree):
    pass # remove this line

## Question 2G
"""
Answer here.
"""

## Question 2H
def balance_tree(tree):
    pass # remove this line

## Question 2I
"""
Answer here along with the redefined function(s) if any.
"""

## Question 3A
"""
For simplicity, the UndoList supports the following 4 methods:
• append(x) – appends an element x to the end of the list.
• set(n,x) – sets element at index n to x. Throws IndexError if index is out of
bounds.
• undo – reverses (undo) the last mutation (i.e. either append or set operation).
• show – returns a list containing all the elements.
"""
class UndoList:
    pass

## Question 3B
"""
Answer here.
"""

## Question 3C
class LimitedUndoList(UndoList):
    pass

## Question 4A
def interleave(lst):
    pass # remove this line

## Question 4B
# Just like question 4A but in C, so it's redundant in this case.

## Question 4C
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

t = make_tree([3,2,1,6,12,9,4,10,11])

def test_q2e():
    print('Testing Question 2E...')
    print('='*20)
    compare('X',depth(t),6)

def test_q2f():
    print('Testing Question 2F...')
    print('='*20)
    compare('X',flatten(t),[1, 2, 3, 4, 6, 9, 10, 11, 12])

def test_q2h():
    print('Testing Question 2H...')
    print('='*20)
    t2 = make_tree([3,2,1,6,12,9,4,10,11])
    compare(1,depth(t2),6)
    balance_tree(t2)
    compare(2,depth(t2),4)

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    try:
        lst = UndoList()
        compare(1,lst.show(),[])
        
        lst.append(2)
        lst.append(3)
        lst.append(4)
        compare(2,lst.show(),[2,3,4])
        
        lst.set(1,99)
        compare(3,lst.show(),[2,99,4])
        
        lst.undo()
        compare(4,lst.show(),[2,3,4])
        
        lst.undo()
        compare(5,lst.show(),[2,3])
        
        lst.undo()
        compare(6,lst.show(),[2])
        
        lst.undo()
        compare(7,lst.show(),[])
    except:
        print('Error occured. Define all methods properly.\n')
    

def test_q3c():
    print('Testing Question 3C...')
    print('='*20)
    try:
        lst = LimitedUndoList(3)
        compare(1,lst.show(),[])
        
        lst.append(2)
        lst.append(3)
        lst.append(4)
        lst.append(5)
        lst.append(6)
        compare(2,lst.show(),[2,3,4,5,6])
        
        lst.set(2,99)
        compare(3,lst.show(),[2,3,99,5,6])

        lst.undo()
        compare(4,lst.show(),[2,3,4,5,6])

        lst.undo()
        compare(5,lst.show(),[2,3,4,5])

        lst.undo()
        compare(6,lst.show(),[2,3,4])

        lst.undo()
        compare(7,lst.show(),[2,3,4])
    except:
        print('Error occured. Define all methods properly.\n')
    
def test_q4a():
    print('Testing Question 4A...')
    print('='*20)
    a = list(range(10))
    a2 = list(range(12))
    compare(0.1,a,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    compare(0.2,a2,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    interleave(a)
    interleave(a2)
    compare(1,a,[0, 5, 1, 6, 2, 7, 3, 8, 4, 9])
    compare(2,a2,[0, 6, 1, 7, 2, 8, 3, 9, 4, 10, 5, 11])

test_q2e()
test_q2f()
test_q2h()
test_q3a()
test_q3c()
test_q4a()
