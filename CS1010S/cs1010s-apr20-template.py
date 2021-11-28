## CS1010S Apr20 Template

## Question 1A
"""
Answer here.
"""

## Question 1B
"""
Answer here.
"""

seq = ((0, 2), (1, 5), (2, 4), (3, 6), (4, 0))
## Question 2A
def adjacent_viruses(seq, row, col):
    pass # remove this line

## Question 2B
def adjacent_grid(seq, height, width):
    pass # remove this line

## Question 2C
def safe_paths(grid):
    pass # remove this line

## Question 3A
def count_change(amt, denom):
    if amt < 0 or len(denom) == 0:
        return 0
    elif amt == 0:
        return 1
    else:
        return count_change(amt-denom[0], denom) \
               + count_change(amt, denom[1:])
"""
Answer here.
"""
    
## Question 3B
"""
Time :
Space :
"""

## Question 3C
def create_memo_cc():
    db = create_database()
    def memo_cc(amt, denom):
        if amt < 0 or len(denom) == 0:
            return 0
        elif amt == 0:
            return 1
        elif contains(db, amt, denom):
            return get(db, amt, denom)
        else:
            ans = count_change(amt-denom[0], denom) \
                  + count_change(amt, denom[1:])
            put(db, ans, amt, denom)
            return ans
    return memo_cc
"""
Answer here.
"""

## Question 3D
def create_database():
    pass # remove this line

def put(db, ans, amt, denom):
    pass # remove this line

def get(db, amt, denom):
    pass # remove this line

def contains(db, amt, denom):
    pass # remove this line

## Question 3E
count_change_memo = create_memo_cc()
# renamed to avoid overlapping with the previous count_change
"""
Time :
Space :
"""

## Question 3F
"""
Answer here.
"""

## Provided for Question 4
class Trooper:
    def __init__(self, *equipment):
        self.equipment = list(equipment)
        
    def load(self):
        return sum(map(lambda eq: eq[1], self.equipment))
    
    def speed(self):
        return 20 - (self.load() // 10)
    
class JumpJet(Trooper):
    def __init__(self, *equipment):
        super().__init__(('Jetpack', 20), *equipment)
        self.flying = False
        
    def toggle_jet(self):
        if not self.flying and self.load() > 100:
            print('Too heavy to fly')
        else:
            self.flying = not self.flying
            
    def speed(self):
        return super().speed() * (10 if self.flying else 1)

## Question 4A
"""
Answer here.
"""

## Question 4B
class Medic(Trooper):
    pass # remove this line

class JumpJetMedic(JumpJet, Medic):
    pass # no need to modify!

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
    compare(1,adjacent_viruses(seq,2,5),3)
    compare(2,adjacent_viruses(seq,1,5),2)
    compare(3,adjacent_viruses(seq,4,4),0)

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    compare('X',adjacent_grid(seq,6,7),((0, 1, 1, 1, 1, 1, 1),
                                        (0, 1, 1, 2, 2, 2, 1),
                                        (0, 0, 0, 1, 2, 3, 2),
                                        (1, 1, 0, 1, 1, 2, 1),
                                        (1, 1, 0, 0, 0, 1, 1),
                                        (1, 1, 0, 0, 0, 0, 0))
)

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    compare('safe paths',safe_paths(adjacent_grid(seq,6,7)),3
)
    compare('again',safe_paths(adjacent_grid(seq,10,13)),2211
)

def test_q3():
    print('Testing Question 3...')
    print('='*20)
    compare(0,count_change(100,[1,5,10,20,50]),343)
    compare(1,count_change_memo(100,[1,5,10,20,50]),343)

    print('#'*20+'\nTo genuinely pass the final test, you must pass ALL THE NINE test runs\n'+'#'*20+'\n')
    
    import time
    for i in range(2,11):
        a = time.time()
        r1 = count_change(100,[1,5,10,20,50])
        b = time.time()
        r2 = count_change_memo(100,[1,5,10,20,50])
        c = time.time()
        compare(str(i)+' (checking execution time)',c-b<b-a,True) # r2 must be executed faster than r1

def test_q4a():
    print('Testing Question 4A...')
    print('='*20)
    boba = JumpJet(('Rocket Launcher', 30))
    print(boba.speed())
    boba.toggle_jet()
    print(boba.speed())
    print()

def test_q4b():
    print('Testing Question 4B...')
    print('='*20)
    try:
        kix = JumpJetMedic(('Medikit',1))
        compare(1,kix.equipment,[('Stretcher', 10), ('Jetpack', 20), ('Medikit', 1)])
        compare(2,kix.speed(),17)
        
        kix.toggle_jet()
        compare(3,kix.speed(),170)
        kix.toggle_jet()

        rex = Trooper()
        rex.weight = 70
        kix.evacuate(rex)
        compare(4,kix.load(),101)

        compare(5,kix.equipment,[('Stretcher', 10), ('Jetpack', 20), ('Medikit', 1)])
        kix.toggle_jet()    # Too heavy to fly
        print()
    except Exception as e:
        print(e)
        print('Please implement Medic properly first!\n')

test_q2a()
test_q2b()
test_q2c()
test_q3()
test_q4a()
test_q4b()
