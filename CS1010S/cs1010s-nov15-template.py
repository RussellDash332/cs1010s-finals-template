#!/usr/bin/env python3
## CS1010S Nov15 Template

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
def find_oldest(players):
    pass # remove this line

## Question 2B
def avg_age(players):
    pass # remove this line

## Question 2C
def average(seq, key):
    pass # remove this line

## Question 2D
def bmi(height, weight):
    pass # remove this line

def avg_bmi(players):
    pass # remove this line

## Question 3A
"""
Answer here.
"""

# My own lazy version of the pre-made functions. Dp not modify :)
class Vote:
    def __init__(self, string):
        self.vote = string
    
def make_vote(string):
    return Vote(string)

def read_vote(vote):
    return vote.vote

def is_vote(obj):
    return isinstance(obj,Vote)

## Question 3B
def create_box(candidates):
    pass # remove this line

def get_candidates(box):
    pass # remove this line

def show_votes(box):
    pass # remove this line

def cast_vote(box, vote):
    pass # remove this line

## Question 3C
def check_vote(box, vote):
    pass # remove this line

## Question 3D
def transfer_votes(box1, *boxes):
    pass # remove this line

## Question 3E
def count_votes(box):
    pass # remove this line

# Provided for Question 4, modify if necessary
class Food:
    def __init__(self, name):
        self.name = name
        self.eaten = False

class Minion(Food):
    def __init__(self, name, num_eyes):
        self.name = name
        self.num_eyes = num_eyes

    def get_name(self):
        return self.name

    def eat(self, food):
        if not food.eaten:
            print(self.name + " eats " + food.name)
            food.eaten = True
        else:
            print(food.name + " is already eaten!")
            self.say("Matoka!")

    def say(self, words):
        print(self.name + " says '" + words + "'")
    
## Question 4A
"""
Answer here and modify the code above if necessary.
"""

## Question 4B
"""
Answer here and modify the code above if necessary.
"""

## Question 4C
class OneEyeMinion(Minion):
    pass # remove this line

class TwoEyeMinion(Minion):
    pass # remove this line

## Question 4D
"""
Answer here.
"""
def mutate(minion):
    pass # remove this line

def cure(minion):
    pass # remove this line

## Question 4E
class YellowMinion(Minion):
    def __init__(self, name, num_eyes):
        super.__init__(name, num_eyes)
        self.color = 'yellow'

class PurpleMinion(Minion):
    def __init__(self, name, num_eyes):
        super.__init__(name, num_eyes)
        self.color = 'purple'

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

box1 = create_box(('Lion', 'Mouse'))
box2 = create_box(('Lion', 'Mouse'))
box3 = create_box(('Lion', 'Bear'))

def test_q3():
    print('Testing Question 3...')
    print('='*20)
    cast_vote(box1, make_vote('Lion'))
    cast_vote(box1, make_vote('Mouse'))
    cast_vote(box2, make_vote('Cat'))
    cast_vote(box2, make_vote('Mouse'))
    compare(1,get_candidates(box1),('Lion', 'Mouse'))
    compare(2,show_votes(box1),('Lion', 'Mouse'))
    compare(3,show_votes(box2),('Cat', 'Mouse'))

    my_vote = make_vote('Lion')
    cast_vote(box2, my_vote)
    compare(4,show_votes(box2),('Cat', 'Mouse', 'Lion'))
    compare(5,show_votes(box1),('Lion', 'Mouse'))

    compare(6,check_vote(box1, my_vote),False)
    compare(7,check_vote(box2, my_vote),True)

    cast_vote(box3, make_vote('Bear'))
    cast_vote(box3, make_vote('Lion'))
    transfer_votes(box1, box2, box2, box3)

    # ('Cat', 'Mouse', 'Lion', 'Lion', 'Mouse') in PDF
    compare(8,show_votes(box1),('Lion', 'Mouse','Cat', 'Mouse', 'Lion'))
    compare(9,show_votes(box2),())
    compare(10,show_votes(box3),('Bear', 'Lion'))

    compare(11,count_votes(box1),{'Mouse': 2, 'Lion': 2, 'Spoilt': 1})
    
test_q3()
