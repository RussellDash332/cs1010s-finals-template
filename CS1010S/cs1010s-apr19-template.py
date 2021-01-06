#!/usr/bin/env python3
## CS1010S Apr19 Template

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
Answer here.
"""

## Question 2B
def step1(tetromino):
    pass # remove this line

## Question 2C
def step2(tetromino):
    pass # remove this line

## Question 2D
s = [(0,1), (1,0), (1,1), (2,0)]
t = s.copy()
step1(s)
step2(s)
"""
Draw or do something else with this part.
"""

## Question 2E
def compose(f, g):
    return lambda x: f(g(x))
rotate = compose(step1, step2)
"""
Answer here.
"""

## Question 2F
figure_a = [[False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [True, False, False, False, False, False],
            [True, False, False, False, True, False],
            [True, False, False, False, True, False],
            [True, True, True, False, True, True],
            [True, True, True, False, True, True]]

def can_place(tetromino, grid, row, col):
    pass # remove this line

## Question 2G
def drop(tetromino, grid, col):
    pass # remove this line

## For Question 3
parents = {'Brenda': 'Aaron', 'Claire': 'Brenda', 'David': 'Brenda',
'Elis': 'Claire', 'Freddy': 'Claire', 'Gerene': 'David'}

## Question 3A
def is_descendent_parents(parents, a, d): # renamed function to prevent overlapping
    pass # remove this line
    
## Question 3B
def convert(parents):
    pass # remove this line

childrens = convert(parents)

## Question 3C
def is_descendent(childrens, a, d):
    pass # remove this line

## Question 3D
"""
Answer here.
"""

## Provided for Question 4, especially Question 4C
class StorageDevice:
    def __init__(self, memory, *args):
        super().__init__(*args)
        self.memory = memory
        self.used = 0
        self.items = [] # items stored in memory

    def available_storage(self):
        return self.memory - self.used - len(self.items)

class PhoneDevice:
    def __init__(self, number, *args):
        super().__init__(*args)
        self.number = number

    def call(self, number):
        print('Calling number', number)

    def receive(self):
        print('Receiving Call...')
        
class MusicPlayer(StorageDevice):
    def __init__(self, memory):
        super().__init__(memory)

    def play_song(self, song):
        if song in self.items:
            print("Playing " + song)
        else:
            print(song + " not found")

class IPod(MusicPlayer):
    def __init__(self, memory):
        super().__init__(memory)

    def backup_songs(self):
        print("Connect to iTunes to back up songs")

## Question 4A
"""
Answer here.
"""

## Question 4B
# PSA : store_music is a typo. It should be store_song according to the sample execution.
"""
Answer here.
"""

## Question 4C
# Modify the code above.

## Question 4D
class IPhone: # add the superclasses in the correct order.
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

def test_q2bc():
    print('Testing Question 2BC...')
    print('='*20)
    s = [(0,1), (1,0), (1,1), (2,0)]
    step1(s)
    compare(1,sorted(s),sorted([(-1,0),(-1,1),(0,1),(0,2)]))
    step2(s)
    compare(2,sorted(s),sorted([(0,0),(0,1),(1,1),(1,2)]))

def test_q2fg():
    print('Testing Question 2FG...')
    print('='*20)
    s = [(0,1), (1,0), (1,1), (2,0)]
    step1(s)
    step2(s)
    compare(1,can_place(s,figure_a,4,2),False)
    compare(2,can_place(s,figure_a,3,2),True)
    compare(3,can_place(s,figure_a,0,2),True)
    figure_c = [[False, False, False, False, False, False],
                [False, False, False, False, False, False],
                [True, False, False, False, False, False],
                [True, False, True, False, True, False],
                [True, False, True, True, True, False],
                [True, True, True, True, True, True],
                [True, True, True, False, True, True]]

    figure_d = [[False, False, False, False, False, False],
                [False, False, True, False, False, False],
                [True, False, True, True, False, False],
                [True, False, True, True, True, False],
                [True, False, True, True, True, False],
                [True, True, True, True, True, True],
                [True, True, True, False, True, True]]

    compare(4,drop(s,figure_a,2),True)
    compare(5,figure_a,figure_c)
    compare(6,drop(s,figure_a,2),True)
    compare(7,figure_a,figure_d)
    compare(8,drop(s,figure_a,2),False)
    compare(9,figure_a,figure_d)
    compare(10,drop(s,figure_c,2),True)
    compare(11,figure_c,figure_d)

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    compare(1,is_descendent_parents(parents, 'Aaron', 'Elis'),True)
    compare(2,is_descendent_parents(parents, 'Claire', 'Gerene'),False)

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)
    compare('childrens',childrens,{'Aaron': ['Brenda'], 'Brenda': ['Claire', 'David'],
                                   'Claire': ['Elis', 'Freddy'], 'David': ['Gerene'],
                                   'Elis': [], 'Freddy': [], 'Gerene': []})

def test_q3c():
    print('Testing Question 3C...')
    print('='*20)
    compare(1,is_descendent(childrens, 'Aaron', 'Elis'),True)
    compare(2,is_descendent(childrens, 'Claire', 'Gerene'),False)

def test_q4a():
    print('Testing Question 4A...')
    print('='*20)
    ipod = IPod(32)
    print(ipod.available_storage)
    print()
    ipod.play_song("Somewhere Out There")
    print()
    try:
        ipod.call(65169121)
        print()
    except Exception as e:
        print(e)
        print()

def test_q4c():
    print('Testing Question 4C...')
    print('='*20)
    try:
        ipod = IPod(32)
        ipod.store_song("Our Song", 14)         # Our Song stored
        print()                                 # 17 memory left
        
        ipod.store_song("Never Say Never", 10)  # Never Say Never stored
        print()                                 # 6 memory left
        
        ipod.play_song("Our Song")              # Playing Our Song
        print()
        
        ipod.store_song("Never Enough", 6)      # Not enough memory
        print()
        
        ipod.play_song("Never Enough")          # Never Enough not found
        print()
    except Exception as e:
        print(e)
        print('Please define store_song first (store_music in PDF).\n')

def test_q4d():
    print('Testing Question 4D...')
    print('='*20)
    try:
        iphone = IPhone(256)
        iphone.call(98765432)                           # Calling number 98765432
        print()
        iphone.play_song('Sha La La')                   # Sha La La not found

        print()
        iphone.search("How to program with Python?")    # Searching How to program with Python?
        print()
        try:
            iphone.backup_songs()
            print()
        except Exception as e:
            print(e)                                    # AttributeError: 'IPhone' object has no attribute 'backup_songs'
            print()
    except Exception as e:
        print(e)
        print('Please implement IPhone properly first.\n')
    
test_q2bc()
test_q2fg()
test_q3a()
test_q3b()
test_q3c()
test_q4a()
test_q4c()
test_q4d()
