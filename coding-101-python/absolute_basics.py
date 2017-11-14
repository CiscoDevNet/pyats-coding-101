#!/usr/bin/env python

'''
The Basics of Python Language (Python 3+)
-----------------------------------------

- python program files ends with .py
  typically, you can run a python program file using:
    bash$ python <filename>.py

- python files are white space sensitive
    eg: indentation == structure.
  do not mix spaces with tabs - stick with ONE.
'''

# define a function
def hello_world():
    # as usuals :)
    print('hello world')


# boilerplate code - the standard entrypoint to a python program
if __name__ == '__main__':
    # call our function
    hello_world()