from django.db import models
from django.contrib.auth.models import AbstractUser ,BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,email,password=None , **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(
            email=email ,
            **extra_fields

        )
        #haasing password
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,email,password=None ,**extra_fields):
        extra_fields.setdefault("is_staff" ,True)
        extra_fields.setdefault("is_superuser" ,True)
        extra_fields.setdefault("is_active" ,True)

        # if extra_fields.get("is_staff") is not None:

        return self.create_user(
            email=email,
            password=password,
            **extra_fields
        )
           

class CustomeUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
