from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, AbstractUser
)

# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    nickname=models.CharField(max_length=255,blank=True,null=True)
    active=models.BooleanField(default=True)
    staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELD=[]
    
    def __str__(self):
        return self.email
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_superuser(self):
        return self.admin
    
    #가독성 좋게 하려고 사용한다는데 넣는게 맞는지 모르겠음
    User.is_staff()
    User.is_staff
    