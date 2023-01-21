from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    company = models.CharField(max_length=200)
    image = models.URLField()
    bio = models.CharField(max_length=500)
    pass

    def __str__(self):
            return self.username


    # username = models.CharField(max_length=200)
    # email = models.EmailField()
    # password = models.CharField(write_only=True)
    # company = models.CharField(max_length=200)
    # image = models.URLField()
    # bio = models.TextField()
    # id = models.PrimaryKey()

# class CustomUserSerializer(models.Model):
#     username = models.CharField(max_length=200)
#     email = models.EmailField()
#     password = models.CharField(write_only=True)
#     company = models.CharField(max_length=200)
#     image = models.URLField()
#     bio = models.TextField()
#     id = models.PrimaryKey()
