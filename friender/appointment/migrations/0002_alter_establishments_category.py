# Generated by Django 4.1.7 on 2023-04-17 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishments',
            name='category',
            field=models.CharField(choices=[('c', 'cafe'), ('r', 'restaurant'), ('p', 'pub')], max_length=200),
        ),
    ]