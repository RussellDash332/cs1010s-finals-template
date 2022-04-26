## CS1010S Apr22 Template

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
image1 = [
    [[0.3, 1, 1], [0, 0.6, 0.6], [0, 0, 1]],
    [[0, 1, 0], [0, 0.6, 0.3], [0, 0, 0.5]],
    [[0, 1, 0.2], [0.3, 0.6, 0], [0, 0, 0]],
]

image2 = [
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0]
]

## Question 2A
def empty(nrows, ncols):
    pass # remove this line

## Question 2B
def rgb_to_grayscale(image):
    pass # remove this line

## Question 2C
def crop(image, r, c, nrows, ncols):
    pass # remove this line

## Question 2D
def representative(image, r, c, n):
    pass # remove this line

## Question 2E
def scale_down(image, n):
    pass # remove this line

## Question 2F
def next_valid(image, r, c):
    pass # remove this line

## Question 2G
def paint_bucket(image, r, c, value):
    pass # remove this line


## Provided for Question 3
restrictionEnzymes = {
    'bamH1': ('GGATCC', 0),
    'ecoR1': ('GAATTC', 1),
    'sma1': ('CCCGGG', 2)
}
seq = "TCCGGATCCCGGGATGGA"

## Question 3A
def findAll(source, pattern):
    pass # remove this line
    
## Question 3B
def getFragments(seq, restriction, enzyme):
    pass # remove this line

## Question 3C
def getGoodEnzyme(seq, restriction):
    pass # remove this line

## Question 3D
"""
Answer here.
"""

## Question 3E
def circularFindAll(source, pattern):
    pass # remove this line

## Question 3F
def getCircularFragments(seq, restriction, enzyme):
    pass # remove this line


## Provided for Question 4, feel free to modify.
class Team:
    def __init__(self):
        self.base_budget = 1000

    def get_budget(self):
        return self.base_budget

class Testing(Team):
    def __init__(self):
        self.testing_budget = 2000
        self.frozen = False

    def freeze_budget(self):
        self.frozen = True

    def get_budget(self):
        if self.frozen:
            return super().get_budget()
        return self.testing_budget + super().get_budget()

class Development(Team):
    def __init__(self):
        self.development_budget = 4000
        self.frozen = False

    def freeze_budget(self):
        self.frozen = True

    def get_budget(self):
        if self.frozen:
            return super().get_budget()
        return self.development_budget + super().get_budget()

T1 = Development()
T2 = Testing()

## Question 4A
"""
Answer here and modify the classes above.
"""

## Question 4B
"""
Answer here and modify the classes above.
"""

## Question 4C
class Sprint1(Development, Testing):
    pass

class Sprint2(Testing, Development):
    pass

