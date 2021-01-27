from uuid import uuid4

# ---------------------------------------------------------------------

STATUS_CHOICE = (
    ('ON_SALE', 'Satışta'),
    ('PRE_ORDER', 'Ön Sipariş'),
    ('SECOND_HAND', 'İkinci El'),
    ('SOLD', 'Satıldı'),
)

# ---------------------------------------------------------------------

def upload_media(instance, filename):
    file_format = filename.split('.')[-1] # .jpg, .png
    file_name = f'{str(uuid4())}.{file_format}'
    return 'uploads/games/{0}/{1}'.format(instance.name, file_name)

# ---------------------------------------------------------------------