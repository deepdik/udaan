import re

from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import CommonPasswordValidator
from django.utils.translation import ugettext as _


class MinMaxPasswordValidator(object):
    def __init__(self, min_length=6, max_length=20):
        self.regex = r'(^.*(?=.{6,})(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*-+=/(){}]).*$)'
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("This password must contain at least %(min_length)d characters."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

        if len(password) > self.max_length:
            raise ValidationError(
                _("This password must contain at most %(max_length)d characters."),
                code='password_too_long',
                params={'max_length': self.max_length},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_length)d and at most %(max_length)d characters."
            % {'min_length': self.min_length, 'max_length': self.max_length}
        )


class CasePasswordValidator(object):
    """
    """
    def __init__(self):
        self.lower_case_regex = r'(^.*(?=.*[a-z]).*$)'
        self.upper_case_regex = r'(^.*(?=.*[A-Z]).*$)'

    def validate(self, password, user=None):
        if not re.match(self.lower_case_regex, password):
            raise ValidationError(
                _("This password must contain at least one %(lower_case)s characters."),
                code='password_missing_lower_case',
                params={'lower_case': 'lower_case'},
            )

        if not re.match(self.upper_case_regex, password):
            raise ValidationError(
                _("This password must contain at least one %(upper_case)s character."),
                code='password_missing_upper_case',
                params={'upper_case': 'upper_case'},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least one %(lower_case)s character and one %(upper_case)s character."
            % {'lower_case': 'lower_case', 'upper_case': 'upper_case'}
        )


class NumberPasswordValidator(object):
    """
    """
    def __init__(self):
        self.number_regex = r'(^.*(?=.*[0-9]).*$)'

    def validate(self, password, user=None):
        if not re.match(self.number_regex, password):
            raise ValidationError(
                _("This password must contain at least one %(numberic)s character."),
                code='password_missing_numberic',
                params={'numberic': 'numberic'},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least one %(numberic)s character."
            % {'numberic': 'numberic'}
        )


class SpecialCharacterPasswordValidator(object):
    """
    """
    def __init__(self):
        self.special_char_regex = r'(^.*(?=.*[!@#$%^&*-+=/(){}]).*$)'

    def validate(self, password, user=None):
        if not re.match(self.special_char_regex, password):
            raise ValidationError(
                _("This password must contain at least one %(special)s character %(special_char)s"),
                code='password_missing_special',
                params={'special': 'special', 'special_char': '!@#$%^&*-+=/(){}'},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least one %(special)s character %(special_char)s"
            % {'special': 'special', 'special_char': '!@#$%^&*-+=/(){}'}
        )



class CustomCommonPasswordValidator(CommonPasswordValidator):
   """
   """

   def validate(self, password, user=None):
       if password.lower().strip() in self.passwords:
           raise ValidationError(
               _("The password is too common."),
               code='password_too_common',
           )
