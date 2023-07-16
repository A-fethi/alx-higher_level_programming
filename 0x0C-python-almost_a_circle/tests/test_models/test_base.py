#!/usr/bin/python3
"""Defines unittest for base.py model."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests instantiation of Base class."""

    def test_float(self):
        self.assertEqual(8.6, Base(8.6).id)

    def test_int(self):
        self.assertEqual(49, Base(49).id)

    def test_str(self):
        self.assertEqual("Fethi", Base("Fethi").id)

    def test_bool(self):
        self.assertEqual(False, Base(False).id)

    def test_dict(self):
        self.assertEqual({"f": 4, "e": 9}, Base({"f": 4, "e": 9}).id)

    def test_set(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_list(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_NaN(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_inf(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_Base(self):
        b1 = Base()
        self.assertEqual(b1.id, b1.id)

    def test_multiple_Bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        b5 = Base()
        self.assertEqual(b1.id, b1.id)
        self.assertEqual(b2.id, b2.id)
        self.assertEqual(b3.id, b3.id)
        self.assertEqual(b4.id, b4.id)
        self.assertEqual(b5.id, b5.id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(4, 9)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests to_json_string of Base class."""

    def test_type_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 1)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_type_square(self):
        s = Square(10, 7, 2, 8)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_empty(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string(4, 9)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestBase_save_to_file(unittest.TestCase):
    """Unittests save_to_file of Base class."""
    def test_None(self):
        with open("Square.json", "w") as f:
            f.write("[]")
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_empty(self):
        with open("Square.json", "w") as f:
            f.write("[]")
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_no_args(self):
        with open("Square.json", "w") as f:
            f.write("[]")
            with self.assertRaises(TypeError):
                Square.save_to_file()

    def test_args(self):
        with open("Square.json", "w") as f:
            f.write("[]")
            with self.assertRaises(TypeError):
                Square.save_to_file(4, 9)

    def test_RNone(self):
        with open("Rectangle.json", "w") as f:
            f.write("[]")
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_Rempty(self):
        with open("Rectangle.json", "w") as f:
            f.write("[]")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_Rno_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_Rargs(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(9, 4)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests from_json_string of Base class."""

    def test_empty(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(4, 9)

    def test_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7, "y": 8}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_rectangles(self):
        list_input = [
                {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
                {"id": 1, "width": 4, "height": 10, "x": 8, "y": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_squares(self):
        list_input = [
                {"id": 89, "size": 10, "height": 4},
                {"id": 1, "size": 4, "height": 10}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)


class TestBase_create(unittest.TestCase):
    """Unittests create method of Base class."""

    def test_create_originale(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (5) 2/8 - 10/7", str(r1))

    def test_create_new(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (5) 2/8 - 10/7", str(r2))

    def test_create_NotEqual(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_IsNot(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_soriginale(self):
        s1 = Square(10, 7, 2, 8)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (8) 7/2 - 10", str(s1))

    def test_create_snew(self):
        s1 = Square(10, 7, 2, 8)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (8) 7/2 - 10", str(s2))

    def test_create_sNotEqual(self):
        s1 = Square(10, 7, 2, 8)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)

    def test_create_sIsNot(self):
        s1 = Square(10, 7, 2, 8)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests load from file of Base class."""

    def test_1st_rectangle(self):
        with open("Rectangle.json", "w") as f:
            f.write("[]")
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_2nd_rectangle(self):
        with open("Rectangle.json", "w") as f:
            f.write("[]")
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_1st_square(self):
        with open("Square.json", "w") as f:
            f.write("[]")
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, 5, 6)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_2nd_square(self):
        with open("Square.json", "w") as f:
            f.write("[]")
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, 5, 6)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    def test_no_sfile(self):
        with open("Square.json", "w") as f:
            f.write("[]")
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_no_file(self):
        with open("Rectangle.json", "w") as f:
            f.write("[]")
        output = Rectangle.load_from_file()
        self.assertEqual([], output)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests load from file to csv method of Base class."""

    def test_1st_rectangle(self):
        with open("Rectangle.json", "w") as f:
            f.write("[]")
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_2nd_rectangle(self):
        with open("Rectangle.json", "w") as f:
            f.write("[]")
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_1st_square(self):
        with open("Square.json", "w") as f:
            f.write("[]")
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, 5, 6)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_2nd_square(self):
        with open("Square.json", "w") as f:
            f.write("[]")
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, 5, 6)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
