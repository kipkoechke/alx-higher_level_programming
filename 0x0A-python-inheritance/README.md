![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

> Inheritance in python

## About

Inheritance is a powerful feature of object-oriented programming (OOP) that allows a class to inherit attributes and methods from a parent class. This allows you to create a new class that is a modified version of an existing class, without having to rewrite the entire class from scratch. Other than saving you a lot of time and effort, it also helps you to avoid duplication of code. Stay hooked as we dive into how to implement inheritance in python.

## Resources

1. [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
2. [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
3. [Inheritance in python](https://www.geeksforgeeks.org/inheritance-in-python/)
4. [Learn to program 10: Inheritance](https://www.youtube.com/watch?v=d8kCdLCi6Lk)
5. [Youtube](https://www.youtube.com/results?search_query=Inheritance+in+python)
6. [Google](https://www.google.com/search?q=Inheritance+python)

## Learning objectives

At the end of the project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) **without the help of Google** the following concepts

- [x] What is a superclass, baseclass or parentclass
- [x] What is a subclass
- [x] How to list all attributes and methods of a class or instance
- [x] When can an instance have new attributes
- [x] How to inherit class from another
- [x] How to define a class with multiple base classes
- [x] What is the default class every class inherit from
- [x] What is the default class every class inherit from
- [x] Which attributes or methods are available by heritage to subclasses
- [x] What is the purpose of inheritance
- [x] What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

## Quizes

[Quiz](./quiz.md)

## Tests :heavy_check_mark:

- [tests](./tests): Folder of test files. Includes both Holberton-provided ones
  as well as the following two independently-developed:
  _ [1-my_list.txt](./1-my_list.txt)
  _ [7-base_geometry.txt](./7-base_geometry.txt)

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                    | Prototype                             |
| ----------------------- | ------------------------------------- |
| `0-lookup.py`           | `def lookup(obj):`                    |
| `2-is_same_class.py`    | `def is_same_class(obj, a_class):`    |
| `3-is_kind_of_class.py` | `def is_kind_of_class(obj, a_class):` |
| `4-inherits_from.py`    | `def inherits_from(obj, a_class):`    |
| `101-add_attribute.py`  | `def add_attribute(obj, att, value):` |

## Tasks :page_with_curl:

- **0. Lookup**
  - [0-lookup.py](./0-lookup.py): Python function that returns a list of available attributes
    and methods of an objects.

* **1. My list**

  - [1-my_list.py](./1-my_list.py): Python class `MyList` that inherits from `list`. Includes:
    - Public instance method `def print_sorted(self):` that prints the list in
      ascending sorted order (assumes all list elements are `int`s).

* **2. Exact same object**

  - [2-is_same_class.py](./2-is_same_class.py): Python function that returns `True` if an object is
    exactly an instance of a specified class; otherwise `False`.

* **3. Same class or inherit from**

  - [3-is_kind_of_class.py](./3-is_kind_of_class.py): Python function that returns `True` if an object is
    an instance or inherited instance of a specified class; otherwise `False`.

* **4. Only sub class of**
  - [4-inherits_from.py](./4-inherits_from.py): Python function that returns `True` if an object is
    an inherited instance (either directly or indirectly) from a specified class;
    otherwise `False`.
