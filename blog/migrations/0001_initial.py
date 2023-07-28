# Generated by Django 3.2 on 2021-09-01 04:41

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('thumbnail', models.ImageField(default='placeholder.jpg', upload_to='thumbnails')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('featured', models.BooleanField(default=False, verbose_name='Featured')),
                ('meta_tags', models.CharField(blank=True, help_text='comma seperated tags used for SEO ', max_length=255, null=True)),
                ('meta_description', models.CharField(blank=True, help_text='meta description used for SEO (max 170 characters)', max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('tags', models.ManyToManyField(blank=True, to='blog.Tag')),
            ],
        ),
    ]