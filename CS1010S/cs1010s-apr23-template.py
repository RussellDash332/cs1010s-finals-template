## CS1010S Apr23 Template

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
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

## Question 2A
def make_sq_matrix(n, value):
    return [[value] * n] * n # fix this!

## Question 2B
def swap_rowcol(m1, row, m2, col):
    pass # remove this line

## Question 2C
def flip_rowcol(m1, row, m2, col):
    pass # remove this line

## Question 2D
def rotate_ccw(m):
    pass # remove this line

## Question 2E
def rotate_front_ccw(top, left, front, right, back, bottom):
    pass # remove this line


## Provided for Question 3
from datetime import datetime as dt
get_today = lambda: '29-04-2023'
def days_between(a, b):
    a = dt.strptime(a, '%d-%m-%Y')
    b = dt.strptime(b, '%d-%m-%Y')
    return abs(a-b).days
make_book = lambda a, b: lambda x: a if x else b
get_name = lambda b: b(1)
get_ncopies = lambda b: b(0)
book1 = make_book('Harry Potter', 5)
book2 = make_book('Twilight', 1)
book3 = make_book('The Firm', 2)
DoI = get_today()

## Question 3A
def is_available(ledger, book):
    pass # remove this line

## Question 3B
def borrow_book(ledger, borrower, book):
    pass # remove this line

## Question 3C
def return_book(ledger, borrower, book):
    pass # remove this line

## Question 3D
def inverse_ledger(ledger):
    pass # remove this line

## Question 3E
"""
Answer here.
"""


## Provided for Question 4, feel free to modify.
class NUSStaff:
    def __init__(self, name):
        self.name = name
        self.base_salary = 3000

    def get_base(self):
        return self.base_salary

class AcadStaff(NUSStaff):
    def __init__(self, name, modules):
        self.modules = modules

    def topup(self):
        return len(self.modules) * 2000

class AdminStaff(NUSStaff):
    def __init__(self, name):
        self.role = None

    def change_role(self, role):
        self.role = role

    def topup(self):
        return role.allowance if role else 0

Module = str
cs1010s = Module('CS1010S')
ashish = AcadStaff("Ashish", [cs1010s])
linda = AdminStaff("Linda")
john = NUSStaff("John")

## Question 4A
"""
Answer here and modify the classes above.
"""

class Role:
    def __init__(self, name):
        self.allowance = 0
class AcadAdminStaff(AcadStaff, AdminStaff):
    pass

## Question 4B
"""
Answer here and modify the classes above.
"""

## Question 4C
"""
Answer here.
"""

