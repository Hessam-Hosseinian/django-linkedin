# Generated by Django 5.1 on 2024-08-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autuser', '0003_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='additional_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='background_picture',
            field=models.ImageField(blank=True, null=True, upload_to='background_pictures/'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='title',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, max_length=255, unique=True),
        ),
    ]
