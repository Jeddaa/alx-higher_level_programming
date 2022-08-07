#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_(unittest.TestCase):
    """Define unittests for rectangle"""
    def test_rectangle_isinstance_base(self):
        """Test if Rectangle is an instance of Base"""
        self.assertIsInstance(Rectangle(13, 9), Base)

    def test_rectangle_with_no_args(self):
        """testing with no argument in rectangle()"""
        with self.assertRaises(TypeError):
            print(Rectangle())

    def test_rectangle_with_one_args(self):
        """testing with only one argument in rectangle()"""
        with self.assertRaises(TypeError):
            print(Rectangle(10))

    def test_rectangle_with_two_args(self):
        """Test with two arguments"""
        rec1 = Rectangle(8, 18)
        rec2 = Rectangle(12, 9)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_multiple_rectangle(self):
        """Test with two arguments"""
        rec1 = Rectangle(8, 18)
        rec2 = Rectangle(12, 9)
        self.assertEqual(rec1.id, 1)
        self.assertEqual(rec2.id, 2)

    def test_rectangle_with_three_args(self):
        """Test with three arguments"""
        rec1 = Rectangle(8, 18, 2)
        rec2 = Rectangle(12, 9, 3)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_rectangle_with_four_args(self):
        """Test with four arguments"""
        rec1 = Rectangle(8, 18, 2, 1)
        rec2 = Rectangle(12, 9, 3, 2)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_with_five_args(self):
        """Test with five arguments"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.id, 2)

    def test_with_morethan_five_args(self):
        """Test with more than five arguments"""
        with self.assertRaises(TypeError):
            print(Rectangle(8, 18, 2, 0, 2, 6).id)

    def test_private_width(self):
        """Test width as a private instance attribute"""
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 18, 2, 0, 2).__width)

    def test_private_height(self):
        """Test height as a private instance attribute"""
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 18, 2, 0, 2).__height)
    
    def test_private_x(self):
        """Test x as a private instance attribute"""
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 18, 2, 0, 2).__x)
    
    def test_private_y(self):
        """Test y as a private instance attribute"""
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 18, 2, 0, 2).__y)
    
    def test_private_id(self):
        """Test id as a private instance attribute"""
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 18, 2, 0, 2).__id)

    

    def test_y_getter(self):
        """Test gettin y"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.y, 0)

    def test_y_setter(self):
        """Test setting y"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        rec1.y = 1
        self.assertEqual(rec1.y, 1)

    def test_id_getter(self):
        """Test gettin id"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.id, 2)

    def test_id_setter(self):
        """Test setting id"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        rec1.id = 3
        self.assertEqual(rec1.id, 3)

class TestRectangle_width(unittest.TestCase):
    def test_width_getter(self):
        """Test gettin width"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.width, 8)

    def test_width_setter(self):
        """Test setting width"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        rec1.width = 10
        self.assertEqual(rec1.width, 10)

    def test_width_as_float(self):
        """Test width as float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(3.8, 18, 2, 0, 2).width)

    def test_width_as_string(self):
        """Test width as string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle("hey", 18, 2, 0, 2).width)

    def test_width_as_zero(self):
        """Test width as zero"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            print(Rectangle(0, 18, 2, 0, 2).width)

    def test_width_as_negative(self):
        """Test width as negative value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            print(Rectangle(-5, 18, 2, 0, 2).width)

    def test_width_as_bool(self):
        """Test width as bool"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(True, 18, 2, 0, 2).width)

    def test_width_as_inf(self):
        """Test width as inf"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(float('inf'), 18, 2, 0, 2).width)
    
    def test_width_as_NaN(self):
        """Test width as NaN"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(float('NaN'), 18, 2, 0, 2).width)
    
    def test_width_as_list(self):
        """Test width as list"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle([10], 18, 2, 0, 2).width)

    def test_width_as_set(self):
        """Test width as set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle({10}, 18, 2, 0, 2).width)

    def test_width_as_byte(self):
        """Test width as byte"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(b'baboon', 18, 2, 0, 2).width)

    def test_width_as_frozenSet(self):
        """Test width as frozen set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(frozenset({1, 2, 3}), 18, 2, 0, 2).width)

class TestRectangle_height(unittest.TestCase):
    def test_height_getter(self):
        """Test getting height"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.height, 18)

    def test_height_setter(self):
        """Test settin height"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        rec1.height = 12
        self.assertEqual(rec1.height, 12)

    def test_heigt_as_float(self):
        """Test height as float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, 4.8, 2, 0, 2).height)

    def test_height_as_string(self):
        """Test height as string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, "hey", 2, 0, 2).height)

    def test_height_as_zero(self):
        """Test height as zero"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            print(Rectangle(18, 0, 2, 0, 2).height)

    def test_height_as_negative(self):
        """Test height as negative value"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            print(Rectangle(18, -5, 2, 0, 2).height)

    def test_height_as_bool(self):
        """Test height as bool"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, True, 2, 0, 2).height)

    def test_height_as_inf(self):
        """Test height as inf"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, float('inf'), 2, 0, 2).height)
    
    def test_height_as_NaN(self):
        """Test height as NaN"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, float('NaN'), 2, 0, 2).height)
    
    def test_height_as_list(self):
        """Test height as list"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, [10], 2, 0, 2).height)

    def test_height_as_set(self):
        """Test height as set"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, {10}, 2, 0, 2).height)

    def test_height_as_byte(self):
        """Test height as byte"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, b'baboon', 2, 0, 2).height)

    def test_height_as_frozenSet(self):
        """Test height as frozen set"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, frozenset({1, 2, 3}), 2, 0, 2).height)

class TestRectangle_x(unittest.TestCase):
    def test_x_getter(self):
        """Test getting x"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.x, 2)
    
    def test_x_setter(self):
        """Test setting x"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        rec1.x = 3
        self.assertEqual(rec1.x, 3)

    def test_x_as_zero(self):
        """Test x as zero"""
        rec1 = Rectangle(8, 18, 0, 2, 2)
        self.assertEqual(rec1.x, 0)
    
    def test_x_as_float(self):
        """Test x as float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, 20, 4.8, 2).x)

    def test_x_as_string(self):
        """Test x as string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, 2, "hey", 2, 1).x)

    def test_x_as_negative(self):
        """Test x as negative value"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            print(Rectangle(10, 9, -5, 0, 2).x)

    def test_x_as_bool(self):
        """Test x as bool"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(10, 8, True, 0, 2).x)

    def test_x_as_inf(self):
        """Test x as inf"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(10, 7,  float('inf'), 2, 1).x)
    
    def test_x_as_NaN(self):
        """Test x as NaN"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(11, 6, float('NaN'), 2, 2).x)
    
    def test_x_as_list(self):
        """Test x as list"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(12, 8, [10], 0, 2).x)

    def test_x_as_set(self):
        """Test x as set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(12, 8, {3}, 0, 2).x)

    def test_x_as_byte(self):
        """Test x as byte"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(12, 8, b'tired', 0, 2).x)

    def test_x_as_frozenSet(self):
        """Test x as frozen set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(9, 12, frozenset({1, 2, 3}), 0, 2).x)