T3 = Sprint1()
T4 = Sprint2()
"""
What will be the budget for team T3 and T4? What is the MRO for Sprint1 and Sprint2?
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
    
    compare(1, empty(3, 2), [[0, 0], [0, 0], [0, 0]])
    another_empty = empty(2, 3)
    try:
        another_empty[0][1], another_empty[1][2], another_empty[1][0] = 1, 2, 3
        compare(1, another_empty, [[0, 1, 0], [3, 0, 2]])
    except:
        compare("empty", "still have to implement a function correctly :)", "no error")

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)

    image1 = [
        [[0.3, 1, 1], [0, 0.6, 0.6], [0, 0, 1]],
        [[0, 1, 0], [0, 0.6, 0.3], [0, 0, 0.5]],
        [[0, 1, 0.2], [0.3, 0.6, 0], [0, 0, 0]],
    ]

    compare(1, rgb_to_grayscale(image1), [[0.1, 1, 0.4], [0.1, 0.6, 0.3], [0, 0, 0.5]])
    
def test_q2c():
    print('Testing Question 2C...')
    print('='*20)

    image2 = [
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0]
    ]

    candy_image = [[0, 0, 0, 0],
                   [0, 0, 3, 0],
                   [0, 2, 3, 2],
                   [1, 2, 3, 2]]
    
    candy2_image = [[1, 0, 0, 0],
                    [2, 2, 0, 0],
                    [3, 3, 3, 0],
                    [2, 2, 0, 0]]
    
    compare(1, crop(image2, 1, 1, 3, 2), [[0, 1], [1, 0], [1, 1]])
    compare(2, crop(image2, 0, 2, 2, 2), [[0, 1], [1, 0], [1, 1]])
    compare(3, crop(candy_image, 1, 1, 3, 3), [[0, 3, 0], [2, 3, 2], [2, 3, 2]])
    compare(4, crop(candy_image, 3, 1, 1, 1), [[2]])
    compare(5, crop(candy2_image, 0, 0, 3, 3), [[1, 0, 0], [2, 2, 0], [3, 3, 3]])
    compare(6, crop(candy2_image, 1, 0, 1, 4) == crop(candy2_image, 3, 0, 1, 4), True)

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)

    image2 = [
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0]
    ]

    dalgona_image = [[0, 0, 0, 0, 0],
                     [0, 0, 3, 0, 0],
                     [0, 2, 3, 2, 0],
                     [1, 2, 3, 2, 1],
                     [0, 0, 0, 0, 0]]
    
    compare(1, representative(image2, 0, 0, 2), 0)
    compare(2, representative(image2, 1, 1, 2), 0.5)
    compare(3, representative(image2, 0, 0, 4), 0.5)
    compare(4, representative(dalgona_image, 2, 2, 1), 3)
    compare(5, representative(dalgona_image, 0, 0, 5), 0.76)

def test_q2e():
    print('Testing Question 2E...')
    print('='*20)

    image2 = [
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0]
    ]

    dalgona_image = [[0, 0, 0, 0, 0],
                     [0, 0, 3, 0, 0],
                     [0, 2, 3, 2, 0],
                     [1, 2, 3, 2, 1],
                     [0, 0, 0, 0, 0]]

    compare(1, scale_down(image2, 2), [[0, 1], [0.5, 0.5]])
    compare(2, scale_down(image2, 4), [[0.5]])
    compare(3, scale_down(dalgona_image, 1), dalgona_image)
    compare(4, scale_down(dalgona_image, 5), [[0.76]])

def test_q2f():
    print('Testing Question 2F...')
    print('='*20)

    image2 = [
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0]
    ]

    image3 = [
        [1, 0, 1, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 0]
    ]

    try:
        compare(1, sorted(next_valid(image3, 1, 3)), [(0, 3), (1, 2), (2, 3)])
        compare(2, sorted(next_valid(image3, 2, 1)), [(2, 0), (3, 1)])
        compare(3, sorted(next_valid(image3, 0, 0)), [])
        compare(4, sorted(next_valid(image2, 0, 0)), [(0, 1), (1, 0)])
        compare(5, sorted(next_valid(image2, 3, 1)), [(2, 1), (3, 2)])
    except:
        compare("next_valid", "still have to implement a function correctly :)", "no error")

def test_q2g():
    print('Testing Question 2G...')
    print('='*20)

    image2 = [
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0]
    ]

    image3 = [
        [1, 0, 1, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 0]
    ]

    paint_bucket(image2, 1, 1, 0.12)
    paint_bucket(image2, 3, 1, 7)
    paint_bucket(image2, 3, 3, 1)
    paint_bucket(image2, 3, 3, 4)

    paint_bucket(image3, 2, 2, 0.3)
    paint_bucket(image3, 0, 1, 1.2)

    new_image2 = [
        [0.12, 0.12, 4, 4],
        [0.12, 0.12, 4, 4],
        [0.12, 7, 0, 4],
        [0.12, 7, 7, 4]
    ]
    new_image3 = [
        [1, 1.2, 0.3, 0.3, 0, 0],
        [0, 0.3, 0.3, 0.3, 0, 0],
        [0, 0, 0.3, 0.3, 0, 0],
        [0, 0, 0.3, 0.3, 0, 0],
        [0, 0, 0.3, 0.3, 0, 0],
        [0, 0.3, 0.3, 0.3, 0.3, 0]
    ]
    compare(1, image2, new_image2)
    compare(2, image3, new_image3)

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)

    seq = "TCCGGATCCCGGGATGGA"
    compare(1, findAll(seq, "GG"), [3, 10, 11, 15])
    compare(2, findAll(seq, "TTTTA"), [])
    compare(3, findAll(seq, "TCC"), [0, 6])
    compare(4, findAll(seq, "C"), [1, 2, 7, 8, 9])

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)

    restrictionEnzymes = {
        'bamH1': ('GGATCC', 0),
        'ecoR1': ('GAATTC', 1),
        'sma1': ('CCCGGG', 2)
    }
    seq = "TCCGGATCCCGGGATGGA"

    compare(1, getFragments(seq, restrictionEnzymes, "bamH1"), ["TCC", "GGATCCCGGGATGGA"])
    compare(2, getFragments(seq, restrictionEnzymes, "sma1"), ["TCCGGATCC", "CGGGATGGA"])

def test_q3c():
    print('Testing Question 3C...')
    print('='*20)

    restrictionEnzymes2 = {
        'bamH1': ('GGATCC', 0),
        'sma1': ('CCCGGG', 2)
    }
    seq = "TCCGGATCCCGGGATGGA"

    compare("good enzyme", getGoodEnzyme(seq, restrictionEnzymes2), "bamH1")

def test_q3e():
    print('Testing Question 3E...')
    print('='*20)

    seq = "TCCGGATCCCGGGATGGA"

    compare(1, circularFindAll(seq, "GGATCC"), [3, 15])
    compare(2, circularFindAll(seq, "C"), [1, 2, 7, 8, 9])
    compare(3, circularFindAll(seq, "ATCC"), [5, 17])

def test_q3f():
    print('Testing Question 3F...')
    print('='*20)

    restrictionEnzymes = {
        'bamH1': ('GGATCC', 0),
        'ecoR1': ('GAATTC', 1),
        'sma1': ('CCCGGG', 2)
    }
    seq = "TCCGGATCCCGGGATGGA"

    compare(1, getCircularFragments(seq, restrictionEnzymes, "bamH1"), ["GGATCCCGGGAT", "GGATCC"])
    compare(2, getCircularFragments(seq, restrictionEnzymes, "sma1"), ["CGGGATGGATCCGGATCC"])

def test_q4ab():
    print('Testing Question 4AB...')
    print('='*20)
    
    T1 = Development()
    T2 = Testing()
    try:
        compare(1, T1.canSpend(3000), True)
        compare(2, T2.canSpend(2050), False)
    except:
        compare("canSpend", "still have to implement a function correctly :)", "no error")

test_q2a()
test_q2b()
test_q2c()
test_q2d()
test_q2e()
test_q2f()
test_q3a()
test_q3b()
test_q3c()
test_q3e()
test_q3f()
test_q4ab()
