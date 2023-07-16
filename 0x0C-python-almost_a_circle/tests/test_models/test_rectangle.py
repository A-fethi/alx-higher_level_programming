#!/usr/bin/python3
"""Defines unittests for model rectangle.py."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittest instantiation of the Rectangle class."""

    def test_isbase(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_noargs(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_args(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(1, 2, 3)
        r4 = Rectangle(1, 2)
        self.assertEqual(r1.id, r1.id)
        self.assertEqual(r2.id, r2.id)
        self.assertEqual(r3.id, r3.id)
        self.assertEqual(r4.id, r4.id)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)


class TestRectangle_area(unittest.TestCase):
    """Unittests area method of the Rectangle class."""

    def test_small_area(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_large_area(self):
        r = Rectangle(999999999, 999999999, 0, 0, 0)
        self.assertEqual(999999998000000001, r.area())

    def test_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

    def test_attr_changed(self):
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 7
        self.assertEqual(49, r.area())


class TestRectangle_str(unittest.TestCase):
    """Unittests __str__ method."""

    def test_w_h_x(self):
        r = Rectangle(10, 8, 1)
        output = "[Rectangle] ({}) 1/0 - 10/8".format(r.id)
        self.assertEqual(output, r.__str__())

    def test_w_h_x_y(self):
        r = Rectangle(10, 8, 1, 7)
        output = "[Rectangle] ({}) 1/7 - 10/8".format(r.id)
        self.assertEqual(output, r.__str__())

    def test_w_h_x_y_id(self):
        r = Rectangle(10, 8, 1, 7, 89)
        output = "[Rectangle] ({}) 1/7 - 10/8".format(r.id)
        self.assertEqual(output, r.__str__())

    def test_arg(self):
        r = Rectangle(10, 8, 1, 7, 89)
        with self.assertRaises(TypeError):
            r.__str__(1)


class TestRectangle_display(unittest.TestCase):
    """Unittests display of recrangle."""

    def test_arg(self):
        r = Rectangle(10, 8, 1, 7, 89)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_update(unittest.TestCase):
    """Unittest update method of the rectangle class."""

    def test_no_update(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update()
        self.assertEqual("[Rectangle] (89) 1/7 - 10/8", str(r))

    def test_update_id_arg(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(49)
        self.assertEqual("[Rectangle] (49) 1/7 - 10/8", str(r))

    def test_update_width_arg(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(49, 49)
        self.assertEqual("[Rectangle] (49) 1/7 - 49/8", str(r))

    def test_update_height_arg(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(49, 49, 49)
        self.assertEqual("[Rectangle] (49) 1/7 - 49/49", str(r))

    def test_update_x_arg(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(49, 49, 49, 49)
        self.assertEqual("[Rectangle] (49) 49/7 - 49/49", str(r))

    def test_update_y_arg(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(49, 49, 49, 49, 49)
        self.assertEqual("[Rectangle] (49) 49/49 - 49/49", str(r))

    def test_update_arg_twice(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(49, 49, 49, 49, 49)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", str(r))

    def test_update_id_arg_None(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(None)
        self.assertEqual("[Rectangle] (None) 1/7 - 10/8", str(r))

    def test_update_id_kwarg(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(id=49)
        self.assertEqual("[Rectangle] (49) 1/7 - 10/8", str(r))

    def test_update_width_kwarg(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(width=49, id=49)
        self.assertEqual("[Rectangle] (49) 1/7 - 49/8", str(r))

    def test_update_height_kwarg(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(width=49, height=49, id=49)
        self.assertEqual("[Rectangle] (49) 1/7 - 49/49", str(r))

    def test_update_x_kwarg(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(x=49, width=49, height=49, id=49)
        self.assertEqual("[Rectangle] (49) 49/7 - 49/49", str(r))

    def test_update_y_kwarg(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(x=49, y=49, width=49, height=49, id=49)
        self.assertEqual("[Rectangle] (49) 49/49 - 49/49", str(r))

    def test_update_kwarg_twice(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(x=49, y=49, width=49, height=49, id=49)
        r.update(x=4, y=5, width=2, height=3, id=1)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", str(r))

    def test_update_id_kwarg_None(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(id=None)
        self.assertEqual("[Rectangle] (None) 1/7 - 10/8", str(r))

    def test_update_kwargs_args(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(49, 4, 3, width=6, height=5)
        self.assertEqual("[Rectangle] (49) 1/7 - 4/3", str(r))

    def test_update_wrong_kwargs(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(alx=49, fethi=4)
        self.assertEqual("[Rectangle] (89) 1/7 - 10/8", str(r))

    def test_update_mixed_kwargs(self):
        r = Rectangle(10, 8, 1, 7, 89)
        r.update(alx=4, id=49, fethi=15, x=0, y=5, width=2, height=3)
        self.assertEqual("[Rectangle] (49) 0/5 - 2/3", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests to dictionary method of the rectangle class."""

    def test_output(self):
        r = Rectangle(10, 8, 1, 7, 89)
        output = {'x': 1, 'y': 7, 'id': 89, 'height': 8, 'width': 10}
        self.assertEqual(output, r.to_dictionary())

    def test_no_changes(self):
        r1 = Rectangle(10, 8, 1, 7, 89)
        r2 = Rectangle(1, 2, 3, 4, 5)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_arg(self):
        r = Rectangle(10, 8, 1, 7, 89)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
