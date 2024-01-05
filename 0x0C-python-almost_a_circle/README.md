![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

> Python - Almost a circle

## Background Context

The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, you will review everything about Python:

- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

You will also learn about

- `args` and `kwargs`
- Serialization/Deserialization
- JSON

![Meme](https://media2.giphy.com/media/unQ3IJU2RG7DO/200w.webp?cid=ecf05e47vwvnanfaua5wktd4b2fknxalp7wtxh6peo7mok14&rid=200w.webp&ct=g)

## Resources

1. [\*args and \*\*kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
2. [JSON ecoder and decoder](https://docs.python.org/3/library/json.html)
3. [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
4. [Python tests cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Learning objectives

By the end of this project you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) the following concepts **Without the help fo Google**

- [x] What is Unit testing and how to implement it in a large project
- [x] How to serialize and deserialize a Class
- [x] How to write and read a JSON file
- [x] What is `*args` and how to use it
- [x] What is `**kwargs` and how to use it
- [x] How to handle named arguments in a function

## Tests :heavy_check_mark:

- [tests/test_models](./tests/test_models): Folder containing the following
  independently-developed test files:
  - [test_base.py](./tests/test_models/test_base.py)
  - [test_rectangle.py](./tests/test_models/test_rectangle.py)
  - [test_square.py](./tests/test_models/test_square.py)

## Classes :cl:

### Base

Represents the "base" class for all other classes in the project. Includes:

- Private class attribute `__nb_objects = 0`.
- Public instance attribute `id`.
- Class constructor `def __init__(self, id=None):`
  - If `id` is `None`, increments `__nb_objects` and assigns its value to the
    public instance attribute `id`.
  - Otherwise, sets the public instance attribute `id` to the provided `id`.
- Static method `def to_json_string(list_dictionaries):` that returns the JSON
  string serialization of a list of dictionaries.
  - If `list_dictionaries` is `None` or empty, returns the string `"[]"`.
- Class method `def save_to_file(cls, list_objs):` that writes the JSON
  serialization of a list of objects to a file.
  - The parameter `list_objs` is expected to be a list of `Base`-inherited
    instances.
  - If `list_objs` is `None`, the function saves an empty list.
  - The file is saved with the name `<cls name>.json` (ie. `Rectangle.json`)
  - Overwrites the file if it already exists.
- Static method `def from_json_string(json_string):` that returns a list of
  objects deserialized from a JSON string.
  - The parameter `json_string` is expected to be a string representing a
    list of dictionaries.
  - If `json_string` is `None` or empty, the function returns an empty list.
- Class method `def create(cls, **dictionary):` that instantiates an object with
  provided attributes.
  - Instantiates an object with the attributes given in `**dictionary`.
- Class method `def load_from_file(cls):` that returns a list of objects
  instantiated from a JSON file.
  - Reads from the JSON file `<cls name>.json` (ie. `Rectangle.json`)
  - If the file does not exist, the function returns an empty list.
- Class method `def save_to_file_csv(cls, list_objs):` that writes the CSV
  serialization of a list of objects to a file.
  - The parameter `list_objs` is expected to be a list of `Base`-inherited
    instances.
  - If `list_objs` is `None`, the function saves an empty list.
  - The file is saved with the name `<cls name>.csv` (ie. `Rectangle.csv`)
  - Serializes objects in the format `<id>,<width>,<height>,<x>,<y>` for
    `Rectangle` objects and `<id>,<size>,<x>,<y>` for `Square` objects.
- Class method `def load_from_file_csv(cls):` that returns a list of objects
  instantiated from a CSV file.
  - Reads from the CSV file `<cls name>.csv` (ie. `Rectangle.csv`)
  - If the file does not exist, the function returns an empty list.
- Static method `def draw(list_rectangles, list_squares):` that draws
  `Rectangle` and `Square` instances in a GUI window using the `turtle` module.
  - The parameter `list_rectangles` is expected to be a list of `Rectangle`
    objects to print.
  - The parameter `list_squares` is expected to be a list of `Square` objects
    to print.
