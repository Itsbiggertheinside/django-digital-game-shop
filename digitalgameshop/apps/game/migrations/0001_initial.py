# Generated by Django 3.1.5 on 2021-01-18 09:32

from django.db import migrations, models
import django.db.models.deletion
import game.models.images


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('price', models.PositiveSmallIntegerField()),
                ('developer', models.CharField(max_length=55)),
                ('description', models.TextField()),
                ('release_date', models.DateField(blank=True, null=True)),
                ('requirements_minimum', models.TextField(blank=True, null=True)),
                ('requirements_recommended', models.TextField(blank=True, null=True)),
                ('on_sale', models.BooleanField(default=True)),
                ('pre_order', models.BooleanField(default=False)),
                ('stock', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Oyun',
                'verbose_name_plural': 'Oyunlar',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GameImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=game.models.images.upload_media)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='game.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(to='game.Genre'),
        ),
        migrations.AddField(
            model_name='game',
            name='languages',
            field=models.ManyToManyField(to='game.Language'),
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ManyToManyField(to='game.Platform'),
        ),
    ]
