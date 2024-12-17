"""
Demo writing unit tests 
"""


from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """ I am going to write my first unit test"""
    def test_adding_two_numbers(self):
        res = calc.add_two_numbers(5,5)
        self.assertEqual(res,10)

    def test_substracting_two_numbers(self):
        res = calc.substracting_two_numbers(6,5)
        self.assertEqual(res,1)