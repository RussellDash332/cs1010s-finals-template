#!/usr/bin/env python3
## CS1010S Apr16 Template

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
Queues are supported by the following functions:
• make_queue(): returns an empty queue.
• enqueue(q, item): adds item to the back of queue q.
• dequeue(q): removes the item at the front of the queue q, and returns it. If the queue is
empty, None is returned.
• size(q): returns the number of items in the queue q.
"""
def make_queue():
    pass # remove this line

def enqueue(q, item):
    pass # remove this line

def dequeue(q):
    pass # remove this line

def size(q):
    pass # remove this line

## Question 2B
def below_4(p1, p2):
    pass # remove this line

## Question 2C
def priority_enqueue(q, fn, p):
    pass # remove this line

## Question 2D
"""
Answer here.
"""

## Question 2E
"""
Answer here.
"""

## Question 2F
"""
Answer here.
"""

## Question 3A
def valid_heap(node):
    pass # remove this line
    
## Question 3B
def swap(n1, n2):
    pass # remove this line

## Question 3C
def bubble_up(node):
    pass # remove this line

## Question 3D
def bubble_down(node):
    pass # remove this line

## Question 3E
"""
Answer here.
"""

## Question 3F
"""
Answer here.
"""

## Provided for Question 4
class Jedi:
    def __init__(self, name):
        self.name = name
        self.powers = ['jump', 'heal', 'mind trick', 'push']

    def do(self, action):
        if action in self.powers:
            print(self.name + " performs Force " + action)
        else:
            print(self.name + " does not know Force " + action)

class Sith:
    def __init__(self, name):
        self.name = "Darth " + name
        self.powers = ['jump', 'lightning', 'choke', 'push']

    def do(self, action):
        if action in self.powers:
            print(self.name + " performs Force " + action)
        else:
            print(self.name + " does not know Force " + action)

## Question 4A
##maul = Sith("Maul")
##maul.do("lightning")
##
##yoda = Jedi("Yoda")
##yoda.do("choke")
"""
Answer here.
"""

## Question 4B
class JediTurnSith(Jedi,Sith):
    def __init__(self,name):
        super().__init__(name)
"""
Answer here.
"""

## Question 4C and 4D
class ForceUser:
    def __init__(self, name):
        self.name = name
        self.powers = [] # creates empty list of powers
        
    def do(self, action):
        if action in self.powers:
            print(self.name + " performs Force " + action)
        else:
            print(self.name + " does not know Force " + action)

class Jedi(ForceUser):
    pass # remove this line

class Sith(ForceUser):
    pass # remove this line

class JediTurnSith: # add the superclasses in the correct order
    pass # remove this line

## Test Cases
def compare(number,got,expected):
    if got == expected:
        print(f'Test {number} : Passed!')
    else:
        print(f'Test {number} : Failed!')
        print(f'Expected {expected}, got {got}')
    print()

# Made the lazy version of age and Node to prevent error. Do not modify :)
def age(p):
    if p == 'Andy':
        return 4
    elif p == 'Bob':
        return 30
    elif p == 'Jack':
        return 2
    else:
        return 18

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

one = Node(1)
two = Node(2)
four = Node(4)
five = Node(5)
seven = Node(7)
eleven = Node(11)
sixteen = Node(16)
eighteen = Node(18)
twenty_one = Node(21)
twenty_four = Node(24)
thirty = Node(30)

another_five = Node(5)
another_eleven = Node(11)
another_twenty_four = Node(24)
another_sixty_seven = Node(67)
another_fourty_eight = Node(48)
another_fifty_two = Node(52)
newbie_eight = Node(8)

yet_another_eleven = Node(11)
yet_another_twenty_four = Node(24)
yet_another_sixty_seven = Node(67)
yet_another_fourty_eight = Node(48)
yet_another_fifty_two = Node(52)
yet_another_fifty_five = Node(55)

# Heap 1
##       2
##    4     7
## 18     21
two.left, two.right = four, seven
four.parent, four.left = two, eighteen
seven.parent, seven.left = two, twenty_one
eighteen.parent, twenty_one.parent = four, seven

# Heap 2
##         5
##    11      24
## 30   16   1
five.left, five.right = eleven, twenty_four
eleven.parent, eleven.left, eleven.right = five, thirty, sixteen
twenty_four.parent, twenty_four.left = five, one
thirty.parent, sixteen.parent, one.parent = eleven, eleven, twenty_four

# Heap 3
##         5
##    11       24
## 67   48   52
##     8
another_five.left, another_five.right = another_eleven, another_twenty_four
another_eleven.left, another_eleven.right, another_eleven.parent = another_sixty_seven, another_fourty_eight, another_five
another_twenty_four.parent, another_twenty_four.left = another_five, another_fifty_two
another_sixty_seven.parent, another_fourty_eight.parent, another_fifty_two.parent = another_eleven, another_eleven, another_twenty_four
another_fourty_eight.left, newbie_eight.parent = newbie_eight, another_fourty_eight

# Heap 4
##         55
##    11       24
## 67   48   52
yet_another_fifty_five.left, yet_another_fifty_five.right = yet_another_eleven, yet_another_twenty_four
yet_another_eleven.left, yet_another_eleven.right, yet_another_eleven.parent = yet_another_sixty_seven, yet_another_fourty_eight, yet_another_fifty_five
yet_another_twenty_four.parent, yet_another_twenty_four.left = yet_another_fifty_five, yet_another_fifty_two
yet_another_sixty_seven.parent, yet_another_fourty_eight.parent, yet_another_fifty_two.parent = yet_another_eleven, yet_another_eleven, yet_another_twenty_four

def min_node(n1, n2, n3):
    return min(list(filter(lambda x:x != None,[n1,n2,n3])),key=lambda x:x.value)

# Pro tip : drag all the lines that you want to comment/uncomment and press Alt+3/4

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    compare(1,below_4('Andy','Bob'),False)
    compare(2,below_4('Jack','Bob'),True)
    compare(3,below_4('Andy','Jack'),False)

def test_q3():
    print('Testing Question 3...')
    print('='*20)
    compare(1,valid_heap(one),True)
    compare(2,valid_heap(two),True)
    compare(3,valid_heap(four),True)
    compare(4,valid_heap(seven),True)
    compare(5,valid_heap(eleven),True)
    compare(6,valid_heap(sixteen),True)
    compare(7,valid_heap(eighteen),True)
    compare(8,valid_heap(twenty_one),True)
    compare(9,valid_heap(thirty),True)
    compare(10,valid_heap(five),False)
    compare(11,valid_heap(twenty_four),False)

    swap(five, one) # five is 1 and one is 5
    compare(12,eleven.parent.value,1)
    compare(13,twenty_four.left.value,5)
    
    swap(five, one) # back to the original heap
    compare(14,eleven.parent.value,5)
    compare(15,twenty_four.left.value,1)

    bubble_up(newbie_eight)
    compare(16,another_five.left.value,8)
    compare(17,another_sixty_seven.parent.value,8)
    compare(18,another_fourty_eight.value,11)
    compare(19,newbie_eight.value,48)
    compare(20,another_eleven.value,8)

    bubble_down(yet_another_fifty_five)
    compare(21,yet_another_twenty_four.parent.value,11)
    compare(22,yet_another_fifty_five.left.value,48)
    compare(23,yet_another_fourty_eight.value,55)
    compare(24,yet_another_eleven.right.value,55)
    compare(25,yet_another_fourty_eight.parent.value,48)

def test_q4d():
    print('Testing Question 4D...')
    print('='*20)
    try:
        emperor = Sith("Sidious", "Palpatine")
        compare(1,emperor.name,'Darth Sidious')
        compare(2,emperor.alias,'Palpatine')

        vader = JediTurnSith("Vader", "Anakin")
        compare(3,vader.name,'Darth Vader')
        compare(4,vader.alias,'Anakin')
    except Exception as e:
        print(e)
        print('Error occured. Please make sure all methods are well-defined.\n')

test_q2b()
test_q3()
test_q4d()
