#!/usr/bin/env python3
## CS1010S Apr21 Template
import random

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


## Provided for Question 2
blockchain = [
    ["Ben", "2021-02-28", "815"], ["Kenghwee", "2021-04-01", "1456"],
    ["Waikay", "2021-04-17", "1313"], ["Jon", "2021-04-29", "989"]
]

## Question 2A
def hash(string):
    pass # remove this line

## Question 2B
def get_names(blockchain, date):
    pass # remove this line

## Question 2C
def add_block(name, date, blockchain):
    pass # remove this line

## Question 2D
def is_valid(blockchain):
    pass # remove this line

## Question 2E
def date_vaccinated(name, blockchain):
    pass # remove this line

## Question 2F
"""
Is it safe? Answer here.
"""


## Provided for Question 3
bag = [
    [],
    ['K', 'J', 'X', 'Q', 'Z',],
    [' ', 'F', 'H', 'V', 'W', 'Y', 'B', 'C', 'M', 'P'],
    ['G'],
    ['D', 'L', 'S', 'U'],
    [],
    ['N', 'R', 'T'],
    [],
    ['O'],
    ['A', 'I'],
    [],
    [],
    ['E']
]

## Question 3A
def total_tiles(bag):
    pass # remove this line
    
## Question 3B
def remove(char, bag):
    pass # remove this line

## Question 3C
def to_dict(bag):
    pass # remove this line

## Question 3D
def to_list(bag):
    pass # remove this line

## Question 3E
def combine(a,b):
    pass # remove this line

## Provided, do not modify!
def choice(seq):
    return random.choice(list(seq))

## Question 3F
def new_game(bag):
    pass # remove this line


## Provided for Question 4, no need to modify.
class Pony:
    def __init__(self, energy):
        self.energy = energy

    def consume(self):
        self.energy = max(0, self.energy - 10)

    def move(self):
        if self.energy == 0:
            print("Need to rest")
        else:
            print("Let's go!")
            self.consume()

class Pegasus(Pony):
    def fly(self):
        self.flying = True

    def land(self):
        self.flying = False

    def consume(self):
        super().consume()
        if (self.flying):
            super().consume()


## Question 4A
"""
Answer here.
"""

## Question 4B
class Unicorn: # add the superclass(es) if necessary.
    pass # remove this line

## Question 4C
class Alicorn(Pegasus, Unicorn): # or (Unicorn, Pegasus)?
    pass

