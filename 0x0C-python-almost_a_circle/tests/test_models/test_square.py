#!/usr/bin/python3
"""Defines unittests for model square.py."""
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittest instantiation of the Square class."""

    def test_isbase(self):
        self.assertIsInstance(Square(10), Base)

    def test_isrectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_noargs(self):
        with self.assertRaises(TypeError):
            Square()

    def test_args(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(1, 2, 3)
        s3 = Square(1, 2)
        s4 = Square(1)
        self.assertEqual(s1.id, s1.id)
        self.assertEqual(s2.id, s2.id)
        self.assertEqual(s3.id, s3.id)
        self.assertEqual(s4.id, s4.id)
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


class TestSquare_area(unittest.TestCase):
    """Unittests area method of the Square class."""

    def test_small_area(self):
        s = Square(10, 2, 0, 0)
        self.assertEqual(100, s.area())

    def test_large_area(self):
        s = Square(999999999, 999999999, 0, 0)
        self.assertEqual(999999998000000001, s.area())

    def test_arg(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)

    def test_attr_changed(self):
        s = Square(2, 10, 1, 1)
        s.width = 7
        s.height = 7
        self.assertEqual(49, s.area())


class TestSquare_str(unittest.TestCase):
    """Unittests __str__ method."""

    def test_size_x(self):
        s = Square(10, 8)
        output = "[Square] ({}) 8/0 - 10".format(s.id)
        self.assertEqual(output, s.__str__())

    def test_size_x_y(self):
        s = Square(10, 8, 1)
        output = "[Square] ({}) 8/1 - 10".format(s.id)
        self.assertEqual(output, s.__str__())

    def test_size_x_y_id(self):
        s = Square(10, 8, 1, 7)
        output = "[Square] ({}) 8/1 - 10".format(s.id)
        self.assertEqual(output, s.__str__())

    def test_arg(self):
        s = Square(10, 8, 1, 89)
        with self.assertRaises(TypeError):
            s.__str__(1)


class TestSquare_display(unittest.TestCase):
    """Unittests display of square."""

    def test_arg(self):
        s = Square(10, 8, 7, 89)
        with self.assertRaises(TypeError):
            s.display(1)


class TestSquare_update(unittest.TestCase):
    """Unittest update method of the square class."""

    def test_no_update(self):
        s = Square(10, 8, 7, 89)
        s.update()
        self.assertEqual("[Square] (89) 8/7 - 10", str(s))

    def test_update_id_arg(self):
        s = Square(10, 8, 7, 89)
        s.update(49)
        self.assertEqual("[Square] (49) 8/7 - 10", str(s))

    def test_update_width_arg(self):
        s = Square(10, 8, 7, 89)
        s.update(49, 49)
        self.assertEqual("[Square] (49) 8/7 - 49", str(s))

    def test_update_height_arg(self):
        s = Square(10, 8, 7, 89)
        s.update(49, 49, 49)
        self.assertEqual("[Square] (49) 49/7 - 49", str(s))

    def test_update_x_arg(self):
        s = Square(10, 8, 7, 89)
        s.update(49, 49, 49, 49)
        self.assertEqual("[Square] (49) 49/49 - 49", str(s))

    def test_update_arg_twice(self):
        s = Square(10, 8, 7, 89)
        s.update(49, 49, 49, 49)
        s.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(s))

    def test_update_id_arg_None(self):
        s = Square(10, 8, 7, 89)
        s.update(None)
        self.assertEqual("[Square] (None) 8/7 - 10", str(s))

    def test_update_id_kwarg(self):
        s = Square(10, 8, 7, 89)
        s.update(id=49)
        self.assertEqual("[Square] (49) 8/7 - 10", str(s))

    def test_update_width_kwarg(self):
        s = Square(10, 8, 7, 89)
        s.update(size=49, id=49)
        self.assertEqual("[Square] (49) 8/7 - 49", str(s))

    def test_update_height_kwarg(self):
        s = Square(10, 8, 7, 89)
        s.update(size=49, x=49, id=49)
        self.assertEqual("[Square] (49) 49/7 - 49", str(s))

    def test_update_x_kwarg(self):
        s = Square(10, 8, 7, 89)
        s.update(y=49, x=49, size=9, id=49)
        self.assertEqual("[Square] (49) 49/49 - 9", str(s))

    def test_update_kwarg_twice(self):
        s = Square(10, 8, 7, 89)
        s.update(x=49, y=49, size=49, id=49)
        s.update(x=4, y=5, size=3, id=1)
        self.assertEqual("[Square] (1) 4/5 - 3", str(s))

    def test_update_id_kwarg_None(self):
        s = Square(10, 8, 7, 89)
        s.update(id=None)
        self.assertEqual("[Square] (None) 8/7 - 10", str(s))

    def test_update_kwargs_args(self):
        s = Square(10, 8, 7, 89)
        s.update(49, 4, x=3, size=5)
        self.assertEqual("[Square] (49) 8/7 - 4", str(s))

    def test_update_wrong_kwargs(self):
        s = Square(10, 8, 7, 89)
        s.update(alx=49, fethi=4)
        self.assertEqual("[Square] (89) 8/7 - 10", str(s))

    def test_update_mixed_kwargs(self):
        s = Square(10, 8, 7, 89)
        s.update(alx=4, id=49, fethi=15, x=0, y=5, size=3)
        self.assertEqual("[Square] (49) 0/5 - 3", str(s))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests to dictionary method of the square class."""

    def test_output(self):
        s = Square(10, 8, 7, 89)
        output = {'x': 8, 'y': 7, 'id': 89, 'size': 10}
        self.assertEqual(output, s.to_dictionary())

    def test_no_changes(self):
        s1 = Square(10, 8, 7, 89)
        s2 = Square(1, 2, 4, 5)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_arg(self):
        s = Square(10, 8, 7, 89)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
