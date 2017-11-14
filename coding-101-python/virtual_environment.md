# Python Virtual Environment

A Python virtual environment is an isolated Python environment that allows you
install various packages & modules into, without impacting anything else.

A Python virtual environment appears as a standard file system directory. To 
create a new virtual environment, do:

```bash

bash$ python3 -m venv my_new_venv
```

This will create a new virtual environment in a folder called `my_new_venv` 
under the current directory. 

To *set into and start using* this virtual environment, you **activate** it by:
```bash
bash$ source my_new_venv/bin/activate     # for bash
csh> source my_new_venv/bin/activate.csh  $ for csh
```

You can delete any virtual environment by just deleting the folder. This will
destroy/delete all packages/content managed under this virtual environment.

Read more on [Python venv](https://docs.python.org/3/tutorial/venv.html)
