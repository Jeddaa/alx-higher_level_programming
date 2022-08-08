#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_(unittest.TestCase):
    """Define unittests for square"""
    def test_square_with_no_args(self):
        """testing with no argument in square()"""
        with self.assertRaises(TypeError):
            print(Square())

    def test_square_with_one_arg(self):
        """testing with one argument"""
        sq = Square(13)
        self.assertEqual(str(sq), "[Square] (1) 0/0- 13)")

