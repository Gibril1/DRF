from django.db import models
from django.contrib.auth import models as auth_models
# Create your models here.

class UserManager(auth_models.BaseUserManager):
    def create_user(self, first_name:str, last_name:str, email:str,age:int, password:str = None,  is_staff = False, is_superuser = False) -> 'User':
        if not email:
            raise ValueError('User must have email')
        if not first_name:
            raise ValueError('User must have first_name')
        if not last_name:
            raise ValueError('User must have last_name')
        
        user = self.model(email = self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.age = age
        user.set_password(password)
        user.is_active = True
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.save()

        return user

    
    def create_superuser(self, first_name:str, last_name:str, email:str, password:str) -> 'User':
        user = self.create_user(
            first_name= first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,

        )

        return user


    

class User(auth_models.AbstractUser):
    first_name = models.CharField(verbose_name='First Name', max_length=255)
    last_name = models.CharField(verbose_name='Last Name', max_length=255)
    email = models.EmailField(verbose_name='Email', unique=True, max_length=255)
    password = models.CharField(verbose_name='Password', max_length=255)
    age = models.IntegerField(verbose_name='Age', default=0)
    username = None

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']