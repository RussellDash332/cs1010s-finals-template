## CS1010A Nov23 Template

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


## Provided for Question 2, do not assume implementation!
class Queue:
    def __init__(self, *items): self.q = [*items]
    def enqueue(self, item): self.q.append(item)
    def dequeue(self): return self.q.pop(0)
    def head(self): return self.q[0]
    def size(self): return len(self.q)
    def empty(self): return not bool(self.q)

## Question 2A
def concat(q1, q2):
    pass # remove this line

## Question 2B
def merge(q1, q2):
    pass # remove this line

## Question 2C
def merge_all(*qs):
    pass # remove this line

## Question 2D
"""
Answer here.
"""

## Question 2E
def dequeue_nested(q):
    pass # remove this line

## Question 2F
def dequeue_deep(q):
    pass # remove this line


## Provided for Question 3, do not modify!
class Game:
    def __init__(self, size=None, players=None, jumps=None, seed=None):
        import random
        if size == players == jumps == None:
            if seed == None: random.seed(42) # the way of life!
            else: random.seed(seed)
            size = random.randint(11, 39)
            players = random.randint(2, 5)
            jumps = {random.randint(2, size): random.randint(2, size) for _ in range(random.randint(3, 5))}
        self.players = tuple([1] for _ in range(players))
        self.jumps = jumps
        self.size = size

## Question 3A
def valid_jumps(jumps):
    pass # remove this line

## Question 3B
def move_player(game, player, dice):
    pass # remove this line

## Question 3C
def num_jumps(game, player):
    pass # remove this line

## Question 3D
def make_jumps(seq):
    pass # remove this line

## Question 3E
"""
Answer here.
game.jumps[22] = <??>
"""


## Provided for Question 4, feel free to modify.
class ForceUser:
    pass

class Jedi:
    def __init__(self, name):
        self.name = name
        self.powers = ['jump', 'push', 'heal', 'mind trick']

    def use(self, force):
        if force in self.powers:
            print(self.name, 'uses Force', force)
        else:
            print(self.name, 'cannot use Force', force)

class Sith:
    def __init__(self, name):
        self.name = 'Darth ' + name
        self.powers = ['jump', 'push', 'lightning', 'choke']

    def use(self, force):
        if force in self.powers:
            print(self.name, 'uses Force', force)
        else:
            print(self.name, 'cannot use Force', force)

## Question 4A
"""
Answer here.
"""

## Question 4B
"""
Answer here and/or modify the class ForceUser above.
"""

## Question 4C
"""
Answer here and/or modify the class Jedi above.
"""

## Question 4D
"""
Answer here and/or modify the class Sith above.
"""

## For Question 4E
class JediTurnSith(Jedi, Sith):
    pass

## Question 4E
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
    
    try:
        q = concat(Queue(1, 2, 3), Queue(4, 5, 6))
        compare(1, [q.dequeue() for _ in range(6)], [1, 2, 3, 4, 5, 6])
        q = concat(Queue(1, 2, 3, 4, 5, 6), Queue())
        compare(2, [q.dequeue() for _ in range(6)], [1, 2, 3, 4, 5, 6])
    except Exception as e:
        compare('concat', f'{type(e).__name__}: {str(e)}', 'implement concat properly first!')

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    
    try:
        q = merge(Queue(1, 2, 3), Queue(4, 5, 6))
        compare(1, [q.dequeue() for _ in range(6)], [1, 4, 2, 5, 3, 6])
        q = merge(Queue(5), Queue(12))
        compare(2, [q.dequeue() for _ in range(2)], [5, 12])
        q = merge(Queue(1, 3, 5, 7, 9, 11), Queue(2, 4, 6, 8, 10, 12))
        compare(3, [q.dequeue() for _ in range(12)], [*range(1, 13)])
    except Exception as e:
        compare('merge', f'{type(e).__name__}: {str(e)}', 'implement merge properly first!')

