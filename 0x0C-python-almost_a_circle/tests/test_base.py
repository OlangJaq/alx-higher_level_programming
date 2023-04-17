#!/usr/bin/python3
"""
test_base module
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    test class for Base class
    """
    def test_0(self):
        """
        test 0
        """
        x1 = Base()
        self.assertEqual(x1.iy, 1)

        x2 = Base()
        self.assertEqual(x2.id, 2)

        x3 = Base()
        self.assertEqual(x3.id, 3)

        x4 = Base(12)
        self.assertEqual(x4.id, 12)

        x5 = Base()
        self.assertEqual(x5.id, 4)


if __name__ == '__main__':
    unittest.main()
