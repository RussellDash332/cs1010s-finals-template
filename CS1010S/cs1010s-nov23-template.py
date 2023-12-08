## CS1010S Nov23 Template

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
mat = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0]
]
links = [(0, 1), (1, 2), (0, 2), (2, 3), (3, 4)]

## Question 2A
def to_adjacency(n, links):
    pass # remove this line

## Question 2B
def get_neighbours(mat, router):
    pass # remove this line

## Question 2C
def router_down(mat, router):
    pass # remove this line

## Question 2D
# Provided, do not modify!
def is_connected(mat):
    n_vertices = len(mat)
    visited = [False] * n_vertices
    # starting the traversal at vertex 0
    BFS(mat, 0, visited)
    # all evaluates to True only if all entries are True
    return all(visited)

def BFS(mat, source, visited):
    pass # remove this line

## Question 2E
from copy import copy, deepcopy
def is_robust(mat, v):
    pass # remove this line


## Provided for Question 3
studentDB = {
    "A0123873A": {'CS1010S': {'CA': 15, 'Exams': 78},
                  'CS1231S': {'CA': 18, 'Exams': 65}},
    "A0126313B": {'CS1010S': {'CA': 11, 'Exams': 61},
                  'MA1101R': {'CA': 20, 'Exams': 70}},
}

## Question 3A
def get_average(studentDB, student):
    pass # remove this line

## Question 3B
def SU(studentDB, student, course):
    pass # remove this line

## Question 3C
def pivot(studentDB):
    pass # remove this line

## Question 3D
def get_failures(studentDB):
    pass # remove this line

## Question 3E
"""
Answer here.
"""


## Provided for Question 4, feel free to modify.
class Item():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def get_damage(self):
        return self.damage

class Weapon(Item):
    def __init__(self, name, damage):
        self.name = "Weapon: " + name
        self.fused_with = None
        super().__init__(name, damage)

    def fuse(self, item):
        self.fused_with = item

    def get_damage(self):
        return self.damage + self.fused_with.get_damage()

class GerudoWeapon(Weapon):
    def get_damage(self):
        item_damage = self.fused_with.get_damage() * 2
        return self.damage + item_damage

# For Question 4D onwards
class Korok:
    def __init__(self):
        self.name = "Korok"
        self.damage = 1

    def get_damage(self):
        return self.damage

## Question 4A
"""
Rewrite the __init__ in the class Weapon using only a maximum of
TWO (2) statements to fix the problem.
"""

## Question 4B
"""
Provide an explanation for this behaviour.
"""

## Question 4C
"""
Using at most TWO (2) statements, create an infinite recursion!
"""

## Question 4D
"""
Rewrite ONLY Weapon.fuse and Weapon.get_damage to fix the logic error
while adhering to the good OOP practice.
"""

## Question 4E
"""
Rewrite ONLY GerudoWeapon.get_damage to fix the logic error
while adhering to the good OOP practice.
"""


