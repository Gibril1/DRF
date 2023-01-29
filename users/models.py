from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, first_name:str, last_name:str, email:str, password:str, **other_fields) -> 'User':
        if not email:
            raise ValueError('User must have email')
        if not first_name:
            raise ValueError('User must have first_name')
        if not last_name:
            raise ValueError('User must have last_name')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name = first_name,
            last_name = last_name,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    
    def create_superuser(self, first_name:str, last_name:str, email:str, password:str, **other_fields) -> 'User':
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True'
            )
        if other_fields.get('is_active') is not True:
            raise ValueError(
                'Superuser must be assigned to is_active=True'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True'
            )

        user = self.create_user(
            first_name= first_name,
            last_name=last_name,
            email=email,
            password=password,
            **other_fields
        )

        return user


    

class User(AbstractUser):
    first_name = models.CharField(verbose_name='First Name', max_length=255)
    last_name = models.CharField(verbose_name='Last Name', max_length=255)
    email = models.EmailField(verbose_name='Email', unique=True, max_length=255)
    password = models.CharField(verbose_name='Password', max_length=255)
    roles = models.CharField(verbose_name='Role', max_length=255, null=True, default='')
    dob = models.DateField(verbose_name='Date Of Birth', null=True)
    username = models.CharField(unique=True, max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']