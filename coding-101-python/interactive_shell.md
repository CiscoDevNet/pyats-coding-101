# Python Interactive Shell

Python is an interpreted language. One of the best ways to learn Python is to
drop into the interactive shell, type code in it, and see it get evaluated as
you hit enter. No compilation necessary.

To start, type python3 (since we are using python3) in your shell.
```bash
bash$ python3

Python 3.4.1 (default, Nov 12 2014, 13:34:48)
[GCC 4.4.6 20120305 (Red Hat 4.4.6-4)] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

and type away:
```python
>>> foo = "bar"
>>> number = 40 + 2
>>> print('hello world')
hello world

```

There are some nice functions in the interactive shell:
```python
>>> import sys              # let's import a standard module
>>> help(sys)               # display help text w.r.t. module sys
>>> dir(sys)                # print the list of methods/attributes/properties
                            # of the given object
```