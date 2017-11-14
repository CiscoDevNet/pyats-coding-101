'''
Conditionals
------------
    if ... elif ... else

Loops
-----
    for ... in ...
    while ...

'''

# IF statement
# ------------

# basic if statement
if 40 + 2 == 42:
    print('The answer of everything is 42')

number = 100
if number == 100:
    print('number equal to 100')
elif number > 100:
    print('number greater than 100')
else:
    print('number smaller than 100')

# FOR/WHILE loops
# ---------------

# for loop 
for character in 'abcdefghijklmnopqrstuvwxyz':
    print(character)

# while loop
numbers = [1, 2, 3, 4, 5]
while numbers:
    print(numbers.pop())

# Control
# -------

# loop control statements
for character in 'abcdefghijklmnopqrstuvwxyz':
    if character == 'j':
        break
    elif character == 'e':
        continue
    print(character)

numbers = [1, 2, 3, 4, 5]
while numbers:
    if numbers == 4:
        break
    elif number == 2:
        continue
    print(numbers.pop())