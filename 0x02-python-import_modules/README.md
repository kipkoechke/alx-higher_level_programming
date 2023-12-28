![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

> Python import, modules and command line arguments

## Intro

In this session, we will explore importin modules, packages and how to use commandline arguments in python.

## Resources

1. [Modules](https://docs.python.org/3/tutorial/modules.html)
2. [Commandline arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
3. [Code styling](https://pypi.org/project/pycodestyle/)

## Learning objectives

By the end of this session, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) without the help of Google the following concepts

- [x] How to import functions from another file
- [x] How to use imported functions
- [x] How to create a module
- [x] How to use the built-in function `dir()`
- [x] How to prevent code in your script from being executed when imported
- [x] How to use command line arguments with your Python programs

## Script Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version `3.8.5`)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should use the pycodestyle (version 2.8.\*)
- All your files must be executable

## Quizes

[Quiz](./quiz.md)

<div style='postion:relative'>
<a href="../0x01-python-if_else_loops_functions"><img src="https://www.svgrepo.com/show/94045/back.svg" alt="back" width="50px"></a></div>

<div style='postion:relative'><a href="../0x02-python-import_modules"><img src="https://www.svgrepo.com/show/326975/chevron-forward-circle-sharp.svg" alt="next" width="50px"></a></div>

## Tasks :page_with_curl:

- **0. Import a simple function from a simple file**
  - [0-add.py](./0-add.py): Python program that imports the function
    `def add(a, b):` from the file [add_0.py](./add_0.py) and prints the
    result of the addition `1 + 2 = 3`.
  - Output: `<a value> + <b value> = <add(a, b) value>` followed by a new line.

* **1. My first toolbox!**

  - [1-calculation.py](./1-calculation.py): Python program that imports functions
    from the file [calculator_1.py](./1-calculator.py) and prints the result
    of the addition, subtraction, multiplication and division of `10` and `5`.
  - Output: `<a value> <operator> <b value> = <operation(a, b) value>` followed by a new line.

* **2. How to make a script dynamic!**

  - [2-args.py](./2-args.py): Python program that prints the number of
    and list of its arguments.
  - Output: `[Number of arguments] argument` (if number is one) or `arguments` (otherwise), followed by:
    - `:` (or `.` if no argumets were passed), followed by
    - A new line, followed by
    - One argument per line - the position of the argument (starting at `1`) followed by `:` followed by the argument value and another new line.

* **3. Infinite addition**

  - [3-infinite_add.py](./3-infinite_add.py): Python program that prints the result of the
    addition of all arguments.
  - Output: Sum of the arguments followed by a new line.

* **4. Who are you?**
  - [4-hidden_discovery.py](./4-hidden_discovery.py): Python program that prints all the
    names defined by the compiled module `hidden_4.pyc`.
  - Output: One name per line in alphabetical order.
  - Names starting with `__` are not printed.
