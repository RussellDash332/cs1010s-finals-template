## CS1010S Apr24 Template

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
dhi_1 = (1,)
dhi_2 = ((1,), (2, (3,)))
dhi_3 = ((1, 2), ((3,), (((4,),),)))

## Question 2A
"""
Box-and-pointer diagram.
"""

## Question 2B
def count_top_level_ints(dhi):
    pass # remove this line

## Question 2C
def flatten(dhi):
    pass # remove this line

## Question 2D
def count_occurrences(dhi, k):
    pass # remove this line


## Provided for Question 3, do ignore this!
from random import seed, randint
old_seed = seed
def seed(x):
    old_seed(x)
    global get_num
    get_num = f() # reset memory
def f():
    m = set()
    def g():
        while True:
            r = randint(1, 100+len(m))
            if r not in m: m.add(r); break
        return r
    return g
get_num = f()

## Question 3A
def make_card(card_size):
    pass # remove this line

## Question 3B
def make_deck(card_size_list):
    pass # remove this line

## Question 3C
def shift_card_deck(deck):
    pass # remove this line

## Question 3D
def cross_number(deck, num):
    pass # remove this line

## Question 3E
def check_bingo(deck):
    pass # remove this line

## Question 3F
"""
<K> = ...
<R> = ...
"""


## Provided for Question 4
D = {
    (1,2): lambda a,b: a or b,
    (2,3): lambda a,b: a and b,
    (1,3): lambda a,b: not (a and b)
}

## Question 4A
def uniq_vars(D):
    pass # remove this line

## Question 4B
def eval_constraint(C, V):
    pass # remove this line

## Question 4C
def evaluate(D, V):
    pass # remove this line

## Question 4D
def all_values(D):
    pass # remove this line

## Question 4E
def solve(D):
    pass # remove this line


## Test Cases
def compare(number, got, expected):
    if got == expected:
        print(f'Test {number} : Passed!')
    else:
        print(f'Test {number} : Failed!')
        print(f'Expected {expected}, got {got}')
    print()

# Pro tip : drag all the lines that you want to comment/uncomment and press Alt+3/4
def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    compare(1, count_top_level_ints(dhi_1), 1)
    compare(2, count_top_level_ints(dhi_2), 0)
    compare(3, count_top_level_ints(dhi_3), 0)
    compare(4, count_top_level_ints((1, 2, (3, 4))), 2)
    compare(5, count_top_level_ints(((1, 2), (3,), 4, 5, 6, (-1, -2), 3, 8, -7, (1, (1, (1, (1,)))), -1)), 7)
    compare(6, count_top_level_ints(()), 0)
    compare(7, count_top_level_ints((42,)), 1)

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    compare(1, flatten(dhi_1), (1,))
    compare(2, flatten(dhi_2), (1, 2, 3))
    compare(3, flatten(dhi_3), (1, 2, 3, 4))
    compare(4, flatten((1, 2, (3, 4))), (1, 2, 3, 4))
    compare(5, flatten(((1, 2), (3,), 4, 5, 6, (-1, -2), 3, 8, -7, (1, (1, (1, (1,)))), -1)), (1, 2, 3, 4, 5, 6, -1, -2, 3, 8, -7, 1, 1, 1, 1, -1))
    compare(6, flatten(()), ())
    compare(7, flatten((42,)), (42,))

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)
    compare(1, count_occurrences(dhi_1, 3), 0)
    compare(2, count_occurrences(((1, 3), ((3,), (((3,),),))), 3), 3)
    compare(3, count_occurrences(((1, 2), (3,), 4, 5, 6, (-1, -2), 3, 8, -7, (1, (1, (1, (1,)))), -1), 1), 5)
    compare(4, count_occurrences(((1, 2), (3,), 4, 5, 6, (-1, -2), 3, 8, -7, (1, (1, (1, (1,)))), -1), -1), 2)
    compare(5, count_occurrences((), 42), 0)
    compare(6, count_occurrences((42,), 42), 1)
    compare(7, count_occurrences((42,), 0), 0)

