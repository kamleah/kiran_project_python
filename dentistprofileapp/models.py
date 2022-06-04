from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class DentistRegistration(BaseUserManager):
    def create_user(self,name, payment, password):

        user=self.model(
            name = name,
            payment = payment,
            password =password,
            )
        user.is_admin = False
        user.set_password(password)
        user.save(using=self._db)
        return user

class Registration(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=250,blank=False)
    password = models.TextField(max_length=250,blank=False)
    payment = models.IntegerField()
    objects=DentistRegistration()
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.TextField(max_length=250,blank=False)
    lastname = models.TextField(max_length=250,blank=False)
    gender = models.TextField(max_length=250,blank=False)
    image = models.TextField(max_length=250,blank=False)
    address = models.TextField(max_length=1000,blank=False)
    

