# Generated by Django 3.2.9 on 2021-11-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to='user_image/'),
        ),
    ]
