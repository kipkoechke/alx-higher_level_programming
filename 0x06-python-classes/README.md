![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

> Object Oriented Programming

![OOP Meme](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/247/oop-meme.jpg)

## Intro

In this project, I began practicing object-oriented programming using
classes and objects in Python. I learned about attributes, methods, and
properties as well as data abstraction, data encapsulation, and information
hiding.

## Resources

1. [Object Oriented Programming - In English Please](https://python.swaroopch.com/oop.html)
2. [Introduction to OOP](https://python-course.eu/oop/object-oriented-programming.php)
3. [Properties vs. Setters vs. Getters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
4. [Learn to program - part 9 ](https://www.youtube.com/watch?v=1AGyBuVCTeE&)
5. [Python classes and objects](https://www.youtube.com/watch?v=apACNr7DC_s)
6. [OOP](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

## Learning objectives

By the end of this session, I was able to [explain to anyone](https://fs.blog/feynman-learning-technique/) the following concepts without the help of Google.

- [x] What is OOP
- [x] “first-class everything”
- [x] What is a class
- [x] What is an object and an instance
- [x] What is the difference between a class and an object or instance
- [x] What is an attribute
- [x] What are and how to use public, protected and private attributes
- [x] What is `self`
- [x] What is a method
- [x] What is the special `__init__` method and how to use it
- [x] What is Data Abstraction, Data Encapsulation, and Information Hiding
- [x] What is a property
- [x] What is the difference between an attribute and a property in Python
- [x] What is the Pythonic way to write getters and setters in Python
- [x] How to dynamically create arbitrary new attributes for existing instances of a class
- [x] How to bind attributes to object and classes
- [x] What is the `__dict__` of a class and/or instance of a class and what does it contain
- [x] How does Python find the attributes of an object or class
- [x] How to use the getattr function

## More info

### Documentation is mandatory

Each module, class, and method must contain docstring as comments see [example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

### Script requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.\*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tests :heavy_check_mark:

- [tests](./tests): Folder of test files provided by ALX Software Engineering.

## Tasks :page_with_curl:

- **0. My first square**
  - [0-square.py](./0-square.py): Python class `Square` that defines a square.

* **1. Square with size**

  - [1-square.py](./1-square.py): Python class `Square` that defines a square. Builds on
    [0-square.py](./0-square.py) with:
    - Private instance attribute `size`.
    - Instantiation with `size`.

* **2. Size validation**

  - [2-square.py](./2-square.py): Python class `Square` that defines a square. Builds on
    [1-square.py](./1-square.py) with:
    - Instantiation with optional `size`: `def __init__(self, size=0):`
  - If a provided `size` attribute is not an integer, a `TypeError` exception
    is raised with the message `must be an integer`.
  - If a provided `size` attribute is less than `0`, a `ValueError` exception
    is raised with the message `size must be >= 0`.

* **3. Area of a square**

  - [3-square.py](./3-square.py): Python class `Square` that defines a square. Builds on
    [2-square.py](./2-square.py) with:
    - Public instance attribute `def area(self):` that returns the current
      square area.
