import datetime
from django.core.exceptions import ValidationError


def validate_year(year):
    if year < 1900 or year > datetime.date.today().year:
        raise ValidationError('{} is invalid year.'.format(year))
