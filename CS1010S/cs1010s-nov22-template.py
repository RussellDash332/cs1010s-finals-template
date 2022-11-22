## CS1010S Nov22 Template

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
game = [[3, 7, 3, 0], [12, 0, 0, 3], [1, 0, 13, 7], [1, 4, 6]]
game2 = ([3, 7, 3, 0], [12, 0, 0, 3], [1, 0, 13, 7], [1, 4, 6])

## Question 2A
def new_game(num, pits, cnts):
    pass # remove this line

## Question 2B
def has_ended(game):
    pass # remove this line

## Question 2C
def next_pit(game, player, pit):
    pass # remove this line

## Question 2D
def distribute(game, player, pit):
    pass # remove this line

## Question 2E
def play_turn(game, player, pit):
    pass # remove this line

## Question 2F
"""
Answer here.
"""


## Provided for Question 3
# My own ADT, should be viable
class Product:
    def __init__(self, name):
        self.name = name
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        return isinstance(other, Product) and self.name == other.name
    def __repr__(self):
        return f'<Product \'{self.name}\'>'

class Category:
    def __init__(self, name):
        self.name = name
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        return isinstance(other, Category) and self.name == other.name
    def __repr__(self):
        return f'<Category \'{self.name}\'>'

def shelf_life(product):
    from collections import defaultdict
    dd = defaultdict(lambda: 100)
    dd.update({7: 10, 9: 90, 8: 70})
    return dd[len(product.name)]

def category(product):
    from collections import defaultdict
    dd = defaultdict(lambda: 'Others')
    dd.update({'HL Milk': 'Milk', 'Milo': 'Drink', 'Dutch Lady': 'Milk', 'Milo Plus': 'Drink'})
    return Category(dd[product.name])

inventory = {
    Product('HL Milk'): {90: 10, 92: 10},
    Product('Dutch Lady'): {91: 7, 94: 10},
    Product('Milo'): {87: 2, 92: 20}
}

catalog = {
    Category('Milk'): {
        Product('HL Milk'): {90: 10, 92: 10},
        Product('Dutch Lady'): {91: 7, 94: 10}
    },
    Category('Drink'): {
        Product('Milo'): {87: 2, 92: 20}
    }
}

## Question 3A
def stock_up(inv, products, today):
    pass # remove this line

## Question 3B
def clear_stock(inv, today):
    pass # remove this line

## Question 3C
def make_catalog(inv):
    pass # remove this line

## Question 3D
def count_stock(inv, cat, thing):
    pass # remove this line

## Question 3E
"""
Answer here.
"""


## Provided for Question 4, feel free to modify.
class Ship:
    def __init__(self, weight, full):
        self.weight = weight
        self.full = full

    def displacement(self):
        return self.weight

class CargoShip(Ship):
    def __init__(self, weight, full):
        super().__init__(weight, full)
        self.cargo = []

    def displacement(self):
        return sum(map(lambda x: x.weight(), self.cargo)) \
            + super().displacement()

    def load(self, item):
        self.cargo.append(item)

# Assume this is defined
class Overweight(Exception):
    def __str__(self):
        return 'Item is too heavy'

# For 4B onwards
class Tanker(CargoShip):
    def __init__(self, weight, full):
        self.tank = Tank()
        self.load(self.tank)
        super().__init__(weight, full)

    def load(self, amount):
        self.tank.add(amount)


## Question 4A
"""
Just modify the classes above.
"""

## Question 4B
"""
Just answer here and modify the classes above if necessary.
"""

## Question 4C
class Tank:
    pass

## Question 4D
class PassengerFerry: # fill the superclass if necessary
    pass

# DO NOT MODIFY THIS!
class RoPaxFerry(PassengerFerry, CargoShip):
    pass

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
    compare(1, new_game(1, 2, 3), [[3, 3], [0]])
    compare(2, new_game(4, 1, 10), [[10], [10], [10], [10], [0, 0, 0, 0]])
    game = new_game(2, 5, 7)
    try:
        compare(3, game[0] is game[1], False)
    except:
        compare(3, True, False)

def test_q2b():
    print('Testing Question 2B...')
    print('='*20)
    game = [[10], [10], [10], [10], [0, 0, 0, 0]]
    compare(1, has_ended(game), False)
    game = [[1], [1], [1], [1], [0, 0, 0, 0]]
    compare(1, has_ended(game), True)
    game = [[1, 0], [0, 1], [20, 20]]
    compare(3, has_ended(game), True)
    game = [[1, 0], [1, 1], [20, 20]]
    compare(4, has_ended(game), False)

