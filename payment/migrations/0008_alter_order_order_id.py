# Generated by Django 3.2.4 on 2023-07-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_auto_20230716_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
