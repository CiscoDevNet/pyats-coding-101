'''
The Import System
-----------------

there's two types of things that can be imported using the import statement
  - module
  - package   (a module that can contain submodules)

module:
  - is basically any file ending with .py
  - the code is executed on import

package:
  - a directory containing __init__.py file
  - only the content in __init__.py file is executed when imported.
    (unless subsequent modules within this directory is imported in this file)

absolute import in python3

- only modules and packages directly reacheable in sys.path will be imported.

sys.path
  - list of strings that specifies earch path for modules.
  - this is initiated from env var PYTHONPATH

> it's considered very good practice to put all import statements on the    <
> top of your python file for readability.                                  <

https://www.python.org/dev/peps/pep-0328/
https://docs.python.org/3/reference/import.html
'''

# typical imports
import os
import xml.parser
import collections, functools, itertools

from collections import OrderedDict
from itertools import count, cycle, repeat

# rename on import
# (avoid local naming clash)
from os.path import join as join_paths_together

# you can span a single import over multiple lines
from os.path import (abspath, basename, dirname,
                     exists, expanduser, join,
                     ismount, realpath, relpath, stat)

# relative imports within a package
# (the following are for illustrative only)
from . import some_other_module
from ..another_package import some_module

# when an import occurs, the imported module (by name) is put
# into your current module scope as the module object
import sys
print(sys.copyright)

# modify sys.path to enable python to search more paths for python modules.
import sys
sys.path.append('/path/to/your/directory')
import package_from_your_directory