def test_q3a():
    print('Testing Question 3A...')
    print('Warning: not including the sample execution on paper!')
    print('='*20)
    seed(170)
    compare(1, make_card(2), [45, 76, 41, 12])
    seed(42)
    compare(2, make_card(3), [82, 15, 4, 95, 36, 32, 29, 18, 14])
    seed(69)
    compare(3, make_card(5), [88, 5, 13, 103, 22, 9, 78, 45, 42, 101, 102, 111, 71, 54, 60, 107, 55, 73, 57, 67, 72, 104, 19, 53, 51])
    seed(1)
    compare(4, make_card(1), [18])

def test_q3b():
    print('Testing Question 3B...')
    print('Warning: not including the sample execution on paper!')
    print('='*20)
    seed(170)
    compare(1, make_deck([2, 3, 3]), [[45, 76, 41, 12], [32, 42, 34, 75, 16, 28, 102, 101, 2], [50, 65, 39, 74, 64, 67, 1, 24, 106]])
    seed(42)
    compare(2, make_deck([1, 5, 2, 1, 1, 1, 7]), [[82], [15, 4, 95, 36, 32, 29, 18, 14, 87, 70, 12, 76, 55, 5, 28, 30, 65, 78, 72, 26, 92, 84, 90, 54, 58], [104, 112, 2, 41], [109], [88], [40], [56, 27, 24, 98, 25, 89, 68, 118, 138, 97, 21, 142, 93, 50, 59, 75, 60, 117, 94, 42, 91, 69, 19, 156, 44, 137, 63, 119, 143, 57, 9, 81, 103, 17, 146, 168, 128, 102, 165, 37, 64, 144, 150, 110, 131, 127, 13, 161, 175]])

def test_q3c():
    print('Testing Question 3C...')
    print('='*20)
    deck = [[45, 52, 12, 9], [23, 12, 654, 123, 45, 890, 1, 11, 9], [48, 1, 134, 7, 125, 30, 9, 28, 12]]
    deck = shift_card_deck(deck)
    compare(1, deck, [[23, 12, 654, 123, 45, 890, 1, 11, 9], [48, 1, 134, 7, 125, 30, 9, 28, 12], [45, 52, 12, 9]])
    deck = shift_card_deck(deck)
    compare(2, deck, [[48, 1, 134, 7, 125, 30, 9, 28, 12], [45, 52, 12, 9], [23, 12, 654, 123, 45, 890, 1, 11, 9]])
    deck = shift_card_deck(deck)
    compare(3, deck, [[45, 52, 12, 9], [23, 12, 654, 123, 45, 890, 1, 11, 9], [48, 1, 134, 7, 125, 30, 9, 28, 12]])
    deck2 = [set() for _ in range(5)]
    seed(1729)
    for i in range(5):
        sz = randint(1, 5)
        while len(deck2[i]) != sz**2: deck2[i].add(randint(1, 1000))
        deck2[i] = [*deck2[i]]
    deck3 = [deck2[i].copy() for i in range(5)]
    for _ in range(5):
        deck3 = shift_card_deck(deck3)
    compare(4, deck2, deck3)

def test_q3d():
    print('Testing Question 3D...')
    print('='*20)
    deck = [[48, 1, 134, 7, 125, 30, 9, 28, 12], [45, 52, 12, 9], [23, 12, 654, 123, 45, 890, 1, 11, 9]]
    deck = cross_number(deck, 45)
    compare(1, deck, [[48, 1, 134, 7, 125, 30, 9, 28, 12], ['X', 52, 12, 9], [23, 12, 654, 123, 'X', 890, 1, 11, 9]])
    deck = cross_number(deck, 23)
    compare(2, deck, [[48, 1, 134, 7, 125, 30, 9, 28, 12], ['X', 52, 12, 9], ['X', 12, 654, 123, 'X', 890, 1, 11, 9]])
    deck = cross_number(deck, 9)
    compare(3, deck, [[48, 1, 134, 7, 125, 30, 'X', 28, 12], ['X', 52, 12, 'X'], ['X', 12, 654, 123, 'X', 890, 1, 11, 'X']])
    deck = cross_number(deck, 12)
    compare(4, deck, [[48, 1, 134, 7, 125, 30, 'X', 28, 'X'], ['X', 52, 'X', 'X'], ['X', 'X', 654, 123, 'X', 890, 1, 11, 'X']])
    deck = cross_number(deck, 1)
    compare(5, deck, [[48, 'X', 134, 7, 125, 30, 'X', 28, 'X'], ['X', 52, 'X', 'X'], ['X', 'X', 654, 123, 'X', 890, 'X', 11, 'X']])

