# Generated by Django 3.1.6 on 2021-02-17 12:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0002_post_catagory'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='poll_dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='poll_like', to=settings.AUTH_USER_MODEL),
        ),
    ]