class TestRectangle_x(unittest.TestCase):
    def test_heigth_as_float(self):
        """Test x as float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, 4.8, 2, 0, 2).x)

    def test_x_as_string(self):
        """Test x as string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, "hey", 2, 0, 2).x)

    def test_x_as_zero(self):
        """Test x as zero"""
        with self.assertRaisesRegex(ValueError, "x must be > 0"):
            print(Rectangle(18, 0, 2, 0, 2).x)

    def test_x_as_negative(self):
        """Test x as negative value"""
        with self.assertRaisesRegex(ValueError, "x must be > 0"):
            print(Rectangle(18, -5, 2, 0, 2).x)

    def test_x_as_bool(self):
        """Test x as bool"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, True, 2, 0, 2).x)

    def test_x_as_inf(self):
        """Test x as inf"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, float('inf'), 2, 0, 2).x)
    
    def test_x_as_NaN(self):
        """Test x as NaN"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, float('NaN'), 2, 0, 2).x)
    
    def test_x_as_list(self):
        """Test x as list"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, [10], 2, 0, 2).x)

    def test_x_as_set(self):
        """Test x as set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, {10}, 2, 0, 2).x)

    def test_x_as_byte(self):
        """Test x as byte"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, b'baboon', 2, 0, 2).x)

    def test_x_as_frozenSet(self):
        """Test x as frozen set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, frozenset({1, 2, 3}), 2, 0, 2).x)
