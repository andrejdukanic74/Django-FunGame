# Generated by Django 3.2 on 2023-05-30 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowtbc', '0005_game_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='min_sale',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
