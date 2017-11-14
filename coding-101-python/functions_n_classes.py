'''
Functions
---------
    - define a function using 'def'
    - a function can have arbitrary of arguments (positional and keyword)
    - functions return None if no return statement is provided

Classes
-------
    - created using 'class' statement.
    - __init__() is the entry point
    - the first argument to any method in a class should be 'self'.

'''

# Functions & Arguments
# ---------------------

# define a function
def adder(x, y):
    # functions can return
    return x + y

# access using positional arguments
print(adder(1, 2))

# access using keyword arguments
print(adder(x=1, y=2))

# return statement breaks execution and returns from the function
# scope immediately
def tester(x, y):
    if x + 1 > y:
        return 'x + 1 is greater than y'
    else:
        return 'x + 1 is not greater than y'
    print('done')  # this is never executed !

print(tester(1, 3))

# arbitrary number of positional arguments
def sum_numbers_up(*args):
    total = 0
    for number in args:
        total += number
    return total

# arbitrary number of keyword arguments
def print_arguments(**kwargs):
    for key, value in kwargs.items():
        print('%s = %s' % (key, value))

# Classes
# -------

# define a class
class Person(object):
    '''Person class docstring '''

    def __init__(self, firstname, lastname):
        '''require arguments firstname & lastname'''
        self.firstname = firstname
        self.lastname = lastname

    def print_name(self):
        print('{firstname} {lastname}'.format(firstname = self.firstname,
                                              lastname = self.lastname))

# create an instance of a class
ironman = Person(firstname = 'Tony', lastname = 'Stark')

# call methods
ironman.print_name()

# access attributes
print(ironman.firstname)

# create a subclass by inhering a parent class
class Character(Person):

    def __init__(self, firstname, lastname, nickname):
        # call parent class's methods using super()
        super().__init__(firstname, lastname)
        self.nickname = nickname

    def print_nickname(self):
        print(self.nickname)

ironman = Character(firstname = 'Tony', 
                    lastname = 'Stark', 
                    nickname = 'ironman')

ironman.print_name()
ironman.print_nickname()