def test_q2cd():
    print('Testing Question 2CD...')
    print('='*20)
    
    try:
        q = merge_all(Queue(1, 2, 3), Queue(4, 5), Queue(6, 7, 8, 9))
        compare(1, [q.dequeue() for _ in range(9)], [1, 4, 6, 2, 5, 7, 3, 8, 9])
        q = merge_all(Queue(5), Queue(12, 13), Queue(), Queue(), Queue(14))
        compare(2, [q.dequeue() for _ in range(4)], [5, 12, 14, 13])
        q = merge_all(Queue(1, 3, 5, 7, 9, 11, 13), Queue(2, 4, 6, 8, 10, 12))
        compare(3, [q.dequeue() for _ in range(13)], [*range(1, 14)])
        q1, q2 = Queue(1, 2, 3, 4), Queue(5, 6, 7)
        q = merge_all(q1, q2, q1); s = []
        #while not q.empty(): s.append(q.dequeue())
        #print(s)
    except Exception as e:
        compare('merge_all', f'{type(e).__name__}: {str(e)}', 'implement merge_all properly first!')

def test_q2e():
    print('Testing Question 2E...')
    print('='*20)
    
    try:
        q = Queue(1, 2, 3, 4)
        q.enqueue(Queue(5, 6, 7)), q.enqueue(8), q.enqueue(Queue(9, 10))
        compare(1, [dequeue_nested(q) for _ in range(10)], [*range(1, 11)])
        q = Queue()
        q.enqueue(Queue()), q.enqueue(1), q.enqueue(Queue(2, 3)), q.enqueue(Queue(4))
        q.enqueue(5), q.enqueue(Queue()), q.enqueue(6)
        compare(2, [dequeue_nested(q) for _ in range(6)], [*range(1, 7)])
    except Exception as e:
        compare('dequeue_nested', f'{type(e).__name__}: {str(e)}', 'implement dequeue_nested properly first!')

def test_q2f():
    print('Testing Question 2F...')
    print('='*20)
    
    try:
        # [1, 2, [3, 4, [5, 6]], 7]
        q1, q2, q3 = Queue(1, 2), Queue(3, 4), Queue(5, 6)
        q2.enqueue(q3)
        q1.enqueue(q2)
        q1.enqueue(7)
        compare(1, [dequeue_deep(q1) for _ in range(7)], [*range(1, 8)])
        
        # [[[1], [[2]]], 3]
        a, b, c, d, e = Queue(), Queue(), Queue(), Queue(), Queue()
        b.enqueue(1), e.enqueue(2), c.enqueue(e), a.enqueue(b), a.enqueue(c), d.enqueue(a), d.enqueue(3)
        compare(2, [dequeue_deep(d) for _ in range(3)], [1, 2, 3])
        
        # [[[[3]]]]
        a, b, c, d = Queue(), Queue(), Queue(), Queue()
        a.enqueue(b), b.enqueue(c), c.enqueue(d), d.enqueue(3)
        compare(3, dequeue_deep(a), 3)

        # [[[], []], 3]
        a, b, c, d = Queue(), Queue(), Queue(), Queue()
        b.enqueue(c), b.enqueue(d), a.enqueue(b), a.enqueue(3)
        compare(4, dequeue_deep(a), 3)

        # [[], [], 3]
        a, b, c = Queue(), Queue(), Queue()
        a.enqueue(b), a.enqueue(c), a.enqueue(3)
        compare(5, dequeue_deep(a), 3)
    except Exception as e:
        compare('dequeue_deep', f'{type(e).__name__}: {str(e)}', 'implement dequeue_deep properly first!')

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    
    compare(1, valid_jumps(Game().jumps), False)
    compare(2, valid_jumps(Game(seed=2).jumps), True)
    compare(3, valid_jumps({}), True)
    compare(4, valid_jumps(Game(seed=4).jumps), False)
    compare(5, valid_jumps({1: 2}), True)
    compare(6, valid_jumps({1: 2, 3: 5}), True)

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)
    
    g = Game(seed=2) # size is 38
    move_player(g, 0, 5), move_player(g, 1, 6)
    compare(1, g.players, ([1, 6], [1, 7, 25]))
    move_player(g, 0, 6)
    compare(2, g.players, ([1, 6, 12, 21], [1, 7, 25]))
    move_player(g, 1, 13)
    compare(3, g.players, ([1, 6, 12, 21], [1, 7, 25, 38]))
    move_player(g, 1, 2)
    compare(4, g.players, ([1, 6, 12, 21], [1, 7, 25, 38]))
    g = Game(seed=2)
    move_player(g, 1, 17)
    compare(5, g.players, ([1], [1, 18, 15]))
    move_player(g, 1, 3)
    compare(6, g.players, ([1], [1, 18, 15, 18, 15]))

