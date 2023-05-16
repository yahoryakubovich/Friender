# Generated by Django 4.1.7 on 2023-05-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0011_alter_appointments_options_host_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='status',
            field=models.CharField(choices=[('A', 'Available'), ('B', 'Busy')], default='A', max_length=1),
        ),
    ]
