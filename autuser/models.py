from django.contrib.auth.models import UserManager, PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils import timezone


# Create your models here.
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, default='')
    user_name = models.CharField(max_length=255, unique=True ,default='')
    first_name = models.CharField(max_length=50, blank=True, default='')
    last_name = models.CharField(max_length=50, blank=True, default='')
    additional_name = models.CharField(max_length=50, blank=True, default='')
    title = models.CharField(max_length=50, blank=True, default='')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True ,default='../static/icons/Default_Profile_Picture.png')
    background_picture = models.ImageField(upload_to='background_pictures/', null=True, blank=True)
    country = models.CharField(max_length=50, blank=True, default='')
    city = models.CharField(max_length=50, blank=True, default='')


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'user_name'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
