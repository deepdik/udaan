"""
Provide model user and user-account related models.
"""
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from dukaan.libs.accounts.validators import validate_password


class UserManager(BaseUserManager):
    def create_user(self, password=None, **kwargs):
        # email = self.normalize_email(email)
        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    """
    Store User account details.
    """
    SELLER, CUSTOMER = '1' , '2'
    USER_TYPE = (
        (SELLER, 'seller'),
        (CUSTOMER, 'cunsumer')
        )
    # Use either of the username fields below:
    mobile_no = models.EmailField(
        _('mobile_number'),
        max_length=255,
        unique=True,
        error_messages={
            'unique': _('A user with this number already exists.'),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active.  Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    address = models.CharField(max_length=400, blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE)
    objects = UserManager()

    # Modify USERNAME_FIELD and REQUIRED_FIELDS as required.
    USERNAME_FIELD = 'mobile_no'

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        db_table = 'auth_user'
        permissions = (

        )

    # Use Either one of __str__ methods.
    def __str__(self):
        return '{}'.format(self.mobile_no)
