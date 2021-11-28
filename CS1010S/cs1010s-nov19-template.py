## CS1010S Nov19 Template

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
board = ['       ',
         ' B     ',
         ' APPLE ',
         ' B  E  ',
         ' E  T  ',
         '       ']

## Question 2A
def get_points(word, row, col, vert):
    pass # remove this line

## Question 2B
def get_chars(points, board):
    pass # remove this line

## Question 2C
def num_same(s1, s2):
    pass # remove this line

## Question 2D
def place(word, row, col, vert, board):
    pass # remove this line

## Question 2E
# Using the in-built zip function will fail the test_q2e() function
def zip(*seqs):
    pass # remove this line

## Question 2F
"""
Answer here.
"""

## Provided for Question 3 as a global variable
score_list = ((('D','G'), 2),
              (('B','C','M','P'), 3),
              (('F', 'H', 'V', 'W','Y'), 4),
              (('K',), 5),
              (('J','X'), 8),
              (('Q','Z'), 10))

## Question 3A
def can_form(word, letters):
    pass # remove this line
    
## Question 3B
def tile_score(tile):
    pass # remove this line

## Question 3C
def optimise(score_list):
    pass # remove this line

## Question 3D
def word_score(word, score_dict):
    pass # remove this line

## Question 3E
def make_word_score(score_list):
    return list # placeholder, please remove this line

## Question 3F
def max_score(scoring, words, tiles):
    pass # remove this line

## Provided for Question 4, modify if necessary.
class Car:
    def top_speed(self):
        return 120

    def drive(self, speed):
        print('Vrooom!', min(speed, self.top_speed()), 'km/h')

class SportsCar(Car):
    def __init__(self, boost):
        self.boost = boost
        self.nitro = False
        super().__init__()

    def toggle_nitro(self):
        self.nitro = not self.nitro

class PoliceCar(Car):
    def __init__(self):
        self.siren = False
        super().__init__()

    def toggle_siren(self):
        self.siren = not self.siren

    def drive(self, speed):
        if self.siren:
            print('Bee Doo Bee Doo')
        super().drive(speed)

## Question 4A
"""
Answer here.
"""

## Question 4B
"""
Answer here and modify the code above if necessary.
"""

## Question 4C
class PoliceSportsCar: # add the superclasses in the correct order
    pass # remove this line

## Test Cases
def compare(number,got,expected):
    if got == expected:
        print(f'Test {number} : Passed!')
    else:
        print(f'Test {number} : Failed!')
        print(f'Expected {expected}, got {got}')
    print()

def subtract(word,letters):
    word = list(word)
    for t in letters:
        if t in word:
            word.remove(t)
    return ''.join(word)

# Pro tip : drag all the lines that you want to comment/uncomment and press Alt+3/4

def test_q2a():
    print('Testing Question 2A...')
    print('='*20)
    compare(1,get_points('BEAST',4,0,False),[(4,0), (4,1), (4,2), (4,3), (4,4)])
    compare(2,get_points('BEST',0,6,True),[ (0,6), (1,6), (2,6), (3,6)])

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    compare('X',get_chars([(1,1), (2,2), (3,3), (4,4)],board),'BP T')

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    compare('X',num_same('BOB CAT','DR BRAT'),4)

def test_q2e():
    print('Testing Question 2E...')
    print('='*20)
    compare(1,zip([1, 2, 3], [4, 5, 6], [7, 8, 9, 10]),[(1, 4, 7), (2, 5, 8), (3, 6, 9)])
    compare(2,zip([1, 2], [3, 4], [5, 6]),[(1 ,3, 5), (2, 4, 6)])
    compare(3,zip([1, 2], [3, 4, 5], [6, 7, 8]),[(1 ,3, 6), (2, 4, 7)])
    compare(4,zip([1, 9, 8, 7], [3], [2, 5, 4, 6, 10]),[(1 ,3, 2)])

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    letters = "ANIJOPRKEE"
    compare(1,can_form('JOIN',letters),True)
    compare(2,can_form('KEEP',letters),True)
    compare(3,can_form('KEEPER',letters),False)

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)
    compare(1,tile_score('A'),1)
    compare(2,tile_score('B'),3)
    compare(3,tile_score('Z'),10)
    compare(4,tile_score('X'),8)

def test_q3e():
    print('Testing Question 3E...')
    print('='*20)
    get_score = make_word_score(score_list)
    compare(1,get_score("JOIN"),11)
    compare(2,get_score("KEEP"),10)

def test_q4a():
    print('Testing Question 4A...')
    print('='*20)
    evo = SportsCar(1.5)
    evo.drive(200)
    print()
    police = PoliceCar()
    police.toggle_siren()
    police.drive(100)
    print()

def test_q4c():
    print('Testing Question 4C...')
    print('='*20)
    try:
        police_evo = PoliceSportsCar(1.5)
        police_evo.toggle_nitro()
        police_evo.drive(200)       # Vrooom! 120 km/h

        print()
        police_evo.toggle_siren()
        police_evo.drive(200)       # Bee Doo Bee Doo
        print()                     # Vrooom! 120 km/h
        police_evo.toggle_nitro()
        police_evo.drive(200)       # Bee Doo Bee Doo
        print()                     # Vrooom! 180.0 km/h

        police_evo.toggle_siren()
        police_evo.drive(200)       # Vrooom! 120 km/h
        print()
    except Exception as e:
        print(e)
        print('Implement PoliceSportsCar properly.\n')
 
test_q2a()
test_q2b()
test_q2c()
test_q2e()
test_q3a()
test_q3b()
test_q3e()
test_q4a()
test_q4c()
