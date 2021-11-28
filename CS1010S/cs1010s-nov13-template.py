## CS1010S Nov13 Template

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
def f1(seq):
    pass # remove this line

## Question 2B
def f2(seq):
    pass # remove this line

## Question 2C
def f3(seq):
    pass # remove this line

## Question 2D
def f4(seq):
    pass # remove this line

## Question 2E
def f5(seq):
    pass # remove this line

## Question 3A
def count_change(amount, coins):
    pass # remove this line

## Question 3B
def count_change_limited(amount, coins):
    pass # remove this line

## Question 3C
"""
Answer here.
"""

## Question 3D
"""
Answer here.
"""

## Question 4A
"""
Answer here.
"""

## Question 4B
class SparseMatrix:
    def __init__(self,seq):
        self.data = [len(seq),len(seq[0]),[]]
        for i in range(len(seq)):
            for j in range(len(seq[0])):
                if seq[i][j] != 0:
                    self.data[2].append([i,j,seq[i][j]])

    def rows(self): # Returns the number of rows
        pass # <T1>

    def cols(self): # Returns the number of columns
        pass # <T2>

    def get(self,x,y):
        for record in self.data[2]:
            if record[0] == x and record[1] == y:
                return record[2]
        return 0

    def set(self,x,y,val):
        for record in self.data[2]:
            if record[0] == x and record[1] == y:
                record[2]=val
                return
        self.data[2].append([x,y,val])

    def transpose(self):
        for record in self.data[2]:
            record[0],record[1]=record[1],record[0]
        self.data[0],self.data[1]=self.data[1],self.data[0]

    def get_data(self): # Returns a list of lists representing the matrix data according to input format.
        pass # <T3>

## Question 4C
class DenseMatrix:
    def __init__(self,seq):
        self.data = ()
        for row in seq:
            self.data += (tuple(row),)

    def rows(self):
        return len(self.data)

    def cols(self):
        return len(self.data[0])

    def get(self,x,y):
        return self.data[x][y]

    def set(self,x,y,val): # Sets the value at (x,y) to val
        pass # <T4>

    def transpose(self): # transposes this matrix
        pass # <T5>

    def get_data(self):
        return self.data

## Question 5A
"""
Answer here.
"""

## Question 5B
class Matrix:
    def __init__(self,seq):
        def choose_sparse(seq):
            pass # <T6>
        
        if choose_sparse(seq):
            self.mat = SparseMatrix(seq)
        else:
            self.mat = DenseMatrix(seq)

    def rows(self):
        return self.mat.rows()

    def cols(self):
        return self.mat.cols()

    def get(self,x,y):
        return self.mat.get(x,y)

    def set(self,x,y,val):
        self.mat.set(x,y,val)

    def transpose(self):
        self.mat.transpose()

    def get_data(self):
        return self.mat.get_data()
    
## Question 5C
    def convert(self): # swap internal representation
        pass # <T7>

## Question 5D
"""
Answer here.
"""

## Appendix
def cc(amount, kinds_of_coins):
    if amount == 0:
        return 1
    elif amount < 0 or kinds_of_coins == 0:
        return 0
    else:
        return cc(amount, kinds_of_coins-1) + cc(amount - first_denomination(kinds_of_coins), kinds_of_coins)

def first_denomination(kinds_of_coins):
    if kinds_of_coins == 1:
        return 1
    elif kinds_of_coins == 2:
        return 5
    elif kinds_of_coins == 3:
        return 10
    elif kinds_of_coins == 4:
        return 20
    elif kinds_of_coins == 5:
        return 50

# Dense Matrix
def make_matrix(seq):
    mat = []
    for row in seq:
        mat.append(list(row))
    return mat

def rows(mat):
    return len(mat)

def cols(mat):
    return len(mat[0])

def get(mat,x,y):
    return mat[x][y]

def set(mat,x,y,val):
    mat[x][y] = val

def transpose(mat):
    transposed = []
    for i in range(len(mat[0])):
        column = []
        for j in range(len(mat)):
            column.append(mat[j][i])
        transposed.append(column)
    mat.clear()
    for row in transposed:
        mat.append(row)
    return mat

def print_matrix(mat):
    for row in mat:
        print(row)

# Sparse Matrix
def make_matrix(seq):
    data = []
    for i in range(len(seq)):
        for j in range(len(seq[0])):
            if seq[i][j] != 0:
                data.append([i,j,seq[i][j]])
    return [len(seq),len(seq[0]),data]

