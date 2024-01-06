![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

> Python - Input/Output

## Intro

In this project, I practiced file handling in Python. I used the builtin `with`,
`open`, and `read` functions with the `json` module to read and write files and
serialize and deserialize objects with JSON.

## Resources

**Read or watch**

1. [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
2. [8.7 Predefined cleanup actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
3. [Dive into python3: Chapter 11. Files](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf)
4. [Json econder and decoder](https://docs.python.org/3/library/json.html)
5. [Learn to program 8 - Reading and writting files](https://www.youtube.com/watch?v=EukxMIsNeqU)
6. [Automate the boring stuff with python](https://automatetheboringstuff.com/)
7. [All about py-file I/O](https://techvidvan.com/tutorials/python-file-read-write/s)
8. [Youtube](https://www.youtube.com/results?search_query=python+I%2FO)
9. [Python](https://www.google.com/search?q=python+io)

## Learning objectives

By the end of this session, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) **without the help of google** the following concepts

- [x] Why Python programming is awesome
- [x] How to open a file
- [x] How to write text in a file
- [x] How to read the full content of a file
- [x] How to read a file line by line
- [x] How to move the cursor in a file
- [x] How to make sure a file is closed after using it
- [x] What is and how to use the with statement
- [x] What is JSON
- [x] What is serialization
- [x] What is deserialization
- [x] How to convert a Python data structure to a JSON string
- [x] How to convert a JSON string to a Python data structure

## Tests :heavy_check_mark:

- [tests](./tests): Folder of test files. Provided by ALX School.

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                       | Prototype                                                         |
| -------------------------- | ----------------------------------------------------------------- |
| `0-read_file.py`           | `def read_file(filename=""):`                                     |
| `1-number_of_lines.py`     | `def number_of_lines(filename=""):`                               |
| `2-read_lines.py`          | `def read_lines(filename="", nb_lines=0):`                        |
| `3-write_file.py`          | `def write_file(filename="", text=""):`                           |
| `4-append_write.py`        | `def append_write(filename="", text=""):`                         |
| `5-to_json_string.py`      | `def to_json_string(my_obj):`                                     |
| `6-from_json_string.py`    | `def from_json_string(my_str):`                                   |
| `7-save_to_json_file.py`   | `def save_to_json_file(my_obj, filename):`                        |
| `8-load_from_json_file.py` | `def load_from_json_file(filename):`                              |
| `10-class_to_json.py`      | `def class_to_json(obj):`                                         |
| `14-pascal_triangle.py`    | `def pascal_triangle(n):`                                         |
| `100-append_after.py`      | `def append_after(filename="", search_string="", new_string=""):` |

## Tasks :page_with_curl:

- **0. Read file**

  - [0-read_file.py](./0-read_file.py): Python function that prints the contents of a UTF8 text
    file to standard output.

* **1. Number of lines**

  - [1-number_of_lines.py](./1-number_of_lines.py): Python function that returns the number of lines
    contained in a text file.

* **2. Read n lines**

  - [2-read_lines.py](./2-read_lines.py): Python function that prints `n` lines of a UTF8 text
    file to standard output.

* **3. Write to a file**

  - [3-write_file.py](./3-write_file.py): Python function that writes a string to a UTF8 text
    file and returns the number of characters written.

* **4. Append to a file**

  - [4-append_write.py](./4-append_write.py): Python function that appends a string to the end of a
    UTF8 text file and returns the number of characters appended.

* **5. To JSON string**

  - [5-to_json_string.py](./5-to_json_string.py): Python function that returns the JSON string
    representation of an object.

* **6. From JSON string to Object**

  - [6-from_json_string.py](./6-from_json_string.py): Python function that returns the Python object
    represented by a JSON string.

* **7. Save Object to a file**

  - [7-save_to_json_file.py](./7-save_to_json_file.py): Python function that writes an object to a text
    file using JSON representation.

* **8. Create object from a JSON file**

  - [8-load_from_json_file.py](./8-load_from_json_file.py): Python function that creates an object from a
    `.json` file.

* **9. Load, add, save**

  - [9-add_item.py](./9-add_item.py): Python script that stores all command line arguments to a
    Python list saved in the file `add_item.json`.
