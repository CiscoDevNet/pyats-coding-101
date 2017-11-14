'''
basic datatypes
---------------
      bool    -> boolean
      int     -> integer
      float   -> decimals/float
      str     -> string
      dict    -> dictionaries (aka. hash map in some languages)
      list    -> lists (aka. arrays in some langauges)
      tuples  -> basically lists, but immutable
      None    -> special object, singleton that means, well, nothing.
'''

# there's no variable declaration/initialization - just name as you go
# variable names may contain A-Z, a-z, 0-9, _, but cannot start with a number.
foo = 'bar'             # set variable named foo to contain string 'bar'
total = 1 * 2 * 3       # set variable named total to result of 1 x 2 x 3 (6)

# Booleans
# --------

# there's true... and there's false
truth = True
falsehood = False

# Integers/Floats
# ---------------

# integers are just numbers
integer_1 = 1
the_ultimate_answer_to_question_of_life_universe_and_everything = 42

# declare a float by just using . naturally in math
pi = 3.1415926535897932384626433832795028841971693

# Strings
# -------

# a string is typically surrounded by '', ""
foo1 = "bar"
foo2 = 'bar'  # no difference

# a '' quoted string cannot contain '
# a "" quoted string cannot contain "
# (unless you escape it)
foo3 = "\"bar\""
foo4 = '\rbar\''

# so it's better to mix them
foo5 = '"bar"'
foo6 = "'bar'"

# a string must finish on the same line, unless you use \ at the end
foo7 = "a multiple\
line string"

# alternatively, use ''' and """ to denote multi-line strings without having
# any of the above difficulties
foo8 = '''python is a simple
yet complicated programming
language for "adults"'''

# use index to access string position
print(foo1[0])

# and slicing to indicate a sub-string
print(foo7[2:10])

# there are many useful, built-in string methods
'python'.title()            # Python
'uppercase'.upper()         # UPPERCASE
'LOWERCASE'.lower()         # lowercase
'a b c'.split()             # ['a', 'b', 'c']
'  a good day  '.strip()    # 'a good day'

# concatenate strings by adding them
ironman = "Tony" + " " + "Stark"

# Dictionary
# ----------

# a dictionary comprises of key-value pairs
# dictionaries are unordered (order of insertion is lost)
character = {}
character['firstname'] = "tony"
character['lastname'] = "stark"
character['nickname'] = "ironman"

# alternatively, create it in one shot
character = {'firstname': 'tony', 'lastname': 'stark', 'nickname': 'ironman'}

# some basic methods of a dictionary
print(character['firstname'], character['lastname'])
charater.pop('firstname')
charater.setdefault('home_automation', 'J.A.R.V.I.S')
character.update(firstname = "Tony", lastname = "Stark")
all_keys = character.keys()
all_values = character.values()
key_value_pairs = character.items()

# Lists & Tuples
# --------------

# lists are extremly versatile, and can contain anything (including other lists)
# lists are ordered.
movies = ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi']
combo = ["Arthur Dent", 42, list1]

# lists are indexed by integer position starting from 0
# negative numbers starts from the end of the list (starting from -1)
print(movies[0], movies[1], movies[2])
print(movies[-1], movies[-2], movies[-3])

# typical list operations
movies.append("The Phantom Menace")
movies.extend(["Attack of the Clones", "Revenge of the Sith"])
movies[0] = "Episode IV - A New Hope"
combo.pop(-1)   # -1 means last item

# slicing worsk too
movies[3:]  # everything from 3 onwards

# tuples are the exact same as lists, but you cannot modify it.
movies = ('A New Hope', 'The Empire Strikes Back', 'Return of the Jedi')

# None
# ----

# None is special
nothing = None

# Typecasting
# -----------

# many things can be casted around
number = "42"               # starting with a string
number = int(number)        # cast to integer
number = str(number)        # casted back to string

languages = ['Python', 'C#', 'Ruby']    # start with a list
languages = tuple(languages)            # cast to tuple