from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_user = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_lenth=300)
    image = models.ImageField(upload_to='media')

    def __str__(self) -> str:
        return f'{self.user.username} profile'