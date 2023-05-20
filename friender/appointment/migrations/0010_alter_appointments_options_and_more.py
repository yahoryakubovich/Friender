# Generated by Django 4.1.7 on 2023-04-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0009_establishments_address_establishments_phone_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointments',
            options={'verbose_name': 'Встреча', 'verbose_name_plural': 'Встречи'},
        ),
        migrations.AlterModelOptions(
            name='establishments',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterModelOptions(
            name='establishmentsrating',
            options={'verbose_name': 'Рейтинг места', 'verbose_name_plural': 'Рейтинг мест'},
        ),
        migrations.AlterModelOptions(
            name='guest',
            options={'verbose_name': 'Гость', 'verbose_name_plural': 'Гости'},
        ),
        migrations.AlterModelOptions(
            name='hobbies',
            options={'verbose_name': 'Хобби', 'verbose_name_plural': 'Хобби'},
        ),
        migrations.AlterModelOptions(
            name='host',
            options={'verbose_name': 'Приглашающий', 'verbose_name_plural': 'Приглашающие'},
        ),
        migrations.AlterModelOptions(
            name='passport',
            options={'verbose_name': 'Паспорт пользователя', 'verbose_name_plural': 'Паспорта пользователей'},
        ),
        migrations.AlterModelOptions(
            name='userrating',
            options={'verbose_name': 'Рейтинг пользователя', 'verbose_name_plural': 'Рейтинг пользователей'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='users',
            name='city',
            field=models.CharField(default='Minsk', max_length=100, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='users',
            name='surname',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
    ]