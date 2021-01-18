from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


# Create your models here.
def upload_media(instance, filename):
    file_format = filename.split('.')[-1] # .jpg, .png
    file_name = f'{str(uuid4())}.{file_format}'
    return 'uploads/user_{0}/profile_pic/{1}'.format(instance.user.id, file_name)

class Account(AbstractUser):
    profile_pic = models.ImageField(upload_to=upload_media, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)


    def __str__(self):
        return self.username