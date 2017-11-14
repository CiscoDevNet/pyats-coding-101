# Python Package Index

The [Python Package Index](https://pypi.python.org/pypi), a.k.a. PyPI, is a 
public repository of openly available packages/softwares for the Python 
programming language. 

PyPI packages are managed & installed by `pip`, the Python package management
system. `pip` is installed by default in Python virtual environments.

```bash
bash$ pip list          # list the packages currently installed
pip (9.0.1)
setuptools (36.7.2)
```

It's a good idea to search packages in [PyPI](https://pypi.python.org/pypi), 
and install it using `pip`:

For example, to install [requests](https://pypi.python.org/pypi/requests)
```bash
bash$ pip install requests
Collecting requests
  Downloading requests-2.18.4-py2.py3-none-any.whl (88kB)
    100% |████████████████████████████████| 92kB 932kB/s
Collecting urllib3<1.23,>=1.21.1 (from requests)
  Using cached urllib3-1.22-py2.py3-none-any.whl
Collecting chardet<3.1.0,>=3.0.2 (from requests)
  Using cached chardet-3.0.4-py2.py3-none-any.whl
Collecting idna<2.7,>=2.5 (from requests)
  Using cached idna-2.6-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests)
  Downloading certifi-2017.11.5-py2.py3-none-any.whl (330kB)
    100% |████████████████████████████████| 337kB 2.0MB/s
Installing collected packages: urllib3, chardet, idna, certifi, requests
Successfully installed certifi-2017.11.5 chardet-3.0.4 idna-2.6 requests-2.18.4 urllib3-1.22
```

`pip` automatically finds the package from PyPI, and installs it (and any of its
dependencies) into your current virtual environment.

Here's some useful commands:
```bash
bash$ pip install requests==2.18.4          # install a particular version
bash$ pip install --upgrade requests        # upgrade the specified package
bash$ pip freeze > requirements.txt         # produce the list of all packages installed in this venv into file
bash$ pip install -r requirements.txt       # install all packages/version specified in file
```

Read more on `pip` at [PIP Documentation](https://pip.pypa.io/en/stable/)