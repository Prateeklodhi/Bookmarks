# Generated by Django 4.0.2 on 2022-11-18 11:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0002_rename_user_like_image_users_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='images_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