def rows(mat):
    return mat[0]

def cols(mat):
    return mat[1]

def get(mat,x,y):
    for record in mat[2]:
        if record[0] == x and record[1] == y:
            return record[2]
    return 0

def set(mat,x,y,val):
    for record in mat[2]:
        if record[0] == x and record[1] == y:
            record[2]=val
            return
    mat[2].append([x,y,val])

def transpose(mat):
    for record in mat[2]:
        record[0],record[1]=record[1],record[0]
    mat[0],mat[1]=mat[1],mat[0]
    return mat

def print_matrix(mat):
    temp = []
    zeros = [0]*mat[1]
    for row in range(mat[0]):
        temp.append(list(zeros))
    for record in mat[2]:
        temp[record[0]][record[1]] = record[2]
    for row in temp:
        print(row)

## Test Cases
def compare(number,got,expected):
    if got == expected:
        print(f'Test {number} : Passed!')
    else:
        print(f'Test {number} : Failed!')
        print(f'Expected {expected}, got {got}')
    print()

# Pro tip : drag all the lines that you want to comment/uncomment and press Alt+3/4

a = [1,2,3,4,5,6,7,8,9,10]
b = [10,9,8,7,6,5,4,3,2,1]
c = [1,0,1,0,1,0,2,0,2,0]
d = [5,1,1,1,5]
e = [-1,1,-2,2,-1,1]

def test_q2a():
    print('Testing Question 2A...')
    print('='*20)
    compare(1,f1(a),[1, 2, 3, 4, 100, 6, 7, 8, 9, 10])
    compare(2,f1(b),[10, 9, 8, 7, 6, 100, 4, 3, 2, 1])
    compare(3,f1(c),[1, 0, 1, 0, 1, 0, 2, 0, 2, 0])
    compare(4,f1(d),[100, 1, 1, 1, 100])
    compare(5,f1(e),[-1, 1, -2, 2, -1, 1])

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    compare(1,f2(a),[2, 4, 100, 6, 8, 10])
    compare(2,f2(b),[10, 8, 6, 100, 4, 2])
    compare(3,f2(c),[0, 0, 0, 2, 0, 2, 0])
    compare(4,f2(d),[100, 100])
    compare(5,f2(e),[-2, 2])

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    compare(1,f3(a),[4, 3, 2, 1])
    compare(2,f3(b),[4, 3, 2, 1])
    compare(3,f3(c),[2, 2, 1, 1, 1, 0, 0, 0, 0, 0])
    compare(4,f3(d),[1, 1, 1])
    compare(5,f3(e),[2, 1, 1, -1, -1, -2])

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)
    compare(1,f4(a),[4, 3, 2, 1])
    compare(2,f4(b),[4, 3, 2, 1])
    compare(3,f4(c),[2, 1, 0])
    compare(4,f4(d),[1])
    compare(5,f4(e),[2, 1, -1, -2])

def test_q2e():
    print('Testing Question 2E...')
    print('='*20)
    compare(1,f5(a),[1, 3, 5, 7, 9])
    compare(2,f5(b),[10, 8, 6, 4, 2])
    compare(3,f5(c),[1, 1, 1, 2, 2])
    compare(4,f5(d),[5, 1, 5])
    compare(5,f5(e),[-1, -2, -1])

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    compare(1,count_change(100,[1,5,10,20,50]),343)
    compare(2,count_change(10,[1,5]),3)
    compare(3,count_change(13,[1]),1)
    compare(4,count_change(10,[1,5,10]),4)
    compare(5,count_change(1,[5]),0)
    compare(6,count_change(20,[1,10]),3)
    compare(7,count_change(5,[1,5]),2)

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)
    compare(1,count_change_limited(100,{1:30,5:20,10:5,20:10,50:1}),203)
    compare(2,count_change_limited(10,{1:10,5:10}),3)
    compare(3,count_change_limited(13,{1:100}),1)
    compare(4,count_change_limited(10,{}),0)
    compare(5,count_change_limited(10,{1:5,5:1}),1)
    compare(6,count_change_limited(10,{1:5,5:2}),2)
    compare(7,count_change_limited(10,{1:10,5:3}),3)
    
test_q2a()
test_q2b()
test_q2c()
test_q2d()
test_q2e()
test_q3a()
test_q3b()