def test_q3e():
    print('Testing Question 3E...')
    print('='*20)
    deck = [[48, 1, 134, 7, 125, 30, 'X', 28, 12], ['X', 52, 12, 'X'], ['X', 12, 654, 123, 'X', 890, 1, 11, 'X']]
    compare(1, check_bingo(deck) in ['Bingo', 'Bingo!'], True) # we eventually accepted both
    deck = [[48, 1, 134, 7, 125, 30, 9, 28, 12], ['X', 52, 12, 9], ['X', 12, 654, 123, 'X', 890, 1, 11, 9]]
    compare(2, check_bingo(deck) in ['No Bingo!', 'Not Bingo!'], True) # we eventually accepted both too
    deck = [[1, 2, 3, 4], [1, 'X', 'X', 4], ['X', 'X', 3, 4], ['X', 2, 'X', 4], [1, 'X', 3, 'X'], [1, 2, 'X', 'X']]
    compare(3, check_bingo(deck) in ['No Bingo!', 'Not Bingo!'], True)
    deck = [[1, 2, 3, 4], [1, 'X', 'X', 4], ['X', 'X', 3, 4], ['X', 2, 'X', 4], [1, 'X', 3, 'X'], [1, 2, 'X', 'X'], [1]]
    compare(4, check_bingo(deck) in ['No Bingo!', 'Not Bingo!'], True)
    deck = [['X', 2, 3, 'X'], [1, 'X', 'X', 4], ['X', 'X', 3, 4], ['X', 2, 'X', 4], [1, 'X', 3, 'X'], [1, 2, 'X', 'X'], [1]]
    compare(5, check_bingo(deck) in ['Bingo', 'Bingo!'], True)
    deck = [[1, 2, 3, 4], [1, 'X', 'X', 4], ['X', 'X', 3, 4], ['X', 2, 'X', 4], [1, 'X', 3, 'X'], [1, 2, 'X', 'X'], ['X']]
    compare(6, check_bingo(deck) in ['Bingo', 'Bingo!'], True)
    deck = [['X', 2, 3, 'X'], [1, 'X', 'X', 4], ['X', 'X', 3, 4], ['X', 2, 'X', 4], [1, 'X', 3, 'X'], [1, 2, 'X', 'X'], ['X']]
    compare(7, check_bingo(deck) in ['Bingo', 'Bingo!'], True)
    deck = [['X', 'X', 'X', 'X'], [1, 'X', 'X', 4], ['X', 'X', 3, 4], ['X', 2, 'X', 4], [1, 'X', 3, 'X'], [1, 2, 'X', 'X'], [122]]
    compare(8, check_bingo(deck) in ['Bingo', 'Bingo!'], True)
    deck = [[1, 'X', 'X', 4], ['X', 'X', 3, 4], ['X', 2, 'X', 4], [1, 'X', 3, 'X'], [1, 2, 'X', 'X'], [122], ['X']*143+[144]]
    compare(9, check_bingo(deck) in ['No Bingo!', 'Not Bingo!'], True)

def test_q4a():
    print('Testing Question 4A...')
    print('='*20)
    compare('type check', type(uniq_vars(D)), list)
    try:
        compare(1, sorted(uniq_vars(D)), [1, 2, 3])
        compare(2, sorted(uniq_vars({(-1, 4): lambda a,b: a or b, (0, 5): lambda a,b: a or (not b), (2270, -7777): lambda a,b: True, (0, 4): lambda a,b: not (a or b)})), [-7777, -1, 0, 4, 5, 2270])
    except:
        compare('error check', True, 'implement uniq_vars properly first!')

