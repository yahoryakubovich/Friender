# Generated by Django 4.1.7 on 2023-05-20 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0016_alter_order_date_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='photo',
            field=models.ImageField(null=True, upload_to='profile_photo'),
        ),
    ]