## Question 4D
"""
Answer here and modify the classes above.
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
    
    face = make_sq_matrix(3, 1)
    compare(1, face, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    face[1][2] = -1000
    face[0][0] = 1001
    compare(2, face, [[1001, 1, 1], [1, 1, -1000], [1, 1, 1]])
    face2 = make_sq_matrix(2, 2)
    compare(3, face2, [[2, 2], [2, 2]])
    compare(4, face2[0] is face2[1], False)

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    swap_rowcol(m1, 0, m2, 1)
    compare(1, m1, [['b', 'e', 'h'], [4, 5, 6], [7, 8, 9]])
    compare(2, m2, [['a', 1, 'c'], ['d', 2, 'f'], ['g', 3, 'i']])
    swap_rowcol(m2, 2, m1, -2)
    compare(3, m1, [['b', 'g', 'h'], [4, 3, 6], [7, 'i', 9]])
    compare(4, m2, [['a', 1, 'c'], ['d', 2, 'f'], ['e', 5, 8]])
    m3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    m4 = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]
    swap_rowcol(m3, 1, m4, 3)
    compare(5, m3, [[1, 2, 3, 4], ['d', 'h', 'l', 'p'], [9, 10, 11, 12], [13, 14, 15, 16]])
    compare(6, m4, [['a', 'b', 'c', 5], ['e', 'f', 'g', 6], ['i', 'j', 'k', 7], ['m', 'n', 'o', 8]])

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    flip_rowcol(m1, 0, m2, 1)
    compare(1, m1, [['h', 'e', 'b'], [4, 5, 6], [7, 8, 9]])
    compare(2, m2, [['a', 3, 'c'], ['d', 2, 'f'], ['g', 1, 'i']])
    flip_rowcol(m2, 2, m1, -2)
    compare(3, m1, [['h', 'i', 'b'], [4, 1, 6], [7, 'g', 9]])
    compare(4, m2, [['a', 3, 'c'], ['d', 2, 'f'], [8, 5, 'e']])
    m3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    m4 = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]
    flip_rowcol(m3, 1, m4, 3)
    compare(5, m3, [[1, 2, 3, 4], ['p', 'l', 'h', 'd'], [9, 10, 11, 12], [13, 14, 15, 16]])
    compare(6, m4, [['a', 'b', 'c', 8], ['e', 'f', 'g', 7], ['i', 'j', 'k', 6], ['m', 'n', 'o', 5]])

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    m3 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    m4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotate_ccw(m1)
    rotate_ccw(m2)
    compare(1, m1, [[3, 6, 9], [2, 5, 8], [1, 4, 7]])
    compare(2, m2 == m3, False)
    for _ in range(3): rotate_ccw(m2)
    compare(3, m2, m3)
    rotate_ccw(m4)
    compare(4, m4, [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]])
    rotate_ccw(m4)
    compare(5, m4, [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]])

def test_q2e():
    print('Testing Question 2E...')
    print('='*20)

    front = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    top = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
    left = [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
    right = [[28, 29, 30], [31, 32, 33], [34, 35, 36]]
    back = [[37, 38, 39], [40, 41, 42], [43, 44, 45]]
    bottom = [[46, 47, 48], [49, 50, 51], [52, 53, 54]]

    small_front = [[2*i+j for j in range(2)] for i in range(2)]
    small_top = [[2*i+j+4 for j in range(2)] for i in range(2)]
    small_left = [[2*i+j+8 for j in range(2)] for i in range(2)]
    small_right = [[2*i+j+12 for j in range(2)] for i in range(2)]
    small_back = [[2*i+j+16 for j in range(2)] for i in range(2)]
    small_bottom = [[2*i+j+20 for j in range(2)] for i in range(2)]

    rotate_front_ccw(top, left, front, right, back, bottom)
    compare(1, front, [[3, 6, 9], [2, 5, 8], [1, 4, 7]])
    compare(2, top, [[10, 11, 12], [13, 14, 15], [28, 31, 34]])
    compare(3, left, [[19, 20, 18], [22, 23, 17], [25, 26, 16]])
    compare(4, right, [[48, 29, 30], [47, 32, 33], [46, 35, 36]])
    compare(5, back, [[37, 38, 39], [40, 41, 42], [43, 44, 45]])
    compare(6, bottom, [[21, 24, 27], [49, 50, 51], [52, 53, 54]])

    rotate_front_ccw(small_top, small_left, small_front, small_right, small_back, small_bottom)
    compare(7, small_front, [[1, 3], [0, 2]])
    compare(8, small_top, [[4, 5], [12, 14]])
    compare(9, small_left, [[8, 7], [10, 6]])
    compare(10, small_right, [[21, 13], [20, 15]])
    compare(11, small_back, [[16, 17], [18, 19]])
    compare(12, small_bottom, [[9, 11], [22, 23]])

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)

    book1 = make_book('Harry Potter', 5)
    book2 = make_book('Twilight', 1)
    book3 = make_book('The Firm', 2)
    ledger = {
        book1: {'Nitya': '10-03-2023', 'Ashish': '12-03-2023'},
        book3: {'Nitya': '10-03-2023', 'WaiKay': '20-03-2023'}
    }
    compare(1, is_available(ledger, book3), False)
    compare(2, is_available(ledger, book1), True)
    compare(3, is_available(ledger, book2), True)

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)

    book1 = make_book('Harry Potter', 5)
    book2 = make_book('Twilight', 1)
    book3 = make_book('The Firm', 2)
    ledger = {
        book1: {'Nitya': '10-03-2023', 'Ashish': '12-03-2023'},
        book3: {'Nitya': '10-03-2023', 'WaiKay': '20-03-2023'}
    }
    borrow_book(ledger, 'Wayaki', book1)
    new_ledger = {
        book1: {'Nitya': '10-03-2023', 'Ashish': '12-03-2023', 'Wayaki': '29-04-2023'},
        book3: {'Nitya': '10-03-2023', 'WaiKay': '20-03-2023'}
    }
    compare(1, ledger, new_ledger)
    borrow_book(ledger, 'Ashish', book3)
    compare(2, ledger, new_ledger)

    borrow_book(ledger, 'Nitya', book2)
    new_ledger2 = {
        book1: {'Nitya': '10-03-2023', 'Ashish': '12-03-2023', 'Wayaki': '29-04-2023'},
        book3: {'Nitya': '10-03-2023', 'WaiKay': '20-03-2023'},
        book2: {'Nitya': '29-04-2023'}
    }
    compare(3, ledger, new_ledger2)

def test_q3c():
    print('Testing Question 3C...')
    print('='*20)

    book1 = make_book('Harry Potter', 5)
    book2 = make_book('Twilight', 1)
    book3 = make_book('The Firm', 2)
    ledger = {
        book1: {'Nitya': '10-03-2023', 'Ashish': '12-03-2023', 'Wayaki': '20-04-2023'},
        book3: {'Nitya': '10-03-2023', 'WaiKay': '20-03-2023'}
    }
    compare(1, return_book(ledger, 'Nitya', book1), True) # late
    compare(2, return_book(ledger, 'Wayaki', book1), True) # on time
    compare(3, return_book(ledger, 'Ashish', book3), False)

    new_ledger = {
        book1: {'Ashish': '12-03-2023'},
        book3: {'Nitya': '10-03-2023', 'WaiKay': '20-03-2023'}
    }
    compare(4, ledger, new_ledger)
    compare(5, return_book(ledger, 'Ashish', book1), True)
    compare(6, ledger, {book3: {'Nitya': '10-03-2023', 'WaiKay': '20-03-2023'}}) # need to remove key book1

def test_q3d():
    print('Testing Question 3D...')
    print('='*20)

    book1 = make_book('Harry Potter', 5)
    book2 = make_book('Twilight', 1)
    book3 = make_book('The Firm', 2)
    ledger = {
        book1: {'Nitya': '10-03-2023', 'Ashish': '12-03-2023'},
        book2: {'Nitya': '10-03-2023', 'WaiKay': '20-03-2023'}
    }
    inverted_ledger = {
        'Nitya' : {book1: '10-03-2023', book2: '10-03-2023'},
        'Ashish': {book1: '12-03-2023'},
        'WaiKay': {book2: '20-03-2023'},
    }
    compare('invert ledger', inverse_ledger(ledger), inverted_ledger)

def test_q4a():
    print('Testing Question 4A...')
    print('='*20)
    
    cs1010s = Module('CS1010S')
    ashish = AcadStaff("Ashish", [cs1010s])
    linda = AdminStaff("Linda")
    john = NUSStaff("John")
    try:
        ashish.get_base()
        linda.get_base()
        john.get_base()
        ashish.topup()
        linda.topup()
        john.topup()
        compare('fix error', True, True)
    except:
        compare('fix error', False, True)

def test_q4b():
    print('Testing Question 4B...')
    print('='*20)

    cs1010s = Module('CS1010S')
    ashish = AcadStaff("Ashish", [cs1010s])
    linda = AdminStaff("Linda")
    john = NUSStaff("John")
    try:
        compare(1, ashish.get_salary(), 5000)
        compare(2, john.get_salary(), 3000)
        compare(3, linda.get_salary(), 3000)

        hr = Role('HR')
        hr.allowance = 1000
        linda.change_role(hr)
        compare(4, linda.get_salary(), 4000)
    except:
        print('Failed! Implement get_salary() first!\n')

def test_q4d():
    print('Testing Question 4D...')
    print('='*20)

    cs1010s = Module('CS1010S')
    waikay = AcadAdminStaff("Waikay", [cs1010s])
    try:
        compare(1, waikay.get_salary(), 5000)
    except:
        compare(1, 'implement get_salary() first!', 5000)
    dos = Role('Vice-dean of Students')
    dos.allowance = 2000
    waikay.change_role(dos)
    try:
        compare(2, waikay.get_salary(), 7000)
    except:
        compare(2, 'implement get_salary() first!', 7000)

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
test_q4b()
test_q4d()
