from django.db import models

# Create your models here.
class welcome_to_admin(models.Model):
    information = models.CharField(max_length=200)