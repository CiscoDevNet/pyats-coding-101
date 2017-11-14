'''
Arithmetic Operators
--------------------

    +       addition
    -       subtraction
    *       multiplication
    /       division
    %       modulus
    //      floor division
    **      power

Assignment Operators
--------------------
    
    =       assignment
    +=      increment & assign
    -=      decrement & assign
    *=      multiply & assign
    /=      divide & assign
    %=      modulus & assign
    //=     floor division & assign
    **=     power & assign

Relational Operators
--------------------

    ==      equals to
    !=      not equal to
    >       greater than
    <       less than
    >=      greater than or equal to
    <=      less than or equal to

Boolean Operators
-----------------
    
    add, or, not

Identiy
-------
    
    is

Membership
----------

    in

'''

# basic math
ten = 5 + 5
four = 2 ** 2
one = 5 % 2

# assignments
number = 0
number += 1  # increment by 1
number -= 1  # decrement by 1

# relational operators results in a boolean result
0 > 1       # False
1 < 2       # True
3.14 >= 3   # True

# boolean operators
True and False      # False
True or False       # True
not True            # false

# identity check
obj = None
obj is None         # True


# membership
'a' in 'abcdefg'    # True