## Test Cases
def compare(number, got, expected):
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
    mat = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]
    links = [(0, 1), (1, 2), (0, 2), (2, 3), (3, 4)]
    compare(1, to_adjacency(5, links), mat)
    compare(2, to_adjacency(1, []), [[0]])
    compare(3, to_adjacency(3, [(1, 0), (1, 2)]), [[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    compare(4, to_adjacency(5, [(2, 3), (0, 4), (2, 1)]), [[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 0]])

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    mat = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]
    compare(1, get_neighbours(mat, 0), (1, 2))
    compare(2, get_neighbours(mat, 4), (3,))
    compare(3, get_neighbours([[0]], 0), ())
    compare(4, get_neighbours([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 0]], 2), (1, 3))
    compare(5, get_neighbours([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0), (1, 2))

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    mat = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]
    router_down(mat, 0)
    compare(1, mat, [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ])
    router_down(mat, 2)
    compare(2, mat, [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0]
    ])
    mat = [[1]*6 for _ in range(6)]
    for i in range(6): mat[i][i] = 0
    router_down(mat, 5), router_down(mat, 1)
    compare(3, mat, [
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ])

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)
    def is_connected(mat):
        visited = [False] * len(mat)
        BFS(mat, 0, visited)
        return all(visited)
    mat = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]
    compare(1, is_connected(mat), True)
    compare(2, is_connected([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0]
    ]), False)
    compare(3, is_connected([
        [0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0]
    ]), False)
    compare(4, is_connected([
        [0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0]
    ]), True)
    compare(5, is_connected([
        [0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]), False)
    compare(6, is_connected([
        [0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0],
    ]), True)
    compare(7, is_connected([
        [0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0]
    ]), False)
    compare(8, is_connected([
        [0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 0]
    ]), True)
    compare(9, is_connected([[0]*10 for _ in range(10)]), False)

def test_q2e():
    print('Testing Question 2E...')
    print('='*20)
    mat = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]
    compare(1, is_robust(mat, 0), True)
    compare(2, is_robust(mat, 2), False)
    compare(3, mat, [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ])
    mat2 = [
        [0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0],
    ]
    mat3 = deepcopy(mat2)
    compare(4, is_robust(mat2, 1), False)
    compare(5, is_robust(mat2, 0), True)
    compare(6, is_robust(mat2, 5), False)
    compare(7, is_robust(mat2, 4), True)
    compare(8, mat2, mat3)
    mat4 = [
        [0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0]
    ]
    compare(9, is_robust(mat4, 4), True)

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    studentDB = {
        "A0123873A": {'CS1010S': {'CA': 15, 'Exams': 78},
                      'CS1231S': {'CA': 18, 'Exams': 65}},
        "A0126313B": {'CS1010S': {'CA': 11, 'Exams': 61},
                      'MA1101R': {'CA': 20, 'Exams': 70}},
        "A0123456X": {},
        "A0000000G": {'CS1101S': {'Finals': 82},
                      'DSA1101': {'Tut': 10, 'Part': 10, 'Mid': 20, 'Finals': 43},
                      'HSH1000': {'CA1': 30, 'CA2': 27, 'CA3': 25, 'Tut': 9}}
    }
    compare(1, get_average(studentDB, 'A0123873A'), 88.0)
    compare(2, get_average(studentDB, 'A0126313B'), 81.0)
    compare(3, get_average(studentDB, 'A0123456X'), 0)
    compare(4, get_average(studentDB, 'A0000000G'), 256/3)

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)
    studentDB = {
        "A0123873A": {'CS1010S': {'CA': 15, 'Exams': 78},
                      'CS1231S': {'CA': 18, 'Exams': 65}},
        "A0126313B": {'CS1010S': {'CA': 11, 'Exams': 61},
                      'MA1101R': {'CA': 20, 'Exams': 70}},
        "A0123456X": {},
        "A0000001B": {'ES1103': {'CA': 38},
                      'CS1101S': {'Finals': 71}},
        "A0000000G": {'CS1101S': {'Finals': 82},
                      'DSA1101': {'Tut': 10, 'Part': 10, 'Mid': 20, 'Finals': 43},
                      'HSH1000': {'CA1': 30, 'CA2': 27, 'CA3': 25, 'Tut': 9}}
    }
    studentDB2 = {
        "A0123873A": {'CS1010S': {'CA': 15, 'Exams': 78},
                      'CS1231S': {'CA': 18, 'Exams': 65}},
        "A0126313B": {'CS1010S': {'CA': 11, 'Exams': 61},
                      'MA1101R': {'CA': 20, 'Exams': 70}},
        "A0123456X": {},
        "A0000001B": {'ES1103': {'CA': 38},
                      'CS1101S': {'Finals': 71}},
        "A0000000G": {'CS1101S': {'Finals': 82},
                      'DSA1101': {'Tut': 10, 'Part': 10, 'Mid': 20, 'Finals': 43},
                      'HSH1000': {'CA1': 30, 'CA2': 27, 'CA3': 25, 'Tut': 9}}
    }
    studentDB3 = {
        "A0123873A": {'CS1010S': {'CA': 15, 'Exams': 78},
                      'CS1231S': {'CA': 18, 'Exams': 65}},
        "A0126313B": {'CS1010S': {'CA': 11, 'Exams': 61}},
        "A0123456X": {},
        "A0000001B": {'ES1103': {'CA': 38},
                      'CS1101S': {'Finals': 71}},
        "A0000000G": {'CS1101S': {'Finals': 82},
                      'DSA1101': {'Tut': 10, 'Part': 10, 'Mid': 20, 'Finals': 43}}
    }
    SU(studentDB, 'A0123456X', 'CS1010E')
    compare(1, studentDB, studentDB2)
    SU(studentDB, 'A0000001B', 'ES1103')
    compare(2, studentDB, studentDB2)
    SU(studentDB, 'A0126313B', 'MA1101R')
    SU(studentDB, 'A0000000G', 'HSH1000')
    compare(3, studentDB, studentDB3)

def test_q3c():
    print('Testing Question 3C...')
    print('='*20)
    studentDB = {
        "A0123873A": {'CS1010S': {'CA': 15, 'Exams': 78},
                      'CS1231S': {'CA': 18, 'Exams': 65}},
        "A0126313B": {'CS1010S': {'CA': 11, 'Exams': 61},
                      'MA1101R': {'CA': 20, 'Exams': 70}},
        "A0123456X": {},
        "A0000000G": {'CS1101S': {'Finals': 82},
                      'DSA1101': {'Tut': 10, 'Part': 10, 'Mid': 20, 'Finals': 43},
                      'HSH1000': {'CA1': 30, 'CA2': 27, 'CA3': 25, 'Tut': 9}}
    }
    courseDB =  {
        "CS1010S": {'A0123873A': {'CA': 15, 'Exams': 78},
                    'A0126313B': {'CA': 11, 'Exams': 61}},
        "CS1231S": {'A0123873A': {'CA': 18, 'Exams': 65}},
        "MA1101R": {'A0126313B': {'CA': 20, 'Exams': 70}},
        "CS1101S": {'A0000000G': {'Finals': 82}},
        "DSA1101": {'A0000000G': {'Tut': 10, 'Part': 10, 'Mid': 20, 'Finals': 43}},
        "HSH1000": {'A0000000G': {'CA1': 30, 'CA2': 27, 'CA3': 25, 'Tut': 9}}
    }
    compare(1, pivot(studentDB), courseDB)
    compare(2, pivot({}), {})

def test_q3d():
    print('Testing Question 3D...')
    print('='*20)
    studentDB = {
        "A0123873A": {'CS1010S': {'CA': 15, 'Exams': 78},
                      'CS1231S': {'CA': 18, 'Exams': 65}},
        "A0126313B": {'CS1010S': {'CA': 11, 'Exams': 61},
                      'MA1101R': {'CA': 20, 'Exams': 70}},
        "A0123456X": {'CS1010S': {'CA': 10, 'Exams': 10}},
        "A0123457X": {'CS1010S': {'CA': 10, 'Exams': 11}},
        "A0123458X": {'CS1010S': {'CA': 10, 'Exams': 12}},
        "A0123459X": {},
        "A0000001B": {'ES1103': {'CA': 38},
                      'CS1101S': {'Finals': 71}},
        "A0000000G": {'CS1101S': {'Finals': 82},
                      'DSA1101': {'Tut': 10, 'Part': 10, 'Mid': 20, 'Finals': 43},
                      'HSH1000': {'CA1': 30, 'CA2': 27, 'CA3': 25, 'Tut': 9}}
    }
    compare(1, get_failures(studentDB), {'CS1010S': 3, 'CS1231S': 0, 'MA1101R': 0, 'ES1103': 1, 'CS1101S': 0, 'DSA1101': 0, 'HSH1000': 0})
    compare(2, get_failures({}), {})

def test_q4a():
    print('Testing Question 4A...')
    print('='*20)
    horn = Item("Bokoblin's Horn", 5)
    sword = Weapon("Master Sword", 30)
    biggoron = Weapon("Biggoron Sword", 30)
    scimitar = GerudoWeapon("Scimitar of the Seven", 28)
    compare(1, horn.name, "Bokoblin's Horn")
    compare(2, sword.name, "Weapon: Master Sword")
    compare(3, biggoron.name, "Weapon: Biggoron Sword")
    compare(4, scimitar.name, "Weapon: Scimitar of the Seven")

def test_q4d():
    print('Testing Question 4D...')
    print('='*20)
    sword = Weapon("Master Sword", 30)
    sword.fuse(Korok())
    compare(1, sword.get_damage(), 30)
    sword = Weapon("Master Sword", 30)
    sword.fuse(Weapon("Master Sword", 30))
    try: compare(2, sword.get_damage(), 60)
    except: compare(2, 'fix fuse and get_damage first!', 'no attribute error')
    fake_scimitar = Weapon("Scimitar of the Seven", 28) # not the GerudoWeapon scimitar
    fake_scimitar.fuse(fake_scimitar)
    try: compare(3, fake_scimitar.get_damage(), 28)
    except: compare(3, 'fix fuse and get_damage first!', 'no infinite recursion')

def test_q4e():
    print('Testing Question 4E...')
    print('='*20)
    scimitar = GerudoWeapon("Scimitar of the Seven", 28)
    scimitar.fuse(GerudoWeapon("Scimitar of the Seven", 28))
    try: compare(1, scimitar.get_damage(), 84)
    except: compare(1, 'fix get_damage first!', 'no attribute error')
    gerudo = GerudoWeapon("Gerudo Sword", 10)
    gerudo.fuse(scimitar)
    try: compare(2, gerudo.get_damage(), 178)
    except: compare(2, 'fix get_damage first!', 'no issue')
    gerudo.fuse(gerudo)
    try: compare(3, gerudo.get_damage(), 178)
    except: compare(3, 'fix get_damage first!', 'no infinite recursion')
    gerudo = GerudoWeapon("Gerudo Sword", 10)
    gerudo.fuse(gerudo)
    try: compare(4, gerudo.get_damage(), 10)
    except: compare(4, 'fix get_damage first!', 'no infinite recursion')
    w1 = Weapon('A', 10)
    w2 = GerudoWeapon('B', 11)
    w3 = Weapon('C', 12)
    w4 = GerudoWeapon('D', 13)
    w5 = GerudoWeapon('E', 14)
    w5.fuse(w4), w4.fuse(w3), w3.fuse(w2), w2.fuse(w1), w1.fuse(w1)
    try: compare(5, w5.get_damage(), 212)
    except: compare(5, 'fix get_damage first!', 'no issue')
    w1.fuse(gerudo), gerudo.fuse(scimitar)
    try: compare(6, w5.get_damage(), 1636) # that's a lot of damage!
    except: compare(6, 'fix get_damage first!', 'no issue')

test_q2a()
test_q2b()
test_q2c()
test_q2d()
test_q2e()
test_q3a()
test_q3b()
test_q3c()
test_q3d()
test_q4a()
test_q4d()
test_q4e()