def test_q2c():
    print('Testing Question 2C...')
    print('='*20)
    game = [[3, 7, 3, 0], [12, 0, 0, 3], [1, 0, 13, 7], [1, 4, 6]]
    compare(1, next_pit(game, 0, 3), (1, 0))
    compare(2, next_pit(game, 1, 2), (1, 3))
    compare(3, next_pit(game, 2, 3), (0, 0))
    compare(4, next_pit(game, 0, 1), (0, 2))
    compare(5, next_pit(game, 1, 3), (2, 0))

def test_q2d():
    print('Testing Question 2D...')
    print('='*20)
    game = [[3, 7, 3, 0], [12, 0, 0, 3], [1, 0, 13, 7], [1, 4, 6]]
    compare(1, distribute(game, 0, 1), (2, 1))
    compare(2, game, [[3, 0, 4, 1], [13, 1, 1, 4], [2, 0, 13, 7], [1, 4, 6]])
    compare(3, distribute(game, 1, 1), (1, 3))
    compare(4, game, [[3, 0, 4, 1], [13, 0, 2, 4], [2, 0, 13, 7], [1, 4, 6]])

def test_q2e():
    print('Testing Question 2E...')
    print('='*20)
    game = [[3, 7, 3, 0], [12, 0, 0, 3], [1, 0, 13, 7], [1, 4, 6]]
    play_turn(game, 1, 3)
    compare(1, game, [[4, 8, 4, 1], [13, 1, 1, 0], [0, 1, 14, 0], [1, 6, 6]])
    play_turn(game, 2, 1)
    compare(2, game, [[0, 8, 4, 1], [13, 1, 1, 0], [0, 0, 15, 0], [1, 6, 10]])

def test_q3a():
    print('Testing Question 3A...')
    print('='*20)
    inventory = {
        Product('HL Milk'): {90: 10, 92: 10},
        Product('Dutch Lady'): {91: 7, 94: 10},
        Product('Milo'): {87: 2, 92: 20}
    }
    inventory2 = {
        Product('HL Milk'): {90: 11, 92: 10},
        Product('Dutch Lady'): {91: 7, 94: 10},
        Product('Milo'): {87: 2, 92: 20}
    }
    inventory3 = {
        Product('HL Milk'): {90: 11, 92: 10, 93: 1},
        Product('Dutch Lady'): {91: 7, 93: 1, 94: 10},
        Product('Milo'): {87: 2, 92: 20, 93: 1}
    }
    inventory4 = {
        Product('HL Milk'): {90: 11, 92: 11, 93: 1},
        Product('Dutch Lady'): {91: 7, 93: 1, 94: 10},
        Product('Milo'): {87: 2, 92: 21, 93: 1}
    }
    inventory5 = {
        Product('HL Milk'): {90: 12, 92: 11, 93: 1},
        Product('Dutch Lady'): {91: 7, 93: 1, 94: 10},
        Product('Milo'): {87: 2, 92: 21, 93: 1},
        Product('Milo Plus'): {90: 1}
    }
    stock_up(inventory, [Product('HL Milk')], 90)
    compare(1, inventory, inventory2)
    stock_up(inventory, [Product('HL Milk'), Product('Dutch Lady'), Product('Milo')], 93)
    compare(2, inventory, inventory3)
    stock_up(inventory, [Product('HL Milk'), Product('Milo')], 92)
    compare(3, inventory, inventory4)
    stock_up(inventory, [Product('Milo Plus'), Product('Milo')], 90)
    compare(4, inventory, inventory5)

def test_q3b():
    print('Testing Question 3B...')
    print('='*20)
    inventory = {
        Product('HL Milk'): {90: 10, 92: 10},
        Product('Dutch Lady'): {91: 7, 94: 10},
        Product('Milo'): {87: 2, 92: 20}
    }
    clear_stock(inventory, 1000)
    compare(1, inventory, {
        Product('HL Milk'): {},
        Product('Dutch Lady'): {},
        Product('Milo'): {}
    })
    inventory = {
        Product('HL Milk'): {90: 10, 92: 10},
        Product('Dutch Lady'): {91: 7, 94: 10},
        Product('Milo'): {87: 2, 92: 20}
    }
    clear_stock(inventory, 190)
    compare(2, inventory, {
        Product('HL Milk'): {92: 10},
        Product('Dutch Lady'): {91: 7, 94: 10},
        Product('Milo'): {92: 20}
    })

