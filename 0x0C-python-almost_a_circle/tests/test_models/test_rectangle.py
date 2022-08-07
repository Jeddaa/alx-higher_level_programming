#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
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
    
    def test_width_getter(self):
        """Test gettin width"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.width, 8)

    def test_width_setter(self):
        """Test setting width"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        rec1.width = 10
        self.assertEqual(rec1.width, 10)

    def test_height_getter(self):
        """Test getting height"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.height, 18)

    def test_height_setter(self):
        """Test settin height"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        rec1.height = 12
        self.assertEqual(rec1.height, 12)

    def test_x_getter(self):
        """Test getting x"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.x, 2)
    
    def test_x_setter(self):
        """Test setting x"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        rec1.x = 3
        self.assertEqual(rec1.x, 3)

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
