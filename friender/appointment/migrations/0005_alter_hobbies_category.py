# Generated by Django 4.1.7 on 2023-04-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_alter_hobbies_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbies',
            name='category',
            field=models.CharField(choices=[('sport', 'sport'), ('traveling', 'traveling'), ('painting', 'painting')], max_length=100),
        ),
    ]