from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**kwargs):

        if not email:
            raise ValueError("Email field is required")

        user = self.model(email=email,**kwargs)
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self,email,password,**kwargs):
        kwargs.setdefault("is_staff",True)
        kwargs.setdefault("is_superuser",True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email,password,**kwargs)


class DateAbstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True



class CustomUser(AbstractBaseUser,PermissionsMixin,DateAbstract):
    firt_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(unique=True)


    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):
        return self.email
