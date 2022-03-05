import re

from django.core.exceptions import ValidationError


def only_letters_numbers_underscore_validator(value):
    regex = "^[A-Za-z0-9_]*$"
    match = re.match(regex, value)
    pass
    if not match:
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


def min_length_validator(value):
    min_length = 2
    if len(value) < min_length:
        raise ValidationError('Name shorter than expected!')


def below_zero_validator(value):
    if value < 0:
        raise ValidationError('The value cannot be below 0!')
