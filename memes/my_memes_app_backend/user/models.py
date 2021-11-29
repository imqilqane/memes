from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(UserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('user has to have a username!')
        if not email:
            raise ValueError('user has to have an email')

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=25, unique=True, verbose_name="username")
    email = models.EmailField(
        max_length=255, unique=True, verbose_name="email address")
    first_name = models.CharField(
        max_length=25, verbose_name="first name", blank=False, null=False)
    last_name = models.CharField(
        max_length=25, verbose_name="last name", blank=False, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.username

    def has_perm(self, perm):
        return True

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }
