# Generated by Django 4.1.7 on 2023-04-23 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_alter_establishments_category_alter_hobbies_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appointment.users')),
                ('min_bill_value', models.PositiveIntegerField()),
            ],
            bases=('appointment.users',),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appointment.users')),
                ('max_spend_value', models.PositiveIntegerField()),
            ],
            bases=('appointment.users',),
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='user1',
        ),
        migrations.AddField(
            model_name='appointments',
            name='guest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appointment.guest'),
        ),
        migrations.AddField(
            model_name='appointments',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appointment.host'),
        ),
    ]
