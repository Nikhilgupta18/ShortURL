from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(url):
    url_validator = URLValidator()
    try:
        url_validator(url)
    except:
        raise ValidationError("Invalid URL")
    return url