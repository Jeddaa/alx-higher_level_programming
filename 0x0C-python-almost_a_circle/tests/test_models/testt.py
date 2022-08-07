class TestRectangle_y(unittest.TestCase):
    def test_y_as_zero(self):
        """Test y as zero"""
        rec1 = Rectangle(8, 18, 0, 2, 2)
        self.assertEqual(rec1.y, 0)
    
    def test_y_as_float(self):
        """Test y as float"""
        with self.assertRaisesRegey(TypeError, "y must be an integer"):
            print(Rectangle(18, 20, 4.8, 2).y)

    def test_y_as_string(self):
        """Test y as string"""
        with self.assertRaisesRegey(TypeError, "y must be an integer"):
            print(Rectangle(18, 2, "hey", 2, 1).y)

    def test_y_as_negative(self):
        """Test y as negative value"""
        with self.assertRaisesRegey(ValueError, "y must be >= 0"):
            print(Rectangle(10, 9, -5, 0, 2).y)

    def test_y_as_bool(self):
        """Test y as bool"""
        with self.assertRaisesRegey(TypeError, "y must be an integer"):
            print(Rectangle(10, 8, True, 0, 2).y)

    def test_y_as_inf(self):
        """Test y as inf"""
        with self.assertRaisesRegey(TypeError, "y must be an integer"):
            print(Rectangle(10, 7,  float('inf'), 2, 1).y)
    
    def test_y_as_NaN(self):
        """Test y as NaN"""
        with self.assertRaisesRegey(TypeError, "y must be an integer"):
            print(Rectangle(11, 6, float('NaN'), 2, 2).y)
    
    def test_y_as_list(self):
        """Test y as list"""
        with self.assertRaisesRegey(TypeError, "y must be an integer"):
            print(Rectangle(12, 8, [10], 0, 2).y)

    def test_y_as_set(self):
        """Test y as set"""
        with self.assertRaisesRegey(TypeError, "y must be an integer"):
            print(Rectangle(12, 8, {3}, 0, 2).y)

    def test_y_as_byte(self):
        """Test y as byte"""
        with self.assertRaisesRegey(TypeError, "y must be an integer"):
            print(Rectangle(12, 8, b'tired', 0, 2).y)

    def test_y_as_frozenSet(self):
        """Test y as frozen set"""
        with self.assertRaisesRegey(TypeError, "y must be an integer"):
            print(Rectangle(9, 12, frozenset({1, 2, 3}), 0, 2).y)
