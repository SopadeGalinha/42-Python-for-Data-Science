# 42 Python Piscine for Data Science - Module 0 - Starting

## Overview
This repository contains solutions to the exercises provided in the Python Piscine for Data Science. The exercises cover fundamental aspects of Python programming, from basic scripting to creating packages, while adhering to the 42 school's standards.

## Requirements
- Python 3.10
- Follow PEP8 guidelines
- No global variables
- Explicit imports only (e.g., `import numpy as np`, not `from pandas import *`)
- Code must handle exceptions and avoid unexpected quits (e.g., segmentation faults, bus errors).

## Exercises

### Exercise 00: First Python Script
**Directory:** `ex00/`  
**File:** `Hello.py`  
**Objective:** Modify a list, tuple, set, and dictionary to print customized greeting messages.  
**Output Example:**
```bash
$ python Hello.py
['Hello', 'World!']
('Hello', 'France!')
{'Hello', 'Paris!'}
{'Hello': '42Paris!'}
```

### Exercise 01: First Use of a Package
**Directory:** `ex01/`  
**File:** `format_ft_time.py`  
**Objective:** Write a script that formats and displays the current time since the Unix epoch and the current date in a specific format.  
**Output Example:**
```bash
$ python format_ft_time.py
Seconds since January 1, 1970: 1.67e+09
Oct 21 2022
```

### Exercise 02: First Python Function
**Directory:** `ex02/`  
**File:** `find_ft_type.py`  
**Objective:** Implement a function that identifies and prints the type of different objects.  
**Output Example:**
```bash
$ python tester.py
List : <class 'list'>
Tuple : <class 'tuple'>
Set : <class 'set'>
Dict : <class 'dict'>
Brian is in the kitchen : <class 'str'>
Toto is in the kitchen : <class 'str'>
Type not found
42
```

### Exercise 03: NULL Not Found
**Directory:** `ex03/`  
**File:** `NULL_not_found.py`  
**Objective:** Create a function that identifies and prints the type of various "null" objects, returning 0 if successful or 1 if an error occurs.  
**Output Example:**
```bash
$ python tester.py
Nothing: None <class 'NoneType'>
Cheese: nan <class 'float'>
Zero: 0 <class 'int'>
Empty: <class 'str'>
Fake: False <class 'bool'>
Type not Found
1
```

### Exercise 04: The Even and the Odd
**Directory:** `ex04/`  
**File:** `whatis.py`  
**Objective:** Write a script that checks whether a given number is even or odd. Handle cases where the input is invalid or multiple arguments are provided.  
**Output Example:**
```bash
$ python whatis.py 14
I'm Even.
$ python whatis.py -5
I'm Odd.
$ python whatis.py Hi!
AssertionError: argument is not an integer
```

### Exercise 05: First Standalone Python Program
**Directory:** `ex05/`  
**File:** `building.py`  
**Objective:** Create a program that counts the number of uppercase letters, lowercase letters, punctuation marks, digits, and spaces in a given string. The program prompts the user for input if no argument is given.  
**Output Example:**
```bash
$ python building.py "Python 3.0, released in 2008..."
The text contains 31 characters:
1 upper letters
15 lower letters
5 punctuation marks
4 spaces
6 digits
```

### Exercise 06: Recode the `filter()` Function
**Directory:** `ex06/`  
**Files:** `ft_filter.py`, `filterstring.py`  
**Objective:** Recode the `filter()` function using list comprehensions, and create a program that filters words based on a length criteria.  
**Output Example:**
```bash
$ python filterstring.py 'Hello the World' 4
['Hello', 'World']
```

### Exercise 07: Dictionary SoS
**Directory:** `ex07/`  
**File:** `sos.py`  
**Objective:** Implement a program that encodes a given string into Morse code using a dictionary.  
**Output Example:**
```bash
$ python sos.py "sos"
... --- ...
```

### Exercise 08: Loading...
**Directory:** `ex08/`  
**File:** `Loading.py`  
**Objective:** Create a function that mimics the behavior of `tqdm` to show a progress bar during a loop.  
**Output Example:**
```bash
$ python tester.py
100%|[===============================================================>]| 333/333
100%| | 333/333 [00:01<00:00, 191.61it/s]
```

### Exercise 09: My First Package Creation
**Directory:** `ex09/`  
**Files:** `*.py`, `*.txt`, `*.toml`, `README.md`, `LICENSE`  
**Objective:** Create a Python package that can be installed using `pip`, complete with metadata and documentation.  
**Installation Example:**
```bash
$ pip install ./dist/ft_package-0.0.1.tar.gz
$ pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
```

## Additional Notes
- Follow best practices for Python development, including adding docstrings to all functions.
- Your code will be evaluated by peers and automated tools, so ensure it runs without errors and passes all tests.
- Use `flake8` for code formatting and style checks.

---

By Odin, by Thor! Use your brain and good luck!
