#!/usr/bin/env python3
## CS1010S Nov17 Template

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
def make_grid(rows, cols):
    row = [None]*cols
    grid = []
    for _ in range(rows):
        grid.append(row.copy())

    return grid

## Question 2B
def drop(grid, col, token):
    check = list(map(lambda x:x[col],grid))
    if check[0] != None:
        raise ColumnFullError(col)
    else:
        pos = 0
        while pos < len(check) and check[pos] == None:
            pos += 1
        grid[pos-1][col] = token
        # set(grid, pos-1, col, token)

## Question 2C
def check_rows(grid): # provided
    for row in grid:
        t = check_row(row) # check individual row
    if t:
        return t
    return False

def check_row(row):
    cons = 0
    pos = row[0]
    for i in range(len(row)):
        if row[i] == pos:
            cons += 1
        else:
            pos = row[i]
            cons = 0
        if cons == 4:
            return True
    return False

## Question 2D
def deep_map(f, lst):
    for i in range(len(lst)):
        if type(lst[i]) != list:
            lst[i] = f(lst[i])
        else:
            deep_map(f,lst[i])

## Question 2E
def skew(grid):
    row = len(grid)
    col = len(grid[0])
    diag = diagonal(2*row,col,-row,0)
    deep_map(lambda x:grid[x[0]][x[1]] if x[0] in range(row) and x[1] in range(col) else None,diag)
    return diag

## Question 2F
def winner(grid): # provided
    t1 = check_rows(grid)
    rotate(grid) # swap cols to rows
    t2 = check_rows(grid)
    r = skew(grid) # get a skewed representation
    t3 = check_rows(r)
    rotate(r) # swap cols to rows
    t4 = check_rows(r)
    return t1 or t2 or t3 or t4 # return token if any is not False
"""
Answer here.
"""

## Question 3A
def make_container(): # pre-defined
    return {}

def add_item(container, item, weight):
    container[item] = container.get(item,0) + weight

def remove_item(container, item, weight):
    container[item] = max(0,container.get(item)-weight)
    if container[item] == 0:
        del container[item]

def get_items(container):
    return tuple(container.keys())

def get_weight(container):
    return sum(tuple(container.values()))
    
## Question 3B
def transfer_items(container, *containers):
    for c in containers:
        items = list(c.keys())
        for item in items:
            add_item(container,item,c[item])
            remove_item(c,item,c[item])

## Question 3C
"""
Answer here.
"""

## Question 3D
"""
Answer here.
"""

## Question 3E
def lock(container, passcode): # modify the following function
    container = lambda x: container if x == passcode else False
##    c = container.copy()
##    container.clear()
##    container['locked'] = lambda x: c if x == passcode else False

def unlock(container, passcode): # modify the following function
    if container(passcode):
        container = container(passcode)
##    c = container['locked'](passcode)
##    if c != False:
##        container.clear()
##        container.update(c)

## Provided for Question 4, modify if necessary
class Airplane:
    def __init__(self, weight, mtow):
        self.weight = weight
        self.mtow = mtow

    def get_weight(self):
        return self.weight

    def take_off(self):
        if self.weight > self.mtow:
            return 'Too heavy to take off'
        else:
            return 'Ok to take off'

class PassengerPlane(Airplane):
    def __init__(self, weight, mtow):
        super().__init__(weight, mtow)
        self.passengers = 0

    def get_weight(self):
        return self.passengers * 100 + self.weight

## Question 4A
"""
Answer here.
"""

## Question 4B
"""
Answer here.
"""

## Question 4C
class Cargo: # pre-made
    def __init__(self,weight):
        self.weight = weight

class CargoPlane(Airplane):
    def __init__(self,weight,mtow):
        super().__init__(weight,mtow)
        self.cargos = []

    def get_weight(self):
        return sum(list(map(lambda x:x.weight,self.cargos))) + super().get_weight()

## Question 4D
class PassengerCargoPlane(PassengerPlane, CargoPlane):
    pass
"""
Answer here.
"""

## Test Cases
def compare(number,got,expected):
    if got == expected:
        print(f'Test {number} : Passed!')
    else:
        print(f'Test {number} : Failed!')
        print(f'Expected {expected}, got {got}')
    print()

# The following functions have been available to use, I just need to redefine it here to prevent error
def rows(m):
    return len(m)

def cols(m):
    return len(m[0])

def get(m, row, col):
    return m[row][col]

def set(m, row, col, val):
    m[row][col] = val

def transpose(m):
    for i in range(len(m)):
        for j in range(i):
            m[i][j], m[j][i] = m[j][i], m[i][j]

def rotate(m): # my version
    rotated = list(map(lambda x:list(x)[::-1],zip(*m)))
    m.clear()
    for row in rotated:
        m.append(row)

class ColumnFullError(Exception):
    def __init__(self, col):
        self.col = col
        self.message = 'Column '+str(self.col)+' is already filled to top.'

    def __str__(self):
        return self.message

def diagonal(height, width, i, j): # my version
    return [[(i+height-1-x+y,y+j) for y in range(width)] for x in range(height)]

# Pro tip : drag all the lines that you want to comment/uncomment and press Alt+3/4

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)
    print('diagonal(6, 4, -3, 0) = [')
    for row in diagonal(6, 4, -3, 0):
        print(row, end =',\n')
    print(']\n')
    l = [1, 2, [3, 4], [5, 6, [7]]]
    deep_map(lambda x: x*2, l)
    compare('deep map',l,[2, 4, [6, 8], [10, 12, [14]]])

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    c = make_container()
    add_item(c, 'bananas', 5)
    add_item(c, 'apples', 3)
    add_item(c, 'bananas', 5)
    compare(1,c,{'bananas': 10, 'apples': 3})
    compare(2,get_items(c),('bananas', 'apples'))
    compare(3,get_weight(c),13)

    remove_item(c, 'bananas', 3)
    compare(4,c,{'bananas': 7, 'apples': 3})

    remove_item(c, 'bananas', 10)
    compare(5,get_items(c),('apples',))
    compare(6,get_weight(c),3)

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)
    c1 = {"bananas": 5, "apples": 3}
    c2 = {"bananas": 2, "oranges": 7}
    c3 = {"apples": 6, "pears": 4}
    transfer_items(c1, c2, c3)

    compare(1,c1,{'bananas': 7, 'apples': 9, 'oranges': 7, 'pears': 4})
    compare(2,get_weight(c2),0)
    compare(3,get_weight(c3),0)
    
def test_q3e():
    print('Testing Question 3E...')
    print('='*20)
    c = {"bananas": 10, "oranges": 5}
    lock(c,12345)
    if c == {"bananas": 10, "oranges": 5}:
        print('Test lock failed!\nIt should be locked :(\n')
    else:
        print('Test lock passed!\nPretty sure it is locked!\n')
    try:
        unlock(c,12344)
        if c == {"bananas": 10, "oranges": 5}:
            print('Test unlock 1 failed!\nIt should be still locked :(\n')
        else:
            print('Test unlock 1 passed!\nPretty sure it is still locked!\n')
        unlock(c,12345)
        if c == {"bananas": 10, "oranges": 5}:
            print('Test unlock 2 passed!\nPretty sure it is already unlocked!\n')
        else:
            print('Test unlock 2 failed!\nIt should be still locked :(\n')
    except:
        print('Pretty sure you have not modified the lock and unlock function properly.\n')
    
test_q2d()
test_q3a()
test_q3b()
test_q3e()
