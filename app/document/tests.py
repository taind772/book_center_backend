import unittest
# Create your tests here.

from .validators import validate_year
from django.core.validators import ValidationError


class TestValidateYear(unittest.TestCase):
    def test_negative_argv(self):
        self.assertRaises(ValidationError, validate_year, -1)

    def test_big_argv(self):
        self.assertRaises(ValidationError, validate_year, 2022)

    def test_acceptable_argv(self):
        self.assertEqual(validate_year(2015), None)

    def test_currentYear_argv(self):
        self.assertEqual(validate_year(2020), None)


unittest.main()
