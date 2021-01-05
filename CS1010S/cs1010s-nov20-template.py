#!/usr/bin/env python3
## CS1010S Nov20 Template

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

## Provided for Question 2
levels = ((8, 0, 19), (7, 20, 44), (6, 45, 64), (5, 65, 74),
          (4, 75, 79), (3, 80, 84), (2, 85, 89), (1, 90, 100))
updated_levels = ((8, 0), (7, 20), (6, 45), (5, 65), (4, 75), (3, 80), (2, 85),
                  (1, 90))

## Question 2A
def get_level(score, levels):
    pass # remove this line

## Question 2B
def create_levels(levels):
    return str # placeholder, please remove this line

## Question 2C
def tabulate_score(scores, levels):
    pass # remove this line

## Question 2D
def score_distribution(table):
    pass # remove this line

## Provided for Question 3
trie = {'a': {'.': ''},
        't': {'o': {'.': ''},
              'e': {'.': '',
                    'a': {'.': ''},
                    'n': {'.': ''}}},
        'b': {'o': {'o': {'.': ''}}}}

## Question 3A
def next_char(node, prefix):
    pass # remove this line
    
## Question 3B
def prefix_of(node, char):
    pass # remove this line

## Question 3C
def has_word(trie, word):
    pass # remove this line

## Question 3D
def add_word(trie, word):
    pass # remove this line

## Question 3E
"""
has_word
Time :
Space :

add_word
Time :
Space :
"""

## Provided for Question 4, no need to modify.
class Task:
    def __init__(self, name):
        self.name = name
        self.done = False

class Crewmate:
    def __init__(self, tasks):
        self.tasks = tasks
        self.alive = True

    def do(self, task):
        if task.done:
            print(task.name + ' already done')
        else:
            print('Doing ' + task.name)
            task.done = True

## Question 4A
"""
Answer here.
"""

## Question 4B
"""
Answer here.
"""

## Question 4C
class Impostor: # note Impostor is not a subclass of Crewmate
    def kill(self, crewmate):
        if crewmate.alive:
            print("Stab Stab Stab")
            crewmate.alive = False
            return True
        else:
            return False
"""
Answer here and modify the code above.
"""

## Question 4D
class Vigilante: # add the superclasses in the correct order
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

def test_q2a():
    print('Testing Question 2A...')
    print('='*20)
    compare(1,get_level(20,levels),7)
    compare(2,get_level(50,levels),6)
    compare(3,get_level(99,levels),1)

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    new_psle = create_levels(updated_levels)
    compare(1,new_psle(44.5),7)
    compare(2,new_psle(64.7),6)
    compare(3,new_psle(99.5),1)

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    scores = (13, 100, 55, 31, 79, 12, 77, 66, 34, 76, 98)
    scores2 = (30, 25, 35, 100, 98, 97)
    compare(1,tabulate_score(scores, updated_levels),{8: 2, 1: 2, 6: 1, 7: 2, 4: 3, 5: 1})
    compare(2,tabulate_score(scores2, updated_levels),{7: 3, 1: 3})

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)
    scores = (13, 100, 55, 31, 79, 12, 77, 66, 34, 76, 98)
    scores2 = (30, 25, 35, 100, 98, 97)
    compare(1,score_distribution(tabulate_score(scores, updated_levels)),((4, 3), (1, 2), (7, 2), (8, 2), (5, 1), (6, 1)))
    compare(2,score_distribution(tabulate_score(scores2, updated_levels)),((1, 3), (7, 3)))

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    try:
        compare(1,sorted(next_char(trie, 't')),sorted(['e', 'o']))
    except:
        compare(1,'error',sorted(['e', 'o']))
    compare(2,next_char(trie, 'a'),['.'])
    compare(3,next_char(trie, 'e'),[])
    try:
        compare(4,sorted(next_char(trie['t'], 'e')),sorted(['.', 'a', 'n']))
    except:
        compare(4,'error',sorted(['.', 'a', 'n']))

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)
    try:
        compare(1,sorted(prefix_of(trie, 'o')),sorted(['b', 't']))
    except:
        compare(1,'error',sorted(['b', 't']))
    compare(2,prefix_of(trie, 'a'),[])
    try:
        compare(3,sorted(prefix_of(trie['t']['e'], '.')),sorted(['a', 'n']))
    except:
        compare(3,'error',sorted(['a', 'n']))
    
def test_q3c():
    print('Testing Question 3C...')
    print('='*20)
    compare(1,has_word(trie, 'tea'),True)
    compare(2,has_word(trie, 'team'),False)

def test_q3d():
    print('Testing Question 3D...')
    print('='*20)
    add_word(trie, 'are')
    add_word(trie, 'bo')
    compare('new trie',trie,{'a': {'.': '',
                                   'r': {'e': {'.': ''}}},
                             't': {'o': {'.': ''},
                                   'e': {'.': '',
                                         'a': {'.': ''},
                                         'n': {'.': ''}}},
                             'b': {'o': {'.': '',
                                         'o': {'.': ''}}}})

def test_q4():
    print('Testing Question 4...')
    print('='*20)
    tasks = [Task('fix wiring'), Task('empty chute')]
    russell = Crewmate(tasks.copy())
    tasks.append(Task('swipe card'))
    matthew = Crewmate(tasks.copy())

    print('# Question 4A #')
    russell.do(Task('fix wiring'))
    russell.do(Task('fix wiring'))
    print()

    print('# Question 4B #')
    russell.do(russell.tasks[0])
    matthew.do(matthew.tasks[0])
    print()

    print('# Question 4C #')
    ben = Impostor()
    compare('if Prof Ben "spares" me',ben.kill(russell),True)
    compare('if Prof Ben overkills me',ben.kill(russell),False)

    jon = Impostor()
    try:
        compare('if Prof Ben can kill Jon',ben.kill(jon),False)
    except Exception as e:
        print(e)
        print('Modify the code to return False when an Impostor is not killing a Crewmate!\n')
    finally:
        print('# Question 4D #')
        try:
            waikay = Vigilante(tasks, matthew)
            compare('if Prof Wai Kay wants to kill me too',waikay.kill(russell),False)
            compare('if I am not the only one dead',waikay.kill(matthew),True)
            compare('if waikay can kill ben',waikay.kill(ben),False)
            compare('if the revenge is a success',ben.kill(waikay),True)
        except Exception as e:
            print(e)
            print('Please implement Vigilante correctly!\n')
        

test_q2a()
test_q2b()
test_q2c()
test_q2d()
test_q3a()
test_q3b()
test_q3c()
test_q3d()
test_q4()
