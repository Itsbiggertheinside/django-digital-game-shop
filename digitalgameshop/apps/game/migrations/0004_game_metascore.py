# Generated by Django 3.1.5 on 2021-01-23 22:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20210124_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='metascore',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
            preserve_default=False,
        ),
    ]