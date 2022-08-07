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
        b1.id()
        b2.id()
        self.assertEqual(b1.id, b2.id, 2)

