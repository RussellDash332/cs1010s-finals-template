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

# My own fly ADT, do not modify.
fly_hive = []
bee_hive = []

def make_fly(name,male,colour,age):
    fly = [name,male,colour,age]
    if fly not in fly_hive:
        fly_hive.append(fly)
    if fly not in bee_hive and colour == 'yellow':
        bee_hive.append(fly)
    return fly

def is_male(fly):
    return fly[1]

def eye_colour(fly):
    return fly[2]

def age(fly):
    return fly[3]

class Tagger:
    def __init__(self):
        self.tag = 0

    def produce(self):
        self.tag += 1
        return str(self.tag)

    def reset(self):
        self.tag = 0

tagger = Tagger()

def breed(fly1, fly2):
    tag_number = int(tagger.produce())
    if tag_number % 6 == 0:
        return ['Child '+str(tag_number),True,'yellow',0]
    elif tag_number % 3 == 0:
        return ['Child '+str(tag_number),False,'black',0]
    elif tag_number % 2 == 0:
        return ['Child '+str(tag_number),True,'white',0]
    else:
        return ['Child '+str(tag_number),False,'white',0]

king_fly = make_fly('King',True,'white',100)
queen_fly = make_fly('Queen',False,'white',90)
fruit_fly = make_fly('Fruit',True,'red',80)
russells_pet = make_fly('Fly',True,'white',70)
zombie_fly = make_fly('Dead',False,'white',60)
bee = make_fly('Impostor #1',True,'yellow',50)
queen_bee = make_fly('Queen B',False,'yellow',40)
king_bee = make_fly('King B',True,'yellow',30)
sus_fly = make_fly('Impostor #2',True,'white',10)

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

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    compare(1,count_males(fly_hive),6)
    compare(2,count_whites(fly_hive),5)
    compare(3,count_males(bee_hive),2)
    compare(4,count_whites(bee_hive),0)

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)
    add = lambda x,y:x+y
    multiply = lambda x,y:x*y
    lst1 = [1,2,3,4,5]
    lst2 = [5,4,3,2,1]
    compare(1,map2(add,lst1,lst2),[6]*5)
    compare(2,map2(add,lst1,lst1),[2,4,6,8,10])
    compare(3,map2(multiply,lst1,lst2),[5,8,9,8,5])

def test_q3c():
    print('Testing Question 3C...')
    print('='*20)
    add = lambda x,y:x+y
    multiply = lambda x,y:x*y
    lst1 = [1,2,3,4,5,6]
    lst2 = [5,4,3,2,1,0,9,8,7,6]
    compare(1,mapx(add,lst1,lst2),[6]*6)
    compare(2,mapx(add,lst1,lst1),[2,4,6,8,10,12])
    compare(3,mapx(multiply,lst1,lst2),[5,8,9,8,5,0])
    compare(4,mapx(multiply,lst1,lst2[::-1]),[6,14,24,36,0,6])

def test_q3de():
    print('Testing Question 3DE...')
    print('='*20)
    tagger.reset()
    mid = len(fly_hive)//2
    east_flies = fly_hive[:mid]
    west_flies = fly_hive[mid:]
    result1 = cross_breed(east_flies,west_flies)
    compare('cross breed',result1,[['Child 1', False, 'white', 0],
                                   ['Child 2', True, 'white', 0],
                                   ['Child 3', False, 'black', 0]])
    tagger.reset()
    
    males = list(filter(is_male,fly_hive))
    females = list(filter(lambda x: not is_male(x),fly_hive))
    result2 = cross_breed_age(males,females)
    compare('cross breed age',result2,{95.0: [['Child 1', False, 'white', 0]],
                                       70.0: [['Child 2', True, 'white', 0]],
                                       55.0: [['Child 3', False, 'black', 0]]})
    tagger.reset()

    dummy_hive = []
    def make_dummy_fly(male,age):
        fly = ['Dummy '+str(len(dummy_hive)+1),male,'rainbow',age]
        if fly not in dummy_hive:
            dummy_hive.append(fly)
        return fly

    # male flies
    dummy1 = make_dummy_fly(True,100)
    dummy2 = make_dummy_fly(True,90)
    dummy3 = make_dummy_fly(True,80)
    dummy4 = make_dummy_fly(True,80)
    dummy5 = make_dummy_fly(True,10)
    dummy6 = make_dummy_fly(True,10)
    dummy7 = make_dummy_fly(True,5)

    # female flies
    dummy8 = make_dummy_fly(False,60)
    dummy9 = make_dummy_fly(False,50)
    dummy10 = make_dummy_fly(False,40)
    dummy11 = make_dummy_fly(False,40)
    dummy12 = make_dummy_fly(False,30)
    dummy13 = make_dummy_fly(False,30)

    males2 = list(filter(is_male,dummy_hive))
    females2 = list(filter(lambda x: not is_male(x),dummy_hive))
    result3 = cross_breed_age(males2,females2)
    compare('cross breed age again',result3,{80.0: [['Child 1', False, 'white', 0]],
                                             70.0: [['Child 2', True, 'white', 0]],
                                             60.0: [['Child 3', False, 'black', 0],
                                                    ['Child 4', True, 'white', 0]],
                                             20.0: [['Child 5', False, 'white', 0],
                                                    ['Child 6', True, 'yellow', 0]]})
    tagger.reset()
    
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
test_q3a()
test_q3b()
test_q3c()
test_q3de()
test_q4b()
test_q4c()
test_q4d()
