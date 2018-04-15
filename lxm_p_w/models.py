from django.db import models

# Create your models here.
class User(models.Model):
    UserId=models.IntegerField(primary_key=False)
    UserName = models.CharField(max_length=255)
    PassWord = models.CharField(max_length=255)
    # Date = models.DateField(auto_now=True)
