#!/usr/bin/env python3
## CS1010S Apr15 Template

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
def half_price(item):
    pass # remove this line

## Question 2B
def half_price_above_20(item):
    pass # remove this line

## Question 2C
"""
Answer here.
"""

## Question 2D
"""
Answer here.
"""

## Question 2E
def best_item(coupon, items):
    pass # remove this line

## Question 3A
def count_males(flies):
    pass # remove this line

def count_whites(flies):
    pass # remove this line
    
## Question 3B
def map2(f, lst1, lst2):
    pass # remove this line

## Question 3C
def mapx(fn, *seq):
    pass # remove this line

## Question 3D
def cross_breed(grpA, grpB):
    pass # remove this line

## Question 3E
def cross_breed_age(males, females):
    pass # remove this line

## Provided for Question 4
class Creature:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name

    def breathe(self):
        print(self.name + " breathes")

class FlyingCreature(Creature):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(self.get_name() + " flutters")

class FireBreathingCreature(Creature):
    def __init__(self, name, charges):
        super().__init__(name)
        self.charges = charges

    def breathe(self):
        if self.charges > 0:
            print("Whoosh! Fire!")
            self.charges -= 1
        super().breathe()

    def recharge(self, amount):
        self.charges += amount

## Question 4A
"""
Answer here.
"""

## Question 4B
class Dragon: # add the superclass(es)
    pass # remove this line

## Question 4C
    def recharge(self, amount):
        pass # remove this line

## Question 4D
def create_dragon_factory(charges, species):
    pass # remove this line

## Test Cases
def compare(number,got,expected):
    if got == expected:
        print(f'Test {number} : Passed!')
    else:
        print(f'Test {number} : Failed!')
        print(f'Expected {expected}, got {got}')
    print()

# Pro tip : drag all the lines that you want to comment/uncomment and press Alt+3/4
def price(item): # only for the given test case(s)
    if item == '2A':
        return 20
    elif item == '2B':
        return 30

def test_q2a():
    print('Testing Question 2A...')
    print('='*20)
    compare('X',half_price('2A'),10)

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    compare(1,half_price_above_20('2A'),20)
    compare(2,half_price_above_20('2B'),15)

def test_q4b():
    print('Testing Question 4B...')
    print('='*20)
    try:
        toothless = Dragon("Toothless", 2, "Night Fury")
        toothless.breathe() # Whoosh! Fire!
                            # Toothless breathes
        print()
        toothless.fly()     # Toothless the Night Fury soars!
        print()
    except Exception as e:
        print(e)
        print('Error occured. Make sure all methods are well-defined.\n')

def test_q4c():
    print('Testing Question 4C...')
    print('='*20)
    try:
        toothless = Dragon("Toothless", 2, "Night Fury")
        toothless.breathe() # Whoosh! Fire!
                            # Toothless breathes
        print()
        toothless.recharge(5)
        toothless.breathe() # Whoosh! Fire!
                            # Toothless breathes
        print()
        toothless.breathe() # Whoosh! Fire!
                            # Toothless breathes
        print()
        toothless.breathe() # Toothless breathes
        print()
    except Exception as e:
        print(e)
        print('Error occured. Make sure all methods are well-defined.\n')

def test_q4d():
    print('Testing Question 4D...')
    print('='*20)
    try:
        GronkleFactory = create_dragon_factory(5, "Gronkle")
        meatlug = GronkleFactory("Meat Lug")
        seaslug = GronkleFactory("Sea Slug")

        meatlug.fly() # Meat Lug the Gronkle soars!
        seaslug.fly() # Sea Slug the Gronkle soars!
        print()
    except Exception as e:
        print(e)
        print('Error occured. Make sure all methods are well-defined.\n')

test_q2a()
test_q2b()
test_q4b()
test_q4c()
test_q4d()