def test_q4b():
    print('Testing Question 4B...')
    print('='*20)
    compare(1, eval_constraint(lambda a,b: a or b, [True, False]), True)
    compare(2, eval_constraint(lambda a,b: a or b, [True, True]), True)
    compare(3, eval_constraint(lambda a,b: a or b, [False, False]), False)
    compare(4, eval_constraint(lambda a,b: a or (not b), [True, False]), True) # a <- b
    compare(5, eval_constraint(lambda a,b: a or (not b), [False, True]), False)
    compare(6, eval_constraint(lambda a,b: (not a) and (a and not b), [True, True]), False)
    compare(7, eval_constraint(lambda a,b: (a and not b) or (not a and b), [True, True]), False) # a ^ b
    compare(8, eval_constraint(lambda a,b: (a and not b) or (not a and b), [False, True]), True)
    compare(9, eval_constraint(lambda a,b: (a and not b) or (not a and b), [True, False]), True)
    compare(10, eval_constraint(lambda a,b: (a and not b) or (not a and b), [False, False]), False)

def test_q4c():
    print('Testing Question 4C...')
    print('='*20)
    compare(1, evaluate(D, [False, False, True]), False)
    D2 = {
        (1,3): lambda a,b: a and not b,
        (1,4): lambda a,b: a or not b,
        (2,3): lambda a,b: (not a) and (not b),
        (2,1): lambda a,b: not (a and b) or a
    }
    compare(2, evaluate(D2, [True, True, True, True]), False)
    compare(3, evaluate(D2, [True, False, False, True]), True)
    compare(4, evaluate(D2, [True, False, False, False]), True)
    compare(5, evaluate(D2, [False, False, False, False]), False)

def test_q4d():
    print('Testing Question 4D...')
    print('='*20)
    D = {(2,1): lambda a,b: (not a) and (not b)}
    D2 = {
        (1,3): lambda a,b: a and not b,
        (1,4): lambda a,b: a or not b,
        (2,3): lambda a,b: (not a) and (not b),
        (2,1): lambda a,b: not (a and b) or a
    }
    compare('type check', type(all_values(D)), list)
    try:
        compare(1, sorted(all_values(D)), [[False, False], [False, True], [True, False], [True, True]])
        compare(2, sorted(all_values({(-1, 4): lambda a,b: a or b, (0, 5): lambda a,b: a or (not b), (2270, -7777): lambda a,b: True, (0, 4): lambda a,b: not (a or b)})), [[False, False, False, False, False, False], [False, False, False, False, False, True], [False, False, False, False, True, False], [False, False, False, False, True, True], [False, False, False, True, False, False], [False, False, False, True, False, True], [False, False, False, True, True, False], [False, False, False, True, True, True], [False, False, True, False, False, False], [False, False, True, False, False, True], [False, False, True, False, True, False], [False, False, True, False, True, True], [False, False, True, True, False, False], [False, False, True, True, False, True], [False, False, True, True, True, False], [False, False, True, True, True, True], [False, True, False, False, False, False], [False, True, False, False, False, True], [False, True, False, False, True, False], [False, True, False, False, True, True], [False, True, False, True, False, False], [False, True, False, True, False, True], [False, True, False, True, True, False], [False, True, False, True, True, True], [False, True, True, False, False, False], [False, True, True, False, False, True], [False, True, True, False, True, False], [False, True, True, False, True, True], [False, True, True, True, False, False], [False, True, True, True, False, True], [False, True, True, True, True, False], [False, True, True, True, True, True], [True, False, False, False, False, False], [True, False, False, False, False, True], [True, False, False, False, True, False], [True, False, False, False, True, True], [True, False, False, True, False, False], [True, False, False, True, False, True], [True, False, False, True, True, False], [True, False, False, True, True, True], [True, False, True, False, False, False], [True, False, True, False, False, True], [True, False, True, False, True, False], [True, False, True, False, True, True], [True, False, True, True, False, False], [True, False, True, True, False, True], [True, False, True, True, True, False], [True, False, True, True, True, True], [True, True, False, False, False, False], [True, True, False, False, False, True], [True, True, False, False, True, False], [True, True, False, False, True, True], [True, True, False, True, False, False], [True, True, False, True, False, True], [True, True, False, True, True, False], [True, True, False, True, True, True], [True, True, True, False, False, False], [True, True, True, False, False, True], [True, True, True, False, True, False], [True, True, True, False, True, True], [True, True, True, True, False, False], [True, True, True, True, False, True], [True, True, True, True, True, False], [True, True, True, True, True, True]])
        compare(3, sorted(all_values(D2)), [[False, False, False, False], [False, False, False, True], [False, False, True, False], [False, False, True, True], [False, True, False, False], [False, True, False, True], [False, True, True, False], [False, True, True, True], [True, False, False, False], [True, False, False, True], [True, False, True, False], [True, False, True, True], [True, True, False, False], [True, True, False, True], [True, True, True, False], [True, True, True, True]])
    except:
        compare('error check', True, 'implement all_values properly first!')

