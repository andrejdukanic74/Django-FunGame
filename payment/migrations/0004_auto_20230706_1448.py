# Generated by Django 3.2.4 on 2023-07-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20230706_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]