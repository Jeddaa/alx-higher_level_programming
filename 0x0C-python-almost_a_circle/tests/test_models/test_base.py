#!/usr/bin/python3
"""Unittests for base."""


import unittest
Base = __import__ ('models.base').Base


class TestBase(unittest.TestCase):
    """Define unittests for base"""

    def test_base_without_id_value(self):
        """Test without a value for id"""
        b1 = Base()
        self.assertEqual(b1.id(), 1)
    
    def test_base_with_id_value(self):
        """Test with a value for id"""
        b1 = Base()
        self.assertEqual(b1.id(12), 12)
    
    def test_base_without_id_value(self):
        """Test without a value for id multiple times"""
        b1 = Base()
        b1.id()
        b1.id()
        self.assertEqual(b1.id(), 2)
