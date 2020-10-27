from django.core.exceptions import ValidationError


def validate_even(value):
  if value % 2 == 0:
    raise ValidationError('{value} is not an even number')