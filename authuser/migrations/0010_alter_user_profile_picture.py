# Generated by Django 5.1 on 2024-08-18 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0009_user_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='../static/icons/Default_Profile_Picture.png', null=True, upload_to='profile_pictures/'),
        ),
    ]
