from uuid import uuid4


class MediaDirectory():

    def upload_media(self, instance, filename):
        file_format = filename.split('.')[-1] # .jpg, .png
        file_name = f'{str(uuid4())}.{file_format}'
        return 'uploads/user_{0}/games/{1}'.format(instance.game.user.id, file_name)

    def upload_banner(self, instance, filename):
        file_format = filename.split('.')[-1] # .jpg, .png
        file_name = f'{str(uuid4())}.{file_format}'
        return 'uploads/user_{0}/games/{1}'.format(instance.user.id, file_name)