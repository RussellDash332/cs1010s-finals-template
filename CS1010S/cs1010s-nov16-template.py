#!/usr/bin/env python3
## CS1010S Nov16 Template

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
def cost_to_diff(stocks):
    pass # remove this line

## Question 2B
def longest_rise(stocks):
    pass # remove this line

## Question 2C
def days_increase(stocks):
    pass # remove this line

## Question 2D
"""
Answer here for both i) and ii).
"""

## Question 2E
def days_of(stocks, cond):
    pass # remove this line

## Question 2F
def max_profit(stock):
    pass # remove this line

## Question 3A
routes_lol = [('A', [('B', 5), ('C', 6), ('D', 4)]),
              ('B', [('A', 5), ('D', 2)]),
              ('C', [('D', 7), ('A', 6)]),
              ('D', [('C', 7), ('B', 2), ('A', 4)])]

routes_dod = {"A": {"B": 5, "C": 6, "D": 4},
              "B": {"A": 5, "D": 2},
              "C": {"A": 6, "D": 7},
              "D": {"A": 4, "B": 2, "C": 7}}

# Changed function name to prevent overlapping with question 3B
def cost_between_lol(routes, src, dest):
    pass # remove this line

# Time complexity :
    
## Question 3B
def cost_between_dod(routes, src, dest):
    pass # remove this line

# Time complexity :

## Question 3C
"""
Answer here.
"""

## Question 3D
def add_city(routes, new):
    pass # remove this line

## Question 3E
from random import *
def random_walk(routes, src, dest):
    pass # remove this line

## Question 3F
def greedy_walk(routes, src, dest):
    pass # remove this line

## Question 3G
"""
Answer here.
"""

## Provided for Question 4.
class Pokemon:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

class WaterPokemon(Pokemon):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed
        self.distance = 0
        
    def swim(self, time):
        self.distance += self.speed * time
        print(self.name + " swam " + str(self.distance) + " meters")

class FlyingPokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        
    def fly(self):
        print(self.name + " flies")

## Question 4A
"""
Answer here.
"""

## Question 4B
"""
Answer here.
"""

## Question 4C
class DragonPokemon: # add the superclasses in the correct order.
    pass # remove this line

## Test Cases
def compare(number,got,expected):
    if got == expected:
        print(f'Test {number} : Passed!')
    else:
        print(f'Test {number} : Failed!')
        print(f'Expected {expected}, got {got}')
    print()

# NoRouteException
class NoRouteException(Exception):
    def __str__(self):
        return 'NoRouteException!'

# Pro tip : drag all the lines that you want to comment/uncomment and press Alt+3/4

def test_q2a():
    print('Testing Question 2A...')
    print('='*20)
    compare('X',cost_to_diff([5, 10, 4, 6, 10, 12, 8, 8, 3, 5, 6]),[0, 5, -6, 2, 4, 2, -4, 0, -5, 2, 1])

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    compare('X',longest_rise([5, 10, 4, 6, 10, 12, 8, 8, 3, 5, 6]),3)

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    compare('X',days_increase([5, 10, 4, 6, 10, 12, 8, 8, 3, 5, 6]),6)

def test_q2f():
    print('Testing Question 2F...')
    print('='*20)
    compare('X',max_profit([5, 10, 4, 6, 10, 12, 8, 8, 3, 5, 6]),8)

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    compare(1,cost_between_lol(routes_lol,'A','B'),5)
    try:
        test = cost_between_lol(routes_lol,'C','B')
        print('Test 2 : Failed!\nExpected NoRouteException\n')
    except NoRouteException:
        print('Test 2 : Passed!\n')
    except:
        print('Test 2 : Failed!\nExpected NoRouteException\n')

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)
    compare(1,cost_between_dod(routes_dod,'A','B'),5)
    try:
        test = cost_between_dod(routes_dod,'C','B')
        print('Test 2 : Failed!\nExpected NoRouteException\n')
    except NoRouteException:
        print('Test 2 : Passed!\n')
    except:
        print('Test 2 : Failed!\nExpected NoRouteException\n')

def test_q3d():
    print('Testing Question 3D...')
    print('='*20)
    cost_between = cost_between_dod
    try:
        test = cost_between(routes_dod,'A','E')
        if test == 3:
            print('Test 1 : Please run test_q3d() exactly once here.\n')
        else:
            print('Test 1 : Failed!\nExpected NoRouteException\n')
    except NoRouteException:
        print('Test 1 : Passed!\n')
    except:
        print('Test 1 : Failed!\nExpected NoRouteException\n')
    add_city(routes_dod, ("E", (("A", 3), ("D", 8))))

    compare(2,cost_between(routes_dod,'A','E'),3)

def test_q3e():
    # I cannot handle the randomness here but can only ensure that the endpoints are correct
    print('Testing Question 3E...')
    print('='*20)
    def check(i, f, routes, src, dest):
        try:
            if f(routes,src,dest)[0]==src and f(routes,src,dest)[-1]==dest:
                compare(i, 0, 0)
            else:
                compare(i, f(routes,src,dest), 'an okay random route')
        except:
            compare(i, f(routes,src,dest), 'an okay random route')
            
    check(1, random_walk, routes_dod, 'A', 'C')
    check(2, random_walk, routes_dod, 'C', 'A')

def test_q3f():
    # The result will also handle presence of city E
    print('Testing Question 3F...')
    print('='*20)
    if 'E' not in routes_dod:
        compare('greedy walk',greedy_walk(routes_dod,'B','C'),['B','D','A','C'])
    else:
        try:
            compare('greedy walk',greedy_walk(routes_dod,'B','C'),['B','D','A','E'])
        except ValueError:
            print('Value Error occured, it is okay in this case.\n')
        except:
            expected = ['B','D','A','E']
            print(f'Test greedy walk : Failed!\nExpected ValueError or {expected}, depends on your code.\n')

def test_q4c():
    print('Testing Question 4C...')
    print('='*20)
    try:
        gyarados = DragonPokemon("Gyarados", 20, "blue")
        gyarados.breathe()  # Gyarados breathes a blue flame
        print()
        gyarados.fly()      # Gyarados flies
                            # Gyarados breathes a blue flame
        print()
    except:
        print('Failed! Please define all the methods properly.\n')

test_q2a()
test_q2b()
test_q2c()
test_q2f()
test_q3a()
test_q3b()
test_q3d()
test_q3e()
test_q3f()
test_q4c()
