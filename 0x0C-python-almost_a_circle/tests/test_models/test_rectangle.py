#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Define unittests for rectangle"""
    def test_rectangle_isinstance_base(self):
        """Test if Rectangle is an instance of Base"""
        self.assertIsInstance(Rectangle(13, 9), Base)

    def test_rectangle_with_no_id_args(self):
        """testing with no value"""
        self.assertEqual(Rectangle(10, 2).id, 1)

    def test_multiple_rectangle(self):
        """Test without a value for id multiple times"""
        rec1 = Rectangle(8, 18)
        rec2 = Rectangle(12, 9)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_multiple_rectangle(self):
        """Test without a value for id multiple times"""
        rec1 = Rectangle(8, 18)
        rec2 = Rectangle(12, 9)
        self.assertEqual(rec1.id, 1)
        self.assertEqual(rec2.id, 2)

    def test_rectangle_with_no_args(self):
        """testing with no argument in rectangle()"""
        with self.assertRaises(TypeError):
            print(Rectangle())

    def test_rectangle_with_one_args(self):
        """testing with only one argument in rectangle()"""
        with self.assertRaises(TypeError):
            print(Rectangle(10))

    

    
