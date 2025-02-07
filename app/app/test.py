"""
Smaple tests
"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """test the calc module"""

    def test_add_numbers(self):
        """test adding numbers togather"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11, "Addition doesn't match")

    def test_sub_numbers(self):
        """test substracting numbers togather"""
        res = calc.sub(15, 5)

        self.assertEqual(res, 10, "Substraction doesn't match")