def test_q3c():
    print('Testing Question 3C...')
    print('='*20)
    inventory = {
        Product('HL Milk'): {90: 10, 92: 10},
        Product('Dutch Lady'): {91: 7, 94: 10},
        Product('Milo'): {87: 2, 92: 20}
    }
    catalog = {
        Category('Milk'): {
            Product('HL Milk'): {90: 10, 92: 10},
            Product('Dutch Lady'): {91: 7, 94: 10}
        },
        Category('Drink'): {
            Product('Milo'): {87: 2, 92: 20}
        }
    }
    compare(1, make_catalog(inventory), catalog)
    inventory = {
        Product('HL Milk'): {90: 10, 92: 10},
        Product('Dutch Lady'): {91: 7, 94: 10},
        Product('Milo'): {87: 2, 92: 20},
    }
    catalog2 = {
        Category('Milk'): {
            Product('HL Milk'): {90: 10, 92: 10},
            Product('Dutch Lady'): {91: 7, 94: 10}
        },
        Category('Drink'): {
            Product('Milo'): {87: 2, 88: 1, 92: 20},
            Product('Milo Plus'): {88: 1}
        },
        Category('Others'): {
            Product('Bear'): {88: 1}
        }
    }
    stock_up(inventory, [Product('Milo Plus'), Product('Milo'), Product('Bear')], 88)
    compare(2, make_catalog(inventory), catalog2)

def test_q3d():
    print('Testing Question 3D...')
    print('='*20)
    inventory = {
        Product('HL Milk'): {90: 10, 92: 10},
        Product('Dutch Lady'): {91: 7, 94: 10},
        Product('Milo'): {87: 2, 92: 20}
    }
    catalog = {
        Category('Milk'): {
            Product('HL Milk'): {90: 10, 92: 10},
            Product('Dutch Lady'): {91: 7, 94: 10}
        },
        Category('Drink'): {
            Product('Milo'): {87: 2, 92: 20}
        }
    }
    catalog2 = {
        Category('Milk'): {
            Product('HL Milk'): {90: 10, 92: 10},
            Product('Dutch Lady'): {91: 7, 94: 10}
        },
        Category('Drink'): {
            Product('Milo'): {87: 2, 88: 1, 92: 20},
            Product('Milo Plus'): {88: 1}
        },
        Category('Others'): {
            Product('Bear'): {88: 1}
        }
    }
    compare(1, count_stock(inventory, catalog, Product('Hilo')), 0)
    compare(2, count_stock(inventory, catalog, Product('Milo')), 22)
    compare(3, count_stock(inventory, catalog, Category('Milk')), 37)
    compare(4, count_stock(inventory, catalog2, Product('Hilo')), 0)
    compare(5, count_stock(inventory, catalog2, Product('Milo')), 22)
    compare(6, count_stock(inventory, catalog2, Category('Drink')), 24)
    compare(7, count_stock(inventory, catalog, Category('Others')), 0)
    compare(8, count_stock(inventory, catalog2, Category('Others')), 1)

def test_q4c():
    print('Testing Question 4C...')
    print('='*20)
    try:
        evercrude = Tanker(1000, 8500)
    except:
        print('You should implement Tank first!\n')

    try:    evercrude.load(10000)
    except: compare(1, True, False)
    else:   compare(1, True, True)

    try:                evercrude.load(10000)
    except Overweight:  compare(2, True, True)
    except:             compare(2, True, False)
    else:               compare(2, True, False)

def test_q4d():
    print('Testing Question 4D...')
    print('='*20)
    try:
        car = Tank()
        car.add(500/0.75)
        compare(1, car.weight(), 500)
    except:
        compare(1, 'implement Tank first!', True)

    try:
        everseen = RoPaxFerry(1000, 2000)
        everseen.board(500)
    except:
        print('You should implement Tank first!\n')

    try:    everseen.load(car)
    except: compare(2, True, False)
    else:   compare(2, True, True)

    try:                everseen.load(car)
    except Overweight:  compare(3, True, True)
    except:             compare(3, True, False)
    else:               compare(3, True, False)

test_q2a()
test_q2b()
test_q2c()
test_q2d()
test_q2e()
test_q3a()
test_q3b()
test_q3c()
test_q3d()
test_q4c()
test_q4d()
