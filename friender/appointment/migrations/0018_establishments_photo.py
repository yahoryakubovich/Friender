# Generated by Django 4.1.7 on 2023-05-21 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0017_users_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='establishments',
            name='photo',
            field=models.ImageField(null=True, upload_to='establishment_photo'),
        ),
    ]
