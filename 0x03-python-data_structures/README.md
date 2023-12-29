![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

> Python - Data Structures: Lists, Tuples

## Intro

In this project, I learned about how sequence data types work in
Python - specifically, lists and tuples.

## Resources

1. [Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
2. [Data structures ](https://docs.python.org/3/tutorial/datastructures.html)
3. [Youtube](https://www.youtube.com/watch?v=A1HUzrvS-Pw)

## Learning objectives

At the end of this project, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) without the help of Google the following concepts

- [x] What are lists and how to use them
- [x] What are the differences and similarities between strings and lists
- [x] What are the most common methods of lists and how to use them
- [x] How to use lists as stacks and queues
- [x] What are list comprehensions and how to use them
- [x] What are tuples and how to use them
- [x] When to use tuples versus lists
- [x] What is a sequence
- [x] What is tuple packing
- [x] What is sequence unpacking
- [x] What is the del statement and how to use it

## Script Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.\*)
- All your files must be executable

## Quizes

[Quizes](./quiz.md)

<div style='postion:relative'>
<a href="../0x02-python-import_modules"><img src="https://www.svgrepo.com/show/94045/back.svg" alt="back" width="50px"></a></div>

<div style='postion:relative'><a href="../0x04-python-more_data_structures"><img src="https://www.svgrepo.com/show/326975/chevron-forward-circle-sharp.svg" alt="next" width="50px"></a></div>

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                               | Prototype                                      |
| ---------------------------------- | ---------------------------------------------- |
| `0-print_list_integer.py`          | `def print_list_integer(my_list=[]):`          |
| `1-element_at.py`                  | `def element_at(my_list, idx):`                |
| `2-replace_in_list.py`             | `def replace_in_list(my_list, idx, element):`  |
| `3-print_reversed_list_integer.py` | `def print_reversed_list_integer(my_list=[]):` |
| `4-new_in_list.py`                 | `def new_in_list(my_list, idx, element):`      |
| `5-no_c.py`                        | `def no_c(my_string):`                         |
| `6-print_matrix_integer.py`        | `def print_matrix_integer(matrix=[[]]):`       |
| `7-add_tuple.py`                   | `def add_tuple(tuple_a=(), tuple_b=()):`       |
| `8-multiple_returns.py`            | `def multiple_returns(sentence):`              |
| `9-max_integer.py`                 | `def max_integer(my_list=[]):`                 |
| `10-divisible_by_2.py`             | `def divisible_by_2(my_list=[]):`              |
| `11-delete_at.py`                  | `def delete_at(my_list=[], idx=0):`            |
| `100-print_python_list_info.c`     | `void print_python_list_info(PyObject *p);`    |

## Tasks :page_with_curl:

- **0. Print a list of integers**
  - [0-print_list_integer.py](./0-print_list_integer.py): Python function that prints all
    integers of a list, one per line.
  - Without importing modules or casting integers into strings.

* **1. Secure access to an element in a list**

  - [1-element_at.py](./1-element_at.py): Python function that retrieves an element
    from a list.
  - If `idx` is negative or out of range (greater than the number of elements in
    `my_list`), the function returns `None`.
  - Without import modules or using `try/except`.

* **2. Replace element**

  - [2-replace_in_list.py](./2-replace_in_list.py): Python function that replaces an element
    of a list at a specific position.
  - If `idx` is negative or out of range (greater than the number of elements
    in `my_list`), the function returns the original list.
  - Without importing modules or using `try/except`.

* **3. Print a list of integers... in reverse!**

  - [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py): Python
    function that prints all integers of a list, one per line, in reverse order.
  - Without importing modules or casting integers into strings.

* **4. Replace in a copy**

  - [4-new_in_list.py](./4-new_in_list.py): Python function that replaces an element of a
    list at a specific position without modifying the original list.
  - If `idx` is negative or out of range (greater than the number of elements in
    `my_list`), the function returns the original list.
  - Without importing modules or using `try/except`.

* **5. Can you C me now?**
  - [5-no_c.py](./5-no_c.py): Python function that removes all characters `c`
    and `C` from a string and returns the string.
  - Without importing modules or using `str.replace()`.

  
* **6. Lists of lists = Matrix**
  - [6-print_matrix_integer.py](./6-print_matrix_integer.py): Python function that prints
    a matrix of integers, one row per line.
  - Without casting integers into strings.
