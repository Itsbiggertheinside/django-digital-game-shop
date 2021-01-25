from django.db.models import TextChoices
from django.utils.text import gettext_lazy as _
from uuid import uuid4


def upload_media(instance, filename):
        file_format = filename.split('.')[-1] # .jpg, .png
        file_name = f'{str(uuid4())}.{file_format}'
        return 'uploads/user_{0}/games/{1}'.format(instance.game.user.slug, file_name)

def upload_banner(instance, filename):
        file_format = filename.split('.')[-1] # .jpg, .png
        file_name = f'{str(uuid4())}.{file_format}'
        return 'uploads/user_{0}/games/{1}'.format(instance.user.slug, file_name)
