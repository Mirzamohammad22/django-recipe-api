from django.db import models
from django.contrib.auth.models import PermissionsMixin,BaseUserManager,AbstractBaseUser
# Create your models here.



class UserManager(BaseUserManager):

    def create(self,email,password,**extra_fields):
        if not email:
            raise ValueError("NO EMAIL PASSED")

        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(self._db)
        return user

    def create_superuser(self,email,password):
        user = self.create(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