def test_q3c():
    print('Testing Question 3C...')
    print('='*20)
    
    g = Game(seed=22) # size is 15
    g.jumps[14] = 15
    compare(1, num_jumps(g, 1), 0)
    for i in range(3): move_player(g, i, i+1) # 1, 2, 3
    for i in range(3): move_player(g, i, 9-i) # 9, 8, 7
    for i in range(3): move_player(g, i, i+5) # 5, 6, 7
    for i in range(3): move_player(g, i, 2)   # 2, 2, 2
    compare(2, num_jumps(g, 0), 2) # 1 -> 2 -> 11 -> 9 -> 14 -> 15
    compare(3, num_jumps(g, 1), 1) # 1 -> 3 -> 13 -> 15
    compare(4, num_jumps(g, 2), 1) # 1 -> 4 -> 13 -> 15

def test_q3d():
    print('Testing Question 3D...')
    print('='*20)
    
    compare(1, make_jumps([1, 7, 3, 4, 5, 3, 7, 8]), {2: 7, 6: 3})
    compare(2, make_jumps([1, 2, 3, 4, 5, 6, 7, 8]), {})
    compare(3, make_jumps([9, 9, 9, 9, 9, 9, 9, 9, 9]), {k:9 for k in range(1, 9)})

def test_q4d():
    global print
    outputs = []
    old_print = print
    print = lambda *args: outputs.append(' '.join(args))
    old_print('Testing Question 4D...')
    old_print('='*20)
    try:
        # sample
        emperor = Sith('Sidious', 'Palpatine')
        compare(1, emperor.name, 'Palpatine')
        old_print('\n'.join(outputs)), outputs.clear()
        emperor.use('choke')
        compare(2, outputs.pop(), 'Darth Sidious uses Force choke')
        old_print('\n'.join(outputs)), outputs.clear()
        compare(3, emperor.name, 'Palpatine')
        old_print('\n'.join(outputs)), outputs.clear()
        
        # behold yours truly!
        me = Sith('Fennel', 'Russell')
        compare(4, me.name, 'Russell')
        old_print('\n'.join(outputs)), outputs.clear()
        me.use('jump')
        compare(5, outputs.pop(), 'Darth Fennel uses Force jump')
        old_print('\n'.join(outputs)), outputs.clear()
        me.use('push')
        compare(6, outputs.pop(), 'Darth Fennel uses Force push')
        old_print('\n'.join(outputs)), outputs.clear()
        me.use('mind trick')
        compare(7, outputs.pop(), 'Darth Fennel cannot use Force mind trick')
        old_print('\n'.join(outputs)), outputs.clear()
        me.use('lightning')
        compare(8, outputs.pop(), 'Darth Fennel uses Force lightning')
        old_print('\n'.join(outputs)), outputs.clear()
        me.use('heal')
        compare(9, outputs.pop(), 'Darth Fennel cannot use Force heal')
        old_print('\n'.join(outputs)), outputs.clear()
        compare(10, me.name, 'Russell')
        old_print('\n'.join(outputs)), outputs.clear()
        compare(11, isinstance(me, ForceUser), True)
        old_print('\n'.join(outputs)), outputs.clear()
    except Exception as e:
        compare('Sith', f'{type(e).__name__}: {str(e)}', 'implement Sith properly first!')
        old_print('\n'.join(outputs))
    finally:
        outputs.clear()
        print = old_print


test_q2a()
test_q2b()
test_q2cd()
test_q2e()
test_q2f()
test_q3a()
test_q3b()
test_q3c()
test_q3d()
test_q4d()