def test_q4e():
    print('Testing Question 4E...')
    print('='*20)
    D1 = {
        (2,1): lambda a,b: (not a) and (not b)
    }
    D2 = {
        (1,3): lambda a,b: a and not b,
        (1,4): lambda a,b: a or not b,
        (2,3): lambda a,b: (not a) and (not b),
        (2,1): lambda a,b: not (a and b) or a
    }
    D3 = {
        (1,2): lambda a,b: a or b,
        (2,3): lambda a,b: a and b,
        (1,3): lambda a,b: not (a and b)
    }
    D4 = {
        (1,2): lambda a,b: a and b,
        (2,1): lambda a,b: (not a) and b
    }
    D5 = {
        (1,2): lambda a,b: a,
        (1,3): lambda a,b: a or b,
        (5,2): lambda a,b: b,
        (2,4): lambda a,b: a or (not b),
        (5,3): lambda a,b: (not b) or a,
        (3,2): lambda a,b: b or a or (not a),
        (1,4): lambda a,b: a and b,
        (2,3): lambda a,b: a and (not b),
        (5,1): lambda a,b: a or (not b)
    }
    D6 = {
        (1,2): lambda a,b: a,
        (1,3): lambda a,b: a or b,
        (5,2): lambda a,b: b,
        (2,4): lambda a,b: a or (not b),
        (5,3): lambda a,b: (not b) or a,
        (3,2): lambda a,b: b or a or (not a),
        (1,4): lambda a,b: a and b,
        (2,3): lambda a,b: a and (not b),
        (5,1): lambda a,b: a or (not b),
        (1,6): lambda a,b: b,
        (2,1): lambda a,b: (not a) and b
    }
    D7 = {
        (1,2): lambda a,b: a,
        (1,3): lambda a,b: a or b,
        (5,2): lambda a,b: b,
        (2,4): lambda a,b: a or (not b),
        (5,3): lambda a,b: (not b) or a,
        (3,2): lambda a,b: b or a or (not a),
        (1,4): lambda a,b: a and b,
        (2,3): lambda a,b: a and (not b),
        (5,1): lambda a,b: a or (not b),
        (1,6): lambda a,b: b
    }
    D8 = {}
    for i in range(1, 11):
        if i%2: D8[(i, i+1)] = lambda a,b: a and not b
        else: D8[(i, i+1)] = lambda a,b: b and not a
    compare(1, solve(D1), [False, False])
    compare(2, solve(D2) in [[True, False, False, True], [True, False, False, False]], True)
    compare(3, solve(D3), [False, True, True])
    compare(4, solve(D4), [])
    compare(5, solve(D5), [True, True, False, True, True])
    compare(6, solve(D6), [])
    compare(7, solve(D7), [True, True, False, True, True, True])
    compare(8, solve(D8), [True, False, True, False, True, False, True, False, True, False, True])
    D8[(1, 11)] = lambda a,b: (not a) and (not b)
    compare(9, solve(D8), [])

test_q2b()
test_q2c()
test_q2d()
test_q3a()
test_q3b()
test_q3c()
test_q3d()
test_q3e()
test_q4a()
test_q4b()
test_q4c()
test_q4d()
test_q4e()
