#!/usr/bin/python3
"""Unittests for base."""


import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Define unittests for base"""

    def test_base_with_no_args(self):
        """Test without a value for id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
    
    def test_base_with_one_arg(self):
        """Test with a value for id"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
    
    def test_multiple_bases(self):
        """Test without a value for id multiple times"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_multiple_bases(self):
        """Test without a value for id multiple times"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)

    def test_base_with_str(self):
        """Test with a string for id"""
        b1 = Base("hey")
        self.assertEqual(b1.id, hey)

    def test_base_with_str(self):
        """Test with a bool value for id"""
        b1 = Base(True)
        self.assertEqual(b1.id, True)

    def test_base_with_one_floatArg(self):
        """Test with a float value for id"""
        b1 = Base(3.9)
        self.assertEqual(b1.id, 3.9)

    def test_base_with_list(self):
        """Test with a list value for id"""
        b1 = Base([1, "hello", 4])
        self.assertEqual(b1.id,[1, "hello", 4])

    def test_base_with_set(self):
        """Test with a list value for id"""
        b1 = Base({1, "hello", 4})
        self.assertEqual(b1.id,{1, "hello", 4})

    def test_base_with_dict(self):
        """Test with a dictionary value for id"""
        b1 = Base({'num': 1, 'name': "hello", 'age': 4})
        self.assertEqual(b1.id,{'num': 1, 'name': "hello", 'age': 4})