"""
Explain in detail if Twilight Sparkle’s idea is correct, and whether the order of the super classes matter.
You can list some sample execution to aid your explanation.
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
    compare(1,hash("Dd"),"168")
    compare(2,hash("dec"),"300")
    compare(3,hash("Ben"),"277")
    compare(4,hash("CS1010S"),"427")
    compare(5,hash("Waikay"),"614")
    compare(6,hash("Wayaki"),"614")

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    compare(1,get_names(blockchain, "2021-04-01"), ["Ben", "Kenghwee"])
    compare(2,get_names(blockchain, "2021-04-18"), ["Ben", "Kenghwee", "Waikay"])
    compare(3,get_names(blockchain, "2021-04-19"), ["Ben", "Kenghwee", "Waikay"])
    compare(4,get_names(blockchain, "2021-04-28"), ["Ben", "Kenghwee", "Waikay"])
    compare(5,get_names(blockchain, "2021-04-29"), ["Ben", "Kenghwee", "Waikay", "Jon"])
    compare(6,get_names(blockchain, "2021-04-29"), ["Ben", "Kenghwee", "Waikay", "Jon"])

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    dummy_blockchain = [
        ["Ben", "2021-02-28", "815"], ["Kenghwee", "2021-04-01", "1456"],
        ["Waikay", "2021-04-17", "1313"], ["Jon", "2021-04-29", "989"]
    ]
    add_block("Eshin", "2021-04-29", dummy_blockchain)
    compare(1,dummy_blockchain,[["Ben", "2021-02-28", "815"], ["Kenghwee", "2021-04-01", "1456"], ["Waikay", "2021-04-17", "1313"], ["Jon", "2021-04-29", "989"], ["Eshin", "2021-04-29", "1167"]])
    add_block("Wayaki", "2021-04-27", dummy_blockchain)
    compare(2,dummy_blockchain,[["Ben", "2021-02-28", "815"], ["Kenghwee", "2021-04-01", "1456"], ["Waikay", "2021-04-17", "1313"], ["Jon", "2021-04-29", "989"], ["Eshin", "2021-04-29", "1167"], ["Wayaki", "2021-04-27", "1313"]])

    another_dummy_blockchain = [
        ["Ben", "2021-02-28", "815"], ["Kenghwee", "2021-04-01", "1456"],
        ["Waikay", "2021-04-17", "1313"], ["Jon", "2021-04-29", "989"]
    ]
    add_block("Eshin", "2021-04-29", another_dummy_blockchain)
    add_block("Wayaki", "2021-04-30", another_dummy_blockchain)
    compare(3,another_dummy_blockchain,[["Ben", "2021-02-28", "815"], ["Kenghwee", "2021-04-01", "1456"], ["Waikay", "2021-04-17", "1313"], ["Jon", "2021-04-29", "989"], ["Eshin", "2021-04-29", "1167"], ["Wayaki", "2021-04-30", "1307"]])

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)
    dummy_blockchain = [["Ben", "2021-02-28", "768"], ["Eshin", "2021-04-29", "1162"], ["Wayaki", "2021-04-27", "1308"]]
    broken_blockchain = [["Ben", "2021-02-28", "815"], ["Kenghwee", "2021-04-01", "1456"], ["Waikay", "2021-04-17", "1313"], ["Jon", "2021-04-29", "988"], ["Eshin", "2021-04-29", "1167"], ["Wayaki", "2021-04-27", "1313"]]
    another_blockchain = [["Ben", "2021-02-28", "768"], ["Eshin", "2021-04-29", "1162"], ["Wayaki", "2021-04-27", "1308"]]
    
    compare(1,is_valid(blockchain),False)
    compare(2,is_valid(dummy_blockchain),True)
    compare(3,is_valid(broken_blockchain),False)
    compare(4,is_valid(another_blockchain),True)
    
    # Adding another block should retain the validity of a blockchain
    add_block("Neb", "2021-05-01", dummy_blockchain)
    compare(5,is_valid(another_blockchain),True)

def test_q2e():
    print('Testing Question 2E...')
    print('='*20)
    valid_blockchain = [["Ben", "2021-02-28", "768"], ["Eshin", "2021-04-29", "1162"], ["Wayaki", "2021-04-27", "1308"]]

    # Invalid blockchain
    compare(1,date_vaccinated("Ben",blockchain),None)
    compare(2,date_vaccinated("Waikay",blockchain),None)
    compare(3,date_vaccinated("Hengkwee",blockchain),None)
    compare(4,date_vaccinated("Wayaki",blockchain),None)

    # Valid blockchain
    compare(5,date_vaccinated("Ben",valid_blockchain),"2021-02-28")
    compare(6,date_vaccinated("Wayaki",valid_blockchain),"2021-04-27")
    compare(7,date_vaccinated("Waikay",valid_blockchain),None)
    compare(8,date_vaccinated("Eshin",valid_blockchain),"2021-04-29")

def test_q3ab():
    print('Testing Question 3AB...')
    print('='*20)
    local_bag = [
        [],
        ['K', 'J', 'X', 'Q', 'Z',],
        [' ', 'F', 'H', 'V', 'W', 'Y', 'B', 'C', 'M', 'P'],
        ['G'],
        ['D', 'L', 'S', 'U'],
        [],
        ['N', 'R', 'T'],
        [],
        ['O'],
        ['A', 'I'],
        [],
        [],
        ['E']
    ]
    compare(1,total_tiles(local_bag),100)
    compare(2,remove('G',local_bag),True)
    compare(3,total_tiles(local_bag),99)
    compare(4,remove('K',local_bag),True)
    compare(5,total_tiles(local_bag),98)
    compare(6,remove('K',local_bag),False)
    compare(7,total_tiles(local_bag),98)
    compare(8,local_bag,[
        ['K'],
        ['J', 'X', 'Q', 'Z',],
        [' ', 'F', 'H', 'V', 'W', 'Y', 'B', 'C', 'M', 'P', 'G'],
        [],
        ['D', 'L', 'S', 'U'],
        [],
        ['N', 'R', 'T'],
        [],
        ['O'],
        ['A', 'I'],
        [],
        [],
        ['E']
    ])

    
def test_q3cd():
    print('Testing Question 3CD...')
    print('='*20)
    compare(1,to_dict(bag),{' ': 2, 'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1})
    local_bag = [
        [],
        ['K', 'J', 'X', 'Q', 'Z',],
        [' ', 'F', 'H', 'V', 'W', 'Y', 'B', 'C', 'M', 'P'],
        ['G'],
        ['D', 'L', 'S', 'U'],
        [],
        ['N', 'R', 'T'],
        [],
        ['O'],
        ['A', 'I'],
        [],
        [],
        ['E']
    ]
    remove('B',local_bag)
    remove('E',local_bag)
    remove('N',local_bag)
    remove('J',local_bag)
    remove('K',local_bag)
    compare(2,to_dict(local_bag),{' ': 2, 'A': 9, 'B': 1, 'C': 2, 'D': 4, 'E': 11, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 0, 'K': 0, 'L': 4, 'M': 2, 'N': 5, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1})
    remove('C',local_bag)
    remove('S',local_bag)
    remove('S',local_bag)
    remove('S',local_bag)
    remove('S',local_bag)
    remove('S',local_bag)
    remove('S',local_bag)
    remove('S',local_bag)
    compare(3,to_dict(local_bag),{' ': 2, 'A': 9, 'B': 1, 'C': 1, 'D': 4, 'E': 11, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 0, 'K': 0, 'L': 4, 'M': 2, 'N': 5, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 0, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1})

    compare(4,to_list(to_dict(bag)),bag)
    compare(5,to_list(to_dict(local_bag))+[[]],local_bag)

def test_q3e():
    print('Testing Question 3E...')
    print('='*20)

    # Both bags are guaranteed to have the same set of tiles
    mini_bag1 = [[],['A','B'],['C'],['D','E']]
    mini_bag2 = [[],['A'],['B'],['C','E','D']]
    try:
        compare("combine",list(map(sorted,combine(mini_bag1,mini_bag2))),[[],[],['A'],['B'],[],['C'],['D','E']])
    except:
        compare("combine",None,[[],[],['A'],['B'],[],['C'],['D','E']])

def test_q3f():
    print('Testing Question 3F...')
    print('='*20)
    game = new_game(bag)

    try:
        for i in range(100):
            m = game()
            if m == False:
                print("Wrong! Game not ended yet!\n")
                break
        compare(1,game(),False)
        try:
            compare(2,total_tiles(bag),100)
        except:
            print("Please do question 3A and run test_q3a()!\n")
    except:
        print("Please implement the new_game function correctly!\n")

def test_q4b():
    print('Testing Question 4B...')
    print('='*20)
    try:
        rarity = Unicorn(10)
        rarity.move() # Let's go!
        rarity.consume()
        rarity.consume()
        compare("energy",rarity.energy,10)
        rarity.move() # Let's go!
        rarity.move() # Need to rest
    except:
        print("Please implement Unicorn properly!\n")

test_q2a()
test_q2b()
test_q2c()
test_q2d()
test_q2e()
test_q3ab()
test_q3cd()
test_q3e()
test_q3f()
test_q4b()
