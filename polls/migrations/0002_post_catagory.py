# Generated by Django 3.1.6 on 2021-02-17 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='catagory',
            field=models.CharField(choices=[('movies', 'movies'), ('sports', 'sports'), ('political', 'political'), ('general', 'general')], max_length=20, null=True),
        ),
    ]
