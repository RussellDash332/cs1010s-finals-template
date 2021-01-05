#!/usr/bin/env python3
## CS1010S Apr18 Template

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
def new_layer(n):
    pass # remove this line and replace with your code

## Question 2B
def add_block(layer):
    pass # remove this line and replace with your code

## define LayerFilledException here!

## Question 2C
def remove_block(layer, pos):
    pass # remove this line and replace with your code

## Question 2D
def is_stable(layer):
    pass # remove this line and replace with your code

## Question 2E
def new_tower(height, n):
    pass # remove this line and replace with your code

## Question 2F
def play(tower, level, pos):
    pass # remove this line and replace with your code

## Question 2G
"""
Answer here.
"""

## For Question 3
keys = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
keyd = {'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3,
        'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5,
        'm': 6, 'n': 6, 'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7,
        't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9, ' ': 0}

## Question 3A
def to_dict(keys):
    pass # remove this line and replace with your code
    
## Question 3B
def to_keys(keyd):
    pass # remove this line and replace with your code

## Question 3C
def to_nums(word):
    pass # remove this line and replace with your code

## Question 3D
def to_letters(num):
    pass # remove this line and replace with your code

## Question 3E
"""
Answer here.
"""

## Provided for Question 4, modify if necessary.
class Vehicle:
    def __init__(self, reach):
        self.reach = reach
        self.orders = []
        
    def deliver(self, order):
        if self.reach < order.distance:
            print("Too far")
            return False
        else:
            self.orders.append(order)
            print("Order delivered")
            return True

class Motorcycle(Vehicle):
    def __init__(self, fuel):
        self.fuel = fuel
        self.orders = []
        
    def top_up(self, amount): # top up fuel
        self.fuel += amount
        
    def deliver(self, order):
        if self.fuel < order.distance: # fuel units is in distance
            print("Not enough fuel")
            return False
        else:
            self.orders.append(order) # line 29, must use super() instead
            print("Order delivered")
            return True

## Question 4A
"""
Answer here and modify the code above if necessary.
"""

## Question 4B
class Bicycle: # add the superclass(es) if necessary
    pass # remove this line and replace with your code

## Question 4C
class EScooter: # add the superclass(es) in the correct order
    pass # remove this line and replace with your code

## Test Cases
def compare(number,got,expected):
    if got == expected:
        print(f'Test {number} : Passed!')
    else:
        print(f'Test {number} : Failed!')
        print(f'Expected {expected}, got {got}')
    print()

width = len

class Order:
    def __init__(self, distance):
        self.distance = distance

# Pro tip : drag all the lines that you want to comment/uncomment and press Alt+3/4

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    layer = [True,True,True,True]
    try:
        add_block(layer)
        print('Test failed! Expected LayerFilledException\n')
    except LayerFilledException as e:
        print('Test passed!',e,'\n')
    except Exception as e:
        print(e,'\nTest failed!\n')

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    layer1 = [True,False,True,True]
    layer2 = [False,False,False,True]
    remove_block(layer1,0)
    remove_block(layer2,3)
    remove_block(layer1,3)
    compare(1,layer1,[False,False,True,False])
    compare(2,layer2,new_layer(4))

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)
    layer3 = [False,True,False]
    layer4 = [True,False,True,False]
    compare(1,is_stable(layer3),True)
    compare(2,is_stable(layer4),True)
    remove_block(layer4,0)
    compare(3,is_stable(layer4),False)

def test_q2f(): # My own Jenga game
    print('Testing Question 2F...')
    print('='*20)
    jenga = new_tower(10,4)
    compare(0.1,play(jenga,1,2),None)
    compare(0.2,play(jenga,2,2),None)
    compare(0.3,play(jenga,3,2),None)
    compare(0.4,play(jenga,7,1),None)
    compare(1,play(jenga,7,0),'Game Over!')
    jenga2 = new_tower(4,3)
    compare(0.5,play(jenga2,3,1),None)
    compare(0.6,play(jenga2,2,0),None)
    compare(0.7,play(jenga2,2,2),None)
    compare(0.8,play(jenga2,0,1),None)
    compare(0.9,play(jenga2,4,1),None)
    compare(2,play(jenga2,0,0),'Game Over!')

def test_q3ab():
    print('Testing Question 3AB...')
    print('='*20)
    compare(1,to_dict(keys),keyd)
    compare(2,to_keys(keyd),keys)

def test_q3c():
    print('Testing Question 3C...')
    print('='*20)
    compare(1,to_nums("i luv u"),4058808)
    compare(2,to_nums("cs ten ten s is fun"),2708360836070470386)

def test_q3d():
    print('Testing Question 3D...')
    print('='*20)
    compare('to letters',to_letters(293),['awd', 'awe', 'awf', 'axd', 'axe', 'axf', 'ayd', 'aye', 'ayf', 'azd',
                                          'aze', 'azf', 'bwd', 'bwe', 'bwf', 'bxd', 'bxe', 'bxf', 'byd', 'bye',
                                          'byf', 'bzd', 'bze', 'bzf', 'cwd', 'cwe', 'cwf', 'cxd', 'cxe', 'cxf',
                                          'cyd', 'cye', 'cyf', 'czd', 'cze', 'czf'])
    compare('to letters (sorted)',to_letters(293),sorted(['awd', 'awe', 'awf', 'axd', 'axe', 'axf', 'ayd', 'aye', 'ayf', 'azd',
                                          'aze', 'azf', 'bwd', 'bwe', 'bwf', 'bxd', 'bxe', 'bxf', 'byd', 'bye',
                                          'byf', 'bzd', 'bze', 'bzf', 'cwd', 'cwe', 'cwf', 'cxd', 'cxe', 'cxf',
                                          'cyd', 'cye', 'cyf', 'czd', 'cze', 'czf']))

def test_q4b():
    print('Testing Question 4B...')
    print('='*20)
    try:
        bicycle = Bicycle(5)
        compare(1,bicycle.deliver(Order(3)),True)
        compare(2,bicycle.deliver(Order(5)),False)
        compare(3,bicycle.deliver(Order(8)),False)

        bicycle.hydrate()
        compare(4,bicycle.deliver(Order(5)),True)
    except:
        print('Make sure you have defined all the required methods.\n')

test_q2b()
test_q2c()
test_q2d()
test_q2f()
test_q3ab()
test_q3c()
test_q3d()
test_q4b()
