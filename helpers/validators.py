import re
from django.core.exceptions import ValidationError

def phone_validator(value):
    pattern = r'^\+998\d{9}$'
    if not re.match(pattern, value):
        raise ValidationError("ㅅelefon raqam hato formatda yuborildi +998XXXXXXXXX")
