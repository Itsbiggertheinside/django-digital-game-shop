# Generated by Django 3.1.5 on 2021-01-23 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameratings',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='game_total_comments', to='game.Comment'),
        ),
    ]