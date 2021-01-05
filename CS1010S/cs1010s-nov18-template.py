#!/usr/bin/env python3
## CS1010S Nov18 Template

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
def grow_bool(field): # renamed function to prevent overlapping
    pass # remove this line

# Modify for questions 2BDE if necessary.
def grow(field):
    new = []
    for plot in field:              # Changes suggested in part E
        if plot-1 not in new:       # new[-1] < plot-1
            new.append(plot-1)
        elif plot not in new:       # new[-1] < plot
            new.append(plot)
        elif plot+1 not in new:     # new[-1] < plot+1
            new.append(plot+1)
    field = new

## Question 2B
"""
Answer here.
"""

## Question 2C
"""
Answer here.
"""

## Question 2D
"""
Answer here.
"""

## Question 2E
"""
Answer here.
"""

## Question 2F
def kill(field, plots):
    pass # remove this line

## Question 3A
"""
Answer here.
"""

display = {'0': 'abcdef', '1': 'bc', '2': 'abged', '3': 'abdcg',
           '4': 'fgbc','5':'afgcd','6':'afgecd','7':'abc',
           '8':'abcdefg','9':'abcdfg'}

## Question 3B
def inverse(display):
    pass # remove this line

## Question 3C
def character(state, mapping):
    pass # remove this line

## Question 3D
"""
Answer here.
"""

## Question 3E
def guess(state, mapping):
    pass # remove this line

## Question 3F
def better_guess(state,mapping,damaged):
    pass # remove this line

## Provided for Question 4
class Vehicle:
    def __init__(self, name, mpg):
        self.name = name
        self.mpg = mpg
        self.fuel = 16

    def fuel_used(self, mile):
        return mile/self.mpg

    def refuel(self, fuel):
        self.fuel += fuel

    def drive(self, mile):
        fuel_used = self.fuel_used(mile)
        if fuel_used > self.fuel:
            print("Not enough fuel")
            return False
        else:
            self.fuel -= fuel_used
            print("Used " + str(fuel_used) + " gallon of fuel")
            return True

class Car(Vehicle):
    def __init__(self, name, mpg):
        super().__init__(name, mpg)
        self.passengers = 0

    def board(self, passengers):
        self.passengers += passengers

    def alight(self, passengers):
        self.passengers -= passengers
        
    def fuel_used(self, mile):
        return super().fuel_used(mile) + self.passengers*0.1*mile

## Question 4A
"""
Answer here.
"""

## Question 4B
class Truck: # add the superclass(es) if necessary
    pass # remove this line

## Question 4C
class Pickup_Truck(Car, Truck):
    pass
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

def test_q2a():
    print('Testing Question 2A...')
    print('='*20)
    field = [False, False, True, False, False, False, False, True, False, False]
    grow_bool(field)
    compare(1,field,[False, True, True, True, False, False, True, True, True, False])
    grow_bool(field)
    compare(2,field,[True]*len(field))

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)
    inversed = inverse(display)
    try:
        compare('inverse',inversed['a'],'02356789')
    except Exception as e:
        print(e)
        print('Please define inverse(display) properly.\n')

def test_q3e():
    print('Testing Question 3E...')
    print('='*20)
    compare('guess',guess('adg',display),list('235689'))

def test_q3f():
    print('Testing Question 3F...')
    print('='*20)
    compare('better guess',better_guess('adeg',display,'bf'),['2'])

def test_q4b():
    print('Testing Question 4B...')
    print('='*20)
    try:
        truck = Truck("Might-E", 25)
        compare(1,truck.drive(100),True)
        compare(2,truck.fuel_used(100),4.0)

        truck.load(600)
        compare(3,truck.drive(100),True)
        compare(4,truck.fuel_used(100),6.4)

        compare(5,truck.drive(100),False)

        truck.unload(200)
        compare(6,truck.drive(100),True)
        compare(7,truck.fuel_used(100),5.6)
    except Exception as e:
        print(e)
        print('Error! Please define all methods properly.\n')

test_q2a()  
test_q3b()
test_q3e()
test_q3f()
test_q4b()
