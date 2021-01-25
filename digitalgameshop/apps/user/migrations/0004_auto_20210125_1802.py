# Generated by Django 3.1.5 on 2021-01-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_account_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.AlterField(
            model_name='account',
            name='slug',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
    ]
