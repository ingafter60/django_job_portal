# users/models.py

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

# User Manager
class UserManager(BaseUserManager):
    # Use UserManager whenever migrations
    use_in_migrations = True

    # Check email and password
    def _create_user(self,email,password,**extra_fields):
        # If no email, raise error
        if not email:
            raise ValueError('Your email is not correct!')

        # If there is email and password 
        email   = self.normalize_email(email)
        user    = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Create user if email and passord (def _create_user) are ok, and password=None
    def create_user(self, email, password=None, **extra_fields):
        # Create users (employee, employer), but NOT SUPERUSER
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, **extra_fields)

    # Create superuser    
    def create_superuser(self, email, password, **extra_fields):
        # If superuser, its ok
        extra_fields.setdefault('is_superuser',True)
        # If not superuser, raise error
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self._create_user(email,password,**extra_fields)

# Account models
class Account(AbstractBaseUser, PermissionsMixin):
    email       = models.EmailField(_('email address'), unique=True)
    first_name  = models.CharField(_('first name'), max_length=50, blank=True)
    last_name   = models.CharField(_('last name'), max_length=50, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active   = models.BooleanField(_('active'), default=True)
    is_staff    = models.BooleanField(_('is_staff'), default=False)
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')