from django.db import models

class Department(models.Model):
  slug = models.CharField(max_length=40)
  name = models.CharField(max_length=40)

  class Meta:
    verbose_name = '계열'
    verbose_name_plural = '계열'