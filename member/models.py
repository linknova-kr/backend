from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class MemberManager(BaseUserManager):
  def create_user(self, **kwargs):
    identifier = kwargs.get('identifier')
    password = kwargs.get('password')
    if not identifier:
      raise ValueError('An identifier is required.')
    if not password:
      raise ValueError('A password is required.')
    del kwargs['password']
    user = self.model(**kwargs)
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, **kwargs):
    user = self.create_user(**kwargs)
    user.is_superuser = True
    user.save()
    return user

GENDER = (
  ('M', 'MEN'),
  ('W', 'WOMEN'),
)

class Member(AbstractBaseUser, PermissionsMixin):
  id = models.AutoField(primary_key=True)
  identifier = models.CharField(max_length=50, unique=True)
  name = models.CharField(max_length=50)
  birth_date = models.DateField()
  gender = models.CharField(max_length=1, choices=GENDER)
  email = models.EmailField(max_length=50, null=True, unique=True)
  phone_number = models.CharField(max_length=50)
    
  USERNAME_FIELD = 'identifier'
  REQUIRED_FIELDS = ['name', 'birth_date', 'gender', 'email', 'phone_number']
    
  objects = MemberManager()
  def __str__(self):
    return self.identifier
    
  @property
  def is_staff(self):
    return self.is_superuser
    
  class Meta:
    verbose_name = '회원'
    verbose_name_plural = '회원'
