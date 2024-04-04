from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from .manager import CustomUserManager
# Create your models here.
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


class Roles(models.Model):
    USER = 1
    MICROSERVICEUSER = 2
    TYPE_CHOICES = (
        (USER, 'User'),
        (MICROSERVICEUSER, 'Microserviceuser')
    )
    id = models.PositiveIntegerField(choices=TYPE_CHOICES, primary_key=True)
    
    def __str__(self):
        return self.get_id_display()

class CustomUser(AbstractUser):
    username = None
    # username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    
    # is_microserviceuser = models.BooleanField(default=False)
    # is_user = models.BooleanField(default=True)
    
    # type = (
    #     (1, 'user'),
    #     (2, 'microserviceuser')
    # )
    # role = models.IntegerField(choices = type, default=1)
    
    role = models.ManyToManyField(Roles)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

class BaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()