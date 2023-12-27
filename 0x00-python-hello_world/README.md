![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

> Introduction to Programming Python

![meme](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg)

## Author's Disclaimer

```
Welcome to the Python world!

The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode.

Enjoy!

- Guillaume
```

## Intro

In this module, we will explore the basics of programming in python.

### Resources

1. [The python Tutorial](https://docs.python.org/3/tutorial/index.html)
2. [Whetting your appetite](https://docs.python.org/3/tutorial/appetite.html)
3. [Using the python interpreter](https://docs.python.org/3/tutorial/interpreter.html)
4. [An informal introduction to python](https://docs.python.org/3/tutorial/introduction.html)
5. [String formatting](https://realpython.com/python-f-strings/)
6. [Youtube](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
7. [PEP - python coding convention](https://peps.python.org/pep-0008/)
8. [Pycodestyle](https://pypi.org/project/pycodestyle/)

## Learning objectives

By the end of this session, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) without the help of Google the following.

- [x] Why Python programming is awesome
- [x] Who created Python
- [x] Who is Guido van Rossum
- [x] Where does the name ‘Python’ come from
- [x] What is the Zen of Python
- [x] How to use the Python interpreter
- [x] How to print text and variables using print
- [x] How to use strings
- [x] What are indexing and slicing in Python
- [x] What is the official Python coding style and how to check your code with `pycodestyle`

## Script Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.\*)
- All your files must be executable

## Quizes

[Quiz](./quiz.md)

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                       | Prototype                           |
| -------------------------- | ----------------------------------- |
| `10-check_cycle.c`         | `int check_cycle(listint_t *list);` |
| `102-magic_calculation.py` | `def magic_calculation(a, b):`      |

## Tasks :page_with_curl:

- **0. Run Python File**

  - [0-run](./0-run): Bash script that runs a Python script file saved
    in the environment variable `$PYFILE`.

- **1. Run inline**

  - [1-run_inline](./1-run_inline): Bash script that runs Python code saved in the
    environment variable `$PYCODE`.

- **2. Hello, print**

  - [2-print.py](./2-print.py): Python script that prints exactly `"Programming is
like building a multilingual puzzle`, followed by a new line using the function `print`.

- **3. Print integer**

  - [3-print_number.py](./3-print_number.py): Python script that prints the integer stored
    in the variable `number`, followed by `Battery street`, followed by a new line.
  - Completion of [this source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py).

- **4. Print float**

  - [4-print_float.py](./4-print_float.py): Python script that prints the float stored
    in the variable `number` with a precision of two digits.
  - Completion of [this source code](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py).

- **5. Print string**

  - [5-print_string.py](./5-print_string.py): Python script that prints a string stored
    in the variable `str` three times, then a new line, then the first nine characters
    contained in `str`, followed by another new line.
  - Completion of [this source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py).

- **6. Play with strings**

  - [6-concat.py](./6-concat.py): Python script that prints `Welcome to Holberton
School!` using the variables `str1 = "Holberton"` and `str2 = "School"`.
  - Completion of [this source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py).

- **7. Copy - Cut - Paste**

  - [7-edges.py](./7-edges.py): Python script that sets three string variables based
    on the string contained in the variable `word` as follows:
  - `word_first_3`: Contains the first three letters of the variable `word`.
  - `word_last_2`: Contains the last two letters of the variable `word`.
  - `middle_word`: Contains the value of the variable `word` without the first and last letters.
  - Completion of [this source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py).

- **8. Create a new sentence**

  - [8-concat_edges.py](./8-concat_edges.py): Python script that prints `object-oriented
programming with Python`, followed by a new line without creating new variables or
    string literals.
  - Completion of [this source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py).

- **9. Easter Egg**

  - [9-easter_egg.py](./9-easter_egg.py): Python script that prints "The Zen of Python" by
    Tim Peters, followed by a new line.

- **10. Linked list cycle**

  - [10-check_cycle.c](./10-check_cycle.c): C function that checks if a linked list
    contains a cycle.
  - Returns `0` if there is no cycle and `1` if there is.
  - Helper files:
    - [linked_lists.c](./linked_lists.c): C functions handling linked lists for testing
      [10-check_cycle.c](./10-check_cycle.c) (provided by Holberton School).
    - [lists.h](./lists.h): Header file containing definitions and prototypes for
      all types and functions used in [linked_lists.c](./linked_lists.c) and
      [10-check_cycle.c](./10-check_cycle.c).

  <p align="right"><a href="../0x01-python-if_else_loops_functions"><img src="https://www.svgrepo.com/show/326975/chevron-forward-circle-sharp.svg" alt="next" width="50px"></a></p>
