## CS1010S Nov21 Template

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
square_candy = [[0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 2, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]]

kosong_candy = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

left_triangle = [[0, 0, 0, 1, 0],
                 [0, 0, 2, 2, 0],
                 [0, 3, 3, 3, 0],
                 [0, 0, 2, 2, 0],
                 [0, 0, 0, 1, 0]]

thick_square = [[0, 0, 0, 0, 0],
                [0, 1, 2, 1, 0],
                [0, 2, 3, 2, 0],
                [0, 1, 2, 1, 0],
                [0, 0, 0, 0, 0]]

rand_candy = [[2, 1, 2],
              [1, 0, 1],
              [2, 1, 2]]

## Question 2A
def finished(candy):
    pass # remove this line

## Question 2B
def is_symmetric(candy):
    pass # remove this line

## Question 2C
def rotate(candy):
    pass # remove this line

## Question 2D
def is_pair(candy1, candy2):
    pass # remove this line

## Question 2E
def lick(candy):
    pass # remove this line

## Question 2F
def min_licks(candy):
    pass # remove this line


## Provided for Question 3
table = {
    'Ben': {
        'Kate': [1, 0, -1]
    },
    'Kate': {
        'Ben': [-1, 0, 1],
        'Ron': [0, 1]
    },
    'Ron': {
        'Kate': [0, -1]
    }
}

## Question 3A
def add_game(table, p1, p2, outcome):
    def helper(k1, k2, value):
        pass # help Ben complete this helper function
    
    helper(p1, p2, outcome)
    helper(p2, p1, -outcome)
    
## Question 3B
def verify(table):
    pass # remove this line

## Question 3C
def stats(table, player):
    pass # remove this line

## Question 3D
def highest_win_loss_ratio(table):
    pass # remove this line

## Question 3E
"""
Answer here.
"""

## Question 3F
def scores(table, player):
    pass # remove this line


## Provided for Question 4, feel free to modify.
class Person:
    def __init__(self, vaccinated):
        self.vaccinated = vaccinated

    def get_priority(self):
        if self.vaccinated:
            return 10
        else:
            return 0

class Student(Person):
    def __init__(self, vaccinated):
        super().__init__(vaccinated)
        self.elearning = False

    def get_priority(self):
        priority = super().get_priority() + 10
        if not self.elearning:
            priority += 10
        return priority

class Worker(Person):
    def __init__(self, vaccinated):
        super().__init__(vaccinated)
        self.wfh = True

    def get_priority(self):
        priority = super().get_priority()
        if not self.wfh:
            priority += 10
        return priority


## Question 4A
"""
Answer here.
"""

## Question 4B
"""
Just modify the classes above.
"""

## Question 4C
class Intern(Student, Worker):
    pass

class AdultLearner(Worker, Student):
    pass

"""
Do you think both Intern and AdultLearner will have the correct elearning
and wfh properties set? Explain why.
"""

