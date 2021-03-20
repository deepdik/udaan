from django.contrib.auth import password_validation


def validate_password(value):
    password_validation.validate_password(value)
