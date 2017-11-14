'''
Regular Expression in Python
----------------------------

    - use 're' module to do anything regular expression related
    - pre-compiling regex patterns will speed up execution
    - regex matching typically produces match objects
    - it's a good idea to use r'' (raw string literal) to define regex patterns
'''

import re

# basic string matching
re.match(r'[0-9]+', '12345')

# pre-compile to speedup the process
pattern = re.compile(r'[0-9]+')
pattern.match('12345')
pattenr.match('100')

# use if to test whether a match occured
if pattern.match('12345'):
    print('pattern match!')
else:
    print('no match!')

# test if a string contains a pattern
pattern = re.compile(r'([a-z]+)')
if pattern.search("123hello456world789"):
    print('string contains characters')

# find all occurances of a pattern in a string
pattern = re.compile(r'([a-z]+)')
for match in pattern.findall("123hello456world789"):
    print(match)

# matching pattern into variables
result = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Natasha Romanoff")
result.groupdict()
{'first_name': 'Natasha', 'last_name': 'Romanoff'}