## Question 4D
"""
Answer here.
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
    compare(1, finished(kosong_candy), True)
    compare(2, finished(square_candy), False)
    compare(3, finished(rand_candy), False)
    for i in range(4, 7):
        compare(i, finished([[0]*(i-1) for _ in range(i)]), True)

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    some_candy = [[0, 1, 0],
                  [1, 0, 1],
                  [0, 1, 0]]
    
    compare(1, is_symmetric(left_triangle), False)
    compare(2, is_symmetric(square_candy), True)
    compare(3, is_symmetric(thick_square), True)
    compare(4, is_symmetric(rand_candy), True)
    compare(5, is_symmetric(kosong_candy), True)
    compare(6, is_symmetric(some_candy), True)
    some_candy[1][1] += 2
    compare(7, is_symmetric(some_candy), True)
    some_candy[2][2] += 2
    compare(8, is_symmetric(some_candy), False)
    
def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    up_triangle = [[0, 0, 0, 0, 0],
                   [0, 0, 3, 0, 0],
                   [0, 2, 3, 2, 0],
                   [1, 2, 3, 2, 1],
                   [0, 0, 0, 0, 0]]
    
    right_triangle = [[0, 1, 0, 0, 0],
                      [0, 2, 2, 0, 0],
                      [0, 3, 3, 3, 0],
                      [0, 2, 2, 0, 0],
                      [0, 1, 0, 0, 0]]
    
    compare(1, rotate(left_triangle), up_triangle)
    compare(2, rotate(rotate(rotate(rotate(up_triangle)))), up_triangle)
    compare(3, rotate(rotate(rotate(rotate(left_triangle)))), left_triangle)
    compare(4, rotate(up_triangle), right_triangle)
    compare(5, rotate(rotate(left_triangle)), right_triangle)

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)
    up_triangle = [[0, 0, 0, 0, 0],
                   [0, 0, 3, 0, 0],
                   [0, 2, 3, 2, 0],
                   [1, 2, 3, 2, 1],
                   [0, 0, 0, 0, 0]]
    
    right_triangle = [[0, 1, 0, 0, 0],
                      [0, 2, 2, 0, 0],
                      [0, 3, 3, 3, 0],
                      [0, 2, 2, 0, 0],
                      [0, 1, 0, 0, 0]]
    
    compare(1, is_pair(left_triangle, up_triangle), True)
    compare(2, is_pair(left_triangle, square_candy), False)
    compare(3, is_pair(left_triangle,right_triangle), True)

def test_q2e():
    print('Testing Question 2E...')
    print('='*20)

    from copy import deepcopy
    left = deepcopy(left_triangle)
    thick = deepcopy(thick_square)
    rand = deepcopy(rand_candy)

    licked_left = [[0, 0, 0, 0, 0],
                   [0, 0, 2, 2, 0],
                   [0, 3, 3, 3, 0],
                   [0, 0, 2, 2, 0],
                   [0, 0, 0, 1, 0]]
    
    licked_thick = [[0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 2, 3, 2, 0],
                    [0, 1, 2, 1, 0],
                    [0, 0, 0, 0, 0]]
    
    licked_rand = [[1, 0, 1],
                   [1, 0, 1],
                   [2, 1, 2]]

    lick(left)
    lick(thick)
    lick(rand)
    lick(kosong_candy)

    compare(1, left, licked_left)
    compare(2, thick, licked_thick)
    compare(3, rand, licked_rand)
    compare(4, kosong_candy, kosong_candy)

def test_q2f():
    print('Testing Question 2F...')
    print('='*20)

    gihun_candy = [[0, 3, 5],
                   [5, 2, 2],
                   [0, 5, 5],
                   [0, 0, 1]]

    compare(1, min_licks(rand_candy), 4)
    compare(2, min_licks(kosong_candy), 0)
    compare(3, min_licks(left_triangle), 9)
    compare(4, min_licks(thick_square), 7)
    compare(5, min_licks(square_candy), 4)
    try:
        compare(6, min_licks(rotate(left_triangle)), 9)
    except:
        compare(6, "to implement the rotate function", 9)
    compare(7, min_licks(gihun_candy), 15)

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    local_table = {
        'Ben': {
            'Kate': [1, 0, -1]
        },
        'Kate': {
            'Ben': [-1, 0, 1],
            'Ron': [0, 1]
        },
        'Ron': {
            'Kate': [0, -1]
        }
    }
    added_table = {
        'Ben': {
            'Kate': [1, 0, -1, -1]
        },
        'Kate': {
            'Ben': [-1, 0, 1, 1],
            'Ron': [0, 1, 0, 1]
        },
        'Ron': {
            'Kate': [0, -1, 0, -1]
        }
    }
    new_table = {}

    add_game(local_table, 'Kate', 'Ron', 0)
    add_game(local_table, 'Ben', 'Kate', -1)
    add_game(local_table, 'Ron', 'Kate', -1)
    compare("added table", local_table, added_table)

    for i in [1, 0, -1]:
        add_game(new_table, 'Ben', 'Kate', i)
    for i in range(2):
        add_game(new_table, 'Ron', 'Kate', -i)
    compare("new table", new_table, table)

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)
    added_table = {
        'Ben': {
            'Kate': [1, 0, -1, -1]
        },
        'Kate': {
            'Ben': [-1, 0, 1, 1],
            'Ron': [0, 1, 0, 1]
        },
        'Ron': {
            'Kate': [0, -1, 0, -1]
        }
    }

    compare(1, verify(table), True)
    compare(2, verify(added_table), True)
    added_table['Ron']['Kate'][0] += 1
    compare(3, verify(added_table), False)
    added_table['Kate']['Ron'][0] -= 1
    compare(4, verify(added_table), True)
    added_table['Ron']['Kate'].pop()
    compare(5, verify(added_table), False)

def test_q3c():
    print('Testing Question 3C...')
    print('='*20)
    added_table = {
        'Ben': {
            'Kate': [1, 0, -1, -1]
        },
        'Kate': {
            'Ben': [-1, 0, 1, 1],
            'Ron': [0, 1, 0, 1]
        },
        'Ron': {
            'Kate': [0, -1, 0, -1]
        }
    }

    compare(1, stats(table, 'Kate'), [2, 2, 1])
    compare(2, stats(table, 'Ben'), [1, 1, 1])
    compare(3, stats(table, 'Ron'), [1, 0, 1])
    compare(4, stats(added_table, 'Kate'), [3, 4, 1])
    compare(5, stats(added_table, 'Ben'), [1, 1, 2])
    compare(6, stats(added_table, 'Ron'), [2, 0, 2])

def test_q3d():
    print('Testing Question 3D...')
    print('='*20)

    # Assume everyone loses at least once
    special_table = {
        'Ben': {
            'Kate': [1, 0, 1, 1, 1, 1, 1, 1, -1]
        },
        'Kate': {
            'Ben': [-1, 0, -1, -1, -1, -1, -1, -1, 1],
            'Ron': [0, 1, 0, 1]
        },
        'Ron': {
            'Kate': [0, -1, 0, -1]
        }
    }

    compare(1, highest_win_loss_ratio(table), 'Kate')
    compare(2, highest_win_loss_ratio(special_table), 'Ben')

def test_q3f():
    print('Testing Question 3F...')
    print('='*20)

    special_table = {
        'Ben': {
            'Kate': [1, 0, 1, 1, 1, 1, 1, 1, -1]
        },
        'Kate': {
            'Ben': [-1, 0, -1, -1, -1, -1, -1, -1, 1],
            'Ron': [0, 1, 0, 1]
        },
        'Ron': {
            'Kate': [0, -1, 0, -1]
        }
    }

    # Best of 7, means you get some nonzero integers in [-4, 4]
    bo7_table = {
        'Ben': {
            'Kate': [1, -1, 1, 1],
            'Jon': [4, 3, 1, -2, -3],
            'Ron': [1, 1, -1, 1, -1]
        },
        'Kate': {
            'Ben': [-1, 1, -1, -1],
            'Ron': [-4, 1, -2, 1]
        },
        'Ron': {
            'Kate': [4, -1, 2, -1],
            'Jon': [2, 3, -4, -4, -4], # get owned!
            'Ben': [-1, -1, 1, -1, 1]
        },
        'Jon': {
            'Ben': [-4, -3, -1, 2, 3],
            'Ron': [-2, -3, 4, 4, 4] # yes Jon is a god
        }
    }

    compare(1, scores(table, 'Ron'), {0: {'Kate': 1}, -1: {'Kate': 1}})
    compare(2, scores(table, 'Ben'), {1: {'Kate': 1}, 0: {'Kate': 1}, -1: {'Kate': 1}})
    compare(3, scores(table, 'Kate'), {-1: {'Ben': 1}, 0: {'Ben': 1, 'Ron': 1}, 1: {'Ben': 1, 'Ron': 1}})
    compare(4, scores(special_table, 'Ron'), {0: {'Kate': 2}, -1: {'Kate': 2}})
    compare(5, scores(special_table, 'Ben'), {1: {'Kate': 7}, 0: {'Kate': 1}, -1: {'Kate': 1}})
    compare(6, scores(special_table, 'Kate'), {-1: {'Ben': 7}, 0: {'Ben': 1, 'Ron': 2}, 1: {'Ben': 1, 'Ron': 2}})
    compare(7, scores(bo7_table, 'Ron'), {4: {'Kate': 1}, -1: {'Kate': 2, 'Ben': 3}, 2: {'Kate': 1, 'Jon': 1}, 3: {'Jon': 1}, -4: {'Jon': 3}, 1: {'Ben': 2}})
    compare(8, scores(bo7_table, 'Kate'), {-1: {'Ben': 3}, 1: {'Ben': 1, 'Ron': 2}, -4: {'Ron': 1}, -2: {'Ron': 1}})
    compare(9, scores(bo7_table, 'Ben'), {1: {'Kate': 3, 'Jon': 1, 'Ron': 3}, -1: {'Kate': 1, 'Ron': 2}, 4: {'Jon': 1}, 3: {'Jon': 1}, -2: {'Jon': 1}, -3: {'Jon': 1}})
    compare(10, scores(bo7_table, 'Jon'), {-4: {'Ben': 1}, -3: {'Ben': 1, 'Ron': 1}, -1: {'Ben': 1}, 2: {'Ben': 1}, 3: {'Ben': 1}, -2: {'Ron': 1}, 4: {'Ron': 3}})

def test_q4a():
    print('Testing Question 4A...')
    print('='*20)
    
    amy = Student(True)
    print(amy.get_priority())
    amy.elearning = True
    print(amy.get_priority())
    
    ben = Worker(False)
    print(ben.get_priority())
    ben.wfh = False
    print(ben.get_priority())
    print()

def test_q4b():
    print('Testing Question 4B...')
    print('='*20)
    
    try:
        amy = Student(True)
        compare(1, amy.can_fly(100), False)
        compare(2, amy.can_fly(0), True)
        ben = Worker(False)
        compare(3, ben.can_fly(0), False)
        ben.pcr_done = True
        compare(4, ben.can_fly(0), True)
    except:
        compare("modify", "still have to implement a function correctly :)", "no error")

test_q2a()
test_q2b()
test_q2c()
test_q2d()
test_q2e()
test_q2f()
test_q3a()
test_q3b()
test_q3c()
test_q3d()
test_q3f()
test_q4a()
test_q4b()
