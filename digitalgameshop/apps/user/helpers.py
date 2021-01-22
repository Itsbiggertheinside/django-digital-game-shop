from uuid import uuid4

def upload_media(instance, filename):
    file_format = filename.split('.')[-1] # .jpg, .png
    file_name = f'{str(uuid4())}.{file_format}'
    return 'uploads/user_{0}/profile_pic/{1}'.format(instance.id, file_name)