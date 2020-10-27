#!/usr/bin/python
import unittest
from source import validate_even
from django.core.exceptions import ValidationError

class TestValidateEven(unittest.TestCase):
  def test_basic(self):
    self.assertRaises(ValidationError, validate_even, 3)

unittest.main()