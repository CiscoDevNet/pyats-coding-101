'''
Exceptions
----------

    - try ... except ...
    - exception types

Set/Get Attribute By Name
-------------------------
    
    - setattr
    - getattr

Advanced Classes
----------------

    - classmethods
    - staticmethods
    - class variable vs instance variable
    - properties

Context Manager
---------------
    
    - with statements


Decorators
----------

    - what is a decorator
    - how to write a simple decorator

'''

# Exception Handling
# ------------------

# to catch a python exception & handle it, use try/except
try:
    1 / 0
except ZeroDivisionError:
    print('Cannot divide a number by zero!')

# you can also handle the exception... and do something in a cleanup clause
try:
    # use raise statment to raise an exception
    raise TypeError('This is a general TypeError')
except TypeError as e:
    print('I caught the following %s' % e)
finally:
    print('Print ... cleaning up')

# always specify the exception type you are catching for
# if you want to globally catch "any" exception, use the base class Exception
try:
    {}['non_existent_key']
except KeyError:
    # handle the key error
except Exception:
    # handle any other possible exceptions

# it's almost never a good idea to do the following:
try:
    # generate an exception
    raise Exception()
except:     # not specifying exception type
    # handle exception
# because this will catch ALL exceptions, including the few that derive from
# BaseException, including SystemExit, KeyboardInterrupt... etc.
# for more details, see: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# Set/Get Attribute By Name
# -------------------------

# sometimes you may want to set/get attributes by name
# do that with setattr() and getattr()
class MyObject(object): pass
obj = MyObject()
setattr(obj, 'new_attribute', 100)
getattr(obj, 'new_attribute')


# Advanced Classes
# ----------------

# classes may contain classmethods, staticmethods, and class variables
# in addition to standard methods:

class Fruits(object):

    # a class variable common to all instances of Fruits
    all_fruits = []

    def __init__(self, name):
        self.name = name

        # add this fruit instance to the list of all fruits.
        self.all_fruits.append(self)

    @classmethod
    def print_all_fruits(cls):
        '''
        a class method is declared using the @classmethod decorator, and 
        conventionally receives the class it is defined under as the first 
        argument 'cls'
        '''
        print([fruit.name for fruit in cls.all_fruits])

    @staticmethod
    def print_message():
        '''
        static methods are those that got decoreated with @staticmethod, and
        do not receive a class instance or the class as argument.
        '''
        print('i am a fruit!')

    @property
    def capitalized_name(self):
        '''
        define a property attribute using @property decorator. a property 
        attribute is a 'function' that gets the attribute value.
        
        (property is the setter/getter functionality equivalent in Python)

        For more information, refer to https://docs.python.org/3/library/functions.html#property
    
        '''
        return self.name.title()

# Context Manager
# ---------------

# python context managers are used in conjunction with the 'with' statement.
# they are typically used to manage resources that are 'scarce' by automatically
# providing closure when leaving the given context (Sheldon would love it)

# consider the following
file = open('somefile.txt')
# ...
file.close()

# what if the above code in ... failed/raised exception? what if we forgot to
# call file.close()? the resource/filehandler would remain open until process
# exit... unless we always wrapped it in try/except clauses and were very 
# careful with our code. This is prone to human error.

# with to the rescue:
with open('somefile.txt') as file:
    # ...

# when the code finishes execution and leaves the context of with statement,
# file.close() will automatically be called by the context manager/with.

# for more details on how to write context managers, refer to:
#   https://docs.python.org/3/reference/compound_stmts.html#with
#   https://docs.python.org/3/library/contextlib.html


# Decorators
# ----------
#
#   a decorator is a function that takes another function and extends its 
#   behavior without modifying it
#
#   decorator code only ever run one: at import time

def my_decorator(func):
    def wrapper():
        print("Something is happening before func() is called.")
        func()
        print("Something is happening after func() is called.")
    return wrapper

@my_decorator
def a():
    print('a got called')
