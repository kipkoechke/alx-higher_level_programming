#!/usr/bin/python3
# test_square.py
"""
This module defines unit tests for the `models.square.Square` class.

Unittest classes:
    TestSquareInstantiation - Tests instantiation of the Square class.
    TestSquareSize - Tests size attribute initialization.
    TestSquareX - Tests x attribute initialization.
    TestSquareY - Tests y attribute initialization.
    TestSquareOrderOfInitialization - Tests the order of attribute initialization.
    TestSquareArea - Tests the area() method of the Square class.
    TestSquareStdout - Tests __str__ and display() methods.
    TestSquareUpdateArgs - Tests update() method with *args.
    TestSquareUpdateKwargs - Tests update() method with **kwargs.
    TestSquareToDictionary - Tests to_dictionary() method.
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """
    Unittests for testing the instantiation of the Square class.
    """

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_square(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)


class TestSquareSize(unittest.TestCase):
    """
    Unittests for testing size attribute initialization of the Square class.
    """

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def test_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def test_memoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    # Test size values
    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquareX(unittest.TestCase):
    """
    Unittests for testing initialization of Square x attribute.
    """

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3), 2)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5), 2)

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Python', 2)

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefg'), 2)

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcdefg'), 2)

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 2)


class TestSquareY(unittest.TestCase):
    """
    Unittests for testing initialization of Square y attribute.
    """

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {"a": 1, "b": 2})

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, True)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, memoryview(b'abcdefg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, float('nan'))


class TestSquareOrderOfInitialization(unittest.TestCase):
    """
    Unittests for testing the order of attribute initialization.
    """

    def test_order(self):
        s1 = Square(10, 2, 3, 4)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 4)

    def test_order_size_only(self):
        s1 = Square(10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertNotEqual(s1.id, None)


class TestSquareArea(unittest.TestCase):
    """
    Unittests for testing the area() method of the Square class.
    """

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_area_custom_size(self):
        s = Square(10)
        self.assertEqual(s.area(), 100)

    def test_area_custom_size_x_y(self):
        s = Square(7, 3, 4)
        self.assertEqual(s.area(), 49)


class TestSquareStdout(unittest.TestCase):
    """
    Unittests for testing the __str__ and display() methods of the Square class.
    """

    def setUp(self):
        sys.stdout = io.StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_str_output(self):
        s = Square(2, 1, 1)
        s_str = s.__str__()
        self.assertEqual(s_str, "[Square] (1) 1/1 - 2")

    def test_display_output(self):
        s = Square(2, 1, 1)
        s.display()
        displayed = sys.stdout.getvalue()
        self.assertEqual(displayed, "\n  ##\n  ##")


class TestSquareUpdateArgs(unittest.TestCase):
    """
    Unittests for testing the update() method with *args in the Square class.
    """

    def test_update_one_arg(self):
        s = Square(10)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_two_args(self):
        s = Square(10)
        s.update(89, 2)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.id, 89)

    def test_update_three_args(self):
        s = Square(10)
        s.update(89, 2, 3)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.id, 89)

    def test_update_four_args(self):
        s = Square(10)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.id, 89)

    def test_update_five_args(self):
        s = Square(10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.id, 89)


class TestSquareUpdateKwargs(unittest.TestCase):
    """
    Unittests for testing the update() method with **kwargs in the Square class.
    """

    def test_update_kwargs_id(self):
        s = Square(10, 2, 3)
        s.update(id=89)
        self.assertEqual(s.id, 89)

    def test_update_kwargs_size(self):
        s = Square(10, 2, 3)
        s.update(size=5)
        self.assertEqual(s.size, 5)

    def test_update_kwargs_x(self):
        s = Square(10, 2, 3)
        s.update(x=7)
        self.assertEqual(s.x, 7)

    def test_update_kwargs_y(self):
        s = Square(10, 2, 3)
        s.update(y=8)
        self.assertEqual(s.y, 8)

    def test_update_kwargs_multiple(self):
        s = Square(10, 2, 3)
        s.update(size=5, x=7, y=8, id=89)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 8)
        self.assertEqual(s.id, 89)

    def test_update_kwargs_invalid_key(self):
        s = Square(10, 2, 3)
        with self.assertRaises(AttributeError):
            s.update(invalid_key=42)


class TestSquareToDictionary(unittest.TestCase):
    """
    Unittests for testing the to_dictionary() method of the Square class.
    """

    def test_to_dictionary(self):
        s = Square(10, 2, 3, 4)
        s_dict = s.to_dictionary()
        expected_dict = {'id': 4, 'size': 10, 'x': 2, 'y': 3}
        self.assertEqual(s_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
