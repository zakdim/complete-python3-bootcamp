# complete-python3-bootcamp

Course Files for [Complete Python Bootcamp](https://www.udemy.com/course/complete-python-bootcamp/) on Udemy.

## GitHub

[GitHub - Complete python 3 bootcamp](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp)

## s09: Modules and Packages

### s09-77: Pip Install and PyPi

```bash
# pip install <package-name>
$ pip install requests
$ pip install colorama
```

* In python interpreter (command line):

```
>>> from colorama import init
>>> from colorama import Fore
>>> print(Fore.RED + "some red text")
some red text
>>> print(Fore.GREEN + "switch to green")
switch to green
>>> 

```

* Example of Excel package:

https://www.python-excel.org/

```
$ pip install openpyxl
```

## s10: Errors and Exceptions Handling

### s10-83: Update for Pylint Users

To see the same report that I do in the video, in the newest version of PyLint you need to add `-r y` (report yes) at the end of the command, so the full command should be:

```
pylint myexample.py -r y
```

### s10-84: Pylint Overview

```bash
$ pip install pylint
```
