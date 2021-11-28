## CS1010S Apr17 Template

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
def make_card(seq):
    pass # remove this line

## Question 2B
def cross_out(card, num):
    pass # remove this line

## Question 2C
def check_rows(card):
    pass # remove this line

def check_cols(card):
    pass # remove this line

## Question 2D
"""
Answer here.
"""

## Question 2E
def transpose(card):
    pass # remove this line

## Question 2F
from random import *
def draw_number(n):
    return randint(1, n)

class Drawer:
    pass # remove this line
    
## Question 3A
def make_empty_grid():
    return ({},{})
"""
Answer here.
"""

## Question 3B
"""
Answer here.
"""

## Question 3C
def add_ship(grid, ship, *coords):
    pass # remove this line

## Question 3D
def remove_ship(grid, name):
    pass # remove this line

## Question 3E
def is_sunk(ship):
    pass # remove this line

## Question 3F
def ships_left(grid):
    pass # remove this line

## Question 3G
def attack(grid, point):
    pass # remove this line

## Provided for Question 4
class Car:
    def __init__(self, weight):
        self.weight = weight
        
    def get_weight(self):
        return self.weight

class PassengerCar(Car):
    def __init__(self, weight):
        self.passengers = 0
        super().__init__(weight)
        
    def get_weight(self):
        return self.passengers * 100 + super().get_weight()

## Question 4A
"""
Answer here.
"""

## Question 4B
class Engine(Car):
    def __init__(self, power):
        self.power = power
        self.cars = []
        super().__init__(0)
        
    def add_car(self, car):
        self.cars.append(car)
        
    def get_weight(self):
        pass # remove this line
        
    def move(self):
        return self.power >= self.get_weight()

## Question 4C
class RailCar: # add the superclasses in the correct order.
    pass # remove this line

## Test Cases
def compare(number,got,expected):
    if got == expected:
        print(f'Test {number} : Passed!')
    else:
        print(f'Test {number} : Failed!')
        print(f'Expected {expected}, got {got}')
    print()

def print_card(card):
    try:
        for row in card:
            line = ''
            for number in row[:-1]:
                add = str(number)+','+(3-len(str(number)))*' '
                line += add
            line += str(row[-1])
            print(line)
    except Exception as e:
        print(e)
        print('Not a valid card!')

class SignalFault(Exception):
    def __str__(self):
        return 'SignalFault!'

# Pro tip : drag all the lines that you want to comment/uncomment and press Alt+3/4

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    card = make_card([[4, 10], [3, 11]])
    cross_out(card, 4)
    compare(1,card,[['X', 10], [3, 11]])
    compare(2,check_rows(card),False)

    cross_out(card, 10)
    compare(3,card,[['X', 'X'], [3, 11]])
    compare(4,check_rows(card),True)
    compare(5,check_cols(card),False)

    cross_out(card, 11)
    compare(6,card,[['X', 'X'], [3, 'X']])
    compare(7,check_cols(card),True)

def test_q2e():
    print('Testing Question 2E...')
    print('='*20)
    card = make_card([[3, 23, 39, 56, 64],
                      [2, 20, 35, 50, 72],
                      [14, 27, 41, 52, 70],
                      [8, 16, 45, 53, 61],
                      [7, 30, 36, 47, 71]])
    print_card(card)
    print()
    transpose(card)
    print_card(card)
    print()

    compare('transpose',card,[[3, 2, 14, 8, 7],
                              [23, 20, 27, 16, 30],
                              [39, 35, 41, 45, 36],
                              [56, 50, 52, 53, 47],
                              [64, 72, 70, 61, 71]])

def test_q2f():
    print('Testing Question 2F...')
    print('='*20)
    try:
        drawer = Drawer(75)
        print('drawer.draw() :',drawer.draw())
        print()
        for i in range(74):
            drawer.draw()
        compare('draw',drawer.draw(),0)
    except Exception as e:
        print(e)
        print('Please implement Drawer properly.\n')

def test_q3g():
    print('Testing Question 3G...')
    print('='*20)
    grid = make_empty_grid()
    add_ship(grid, "Destroyer", "F6", "F7")
    compare(1,attack(grid, "E5"),'Miss!')
    compare(2,attack(grid, "F6"),'Hit!')
    compare(3,attack(grid, "F6"),'Hit!')
    compare(4,attack(grid, "F7"),'Destroyer sunk')

def test_q4b():
    print('Testing Question 4B...')
    print('='*20)
    thomas = Engine(100000)
    compare(1,thomas.get_weight(),0)

    p1 = PassengerCar(25000)
    thomas.add_car(p1)
    compare(2,thomas.get_weight(),25000)

    p1.passengers = 100
    compare(3,thomas.get_weight(),35000)

def test_q4c():
    print('Testing Question 4C...')
    print('='*20)
    try:
        mrt = RailCar(50000)
        p2 = PassengerCar(15000)
        p3 = PassengerCar(15000)
        compare(1,mrt.get_weight(),0)

        mrt.add_car(p2)
        mrt.add_car(p3)
        compare(2,mrt.get_weight(),30000)

        mrt.passengers = 50
        p2.passengers = 60
        p3.passengers = 70

        compare(3,mrt.get_weight(),48000)
        compare(4,mrt.move(),True)

        mrt.passengers = 100
        compare(5,mrt.get_weight(),53000)
        try:
            res = mrt.move()
            print(f'Test 6 : Failed!\nExpected SignalFault, got {res}\n')
        except SignalFault:
            print('Test 6 : Passed!\n')
        except:
            print(f'Test 6 : Failed!\nExpected SignalFault\n')
    except Exception as e:
        print(e)
        print('Failed! Please implement RailCar properly.')
        
    
test_q2c()
test_q2e()
test_q2f()
test_q3g()
test_q4b()
test_q4c()
