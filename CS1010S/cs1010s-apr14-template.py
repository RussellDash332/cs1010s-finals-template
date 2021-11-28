## CS1010S Apr14 Template

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
def check_charges(seq):
    pass # remove this line

## Question 2B
def charge_5(seq):
    pass # remove this line

## Question 2C
def find_bad_items(seq):
    pass # remove this line

## Question 2D
def update_inventory(seq):
    pass # remove this line

## Question 2E
"""
(do not uncomment)
<T1> :
"""

## Question 3A
def sort_magical_items(box):
    pass # remove this line

# The magical item ADT
def make_magical_item(id, charges):
    return (id, charges)

def get_identity(item):
    return item[0]

def get_charges(item):
    return item[1]

# The inventory_list ADT
# An inventory_list consists of the name of the magical item
# collection (i.e., ‘wands’, ‘spells’, or ‘potions’) and a list of
# magical_items (i.e., the individual wands, spells, or potions)
def make_inventory_list(iname, items):
    return [iname, items]

def get_inventory_name(inv):
    return inv[0]

def get_inventory_items(inv):
    return inv[1]

# All items are "collected" into an inventory_list, so the user does
# not need to know how the inventory list is actually implemented

def collect(items):
    return list(items)

# The magic_box ADT
# A magic_box consists of several inventory_lists
def make_magic_box():
    return {}

def all_inventory_lists(box):
    return list(box.items())

## Question 3B
def add_inventory_item(inv, item):
    pass # remove this line

def remove_inventory_item(inv, item):
    pass # remove this line

## Question 3C
def add_inventory_list(box,inv):
    iname = get_inventory_name(inv)
    items = get_inventory_items(inv)
    # <T2>

## Question 3D
def sort_magical_items2(box):
    pass # remove this line

class Robot:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

class PlayRobot(Robot):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self.fun_factor = 0

    def play(self, time):
        self.fun_factor += time
        print("New fun factor: " + str(self.fun_factor))

class StudyRobot(Robot):
    def __init__(self, name):
        super().__init__(name)
        self.skills = 0

    def teach(self, time):
        self.skills += time
        print("New skills level:" + str(self.skills))

## Question 4A
"""
Answer here.
"""

## Question 4B
class BuddyRobot(PlayRobot, StudyRobot):
    pass # remove this line

## Question 4C
    def teach(): # add the parameter(s)
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

wands = [(1, 1), (2, 2), (3, 3), (4, -1), (5, 5)]
potions = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 5), (6, 6), (7, 7), (8, 8)]
spells = [(1, 5), (2, -1), (3, 5), (4, 0), (5, -1)]

m_box = {'wands': [(1, 1), (2, 2), (3, 3), (4, -1), (5, 5)],
         'potions': [(1, 1), (2, 1), (3, 1), (4, 1), (5, 5), \
                     (6, 6), (7, 7), (8, 8)],
         'spells': [(1, 5), (2, -1), (3, 5), (4, 0), (5, -1)]}


def test_q2a():
    print('Testing Question 2A...')
    print('='*20)
    compare('X',check_charges(spells),[5, -1, 5, 0, -1])

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    compare('X',charge_5(wands),[6, 2, 3, 4, 5])

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    compare('X',find_bad_items(spells),[(2, -1), (5, -1)])

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    sort_magical_items(m_box)
    compare('sort',m_box,{'wands': [(5, 5), (3, 3), (2, 2), (1, 1), (4, -1)],
                          'spells': [(1, 5), (3, 5), (4, 0), (2, -1), (5, -1)],
                          'potions':[(8, 8), (7, 7), (6, 6), (5, 5),
                                     (1, 1), (2, 1), (3, 1), (4, 1)]})

def test_q3d():
    print('Testing Question 3D...')
    print('='*20)
    another_m_box = {'wands': [(1, 1), (2, 2), (3, 3), (4, -1), (5, 5)],
                     'potions': [(1, 1), (2, 1), (3, 1), (4, 1), (5, 5), \
                                 (6, 6), (7, 7), (8, 8)],
                     'spells': [(1, 5), (2, -1), (3, 5), (4, 0), (5, -1)]}

    new_box = sort_magical_items2(another_m_box)
    compare('the original box',another_m_box,{'wands': [(1, 1), (2, 2), (3, 3), (4, -1), (5, 5)],
                                              'potions': [(1, 1), (2, 1), (3, 1), (4, 1), (5, 5), \
                                                          (6, 6), (7, 7), (8, 8)],
                                              'spells': [(1, 5), (2, -1), (3, 5), (4, 0), (5, -1)]})
    compare('the new box',new_box,{'potions': [(8, 8), (7, 7), (6, 6), (5, 5), (1, 1), (2, 1), (3, 1), (4, 1)],
                                   'wands': [(5, 5), (3, 3), (2, 2), (1, 1), (4, -1)],
                                   'spells': [(1, 5), (3, 5), (4, 0), (2, -1), (5, -1)]})

# Test case for Q2D will reveal the answer so not provided    
test_q2a()
test_q2b()
test_q2c()
test_q3a()
test_q3d()
