# Generated by Django 5.1 on 2024-08-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0008_remove_user_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]