from django.db import models
from datetime import datetime
from django.core.validators import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms

SEX = [
    ("M", "Male"),
    ("F", "Female")
]

CATEGORY = [
    ("C", "Cafe"),
    ("R", "Restaurant"),
    ("P", "Pub")
]

HOBBIES = [
    ("S", "Sport"),
    ("T", "Traveling"),
    ("P", "Painting")
]


class Users(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    age = models.IntegerField(verbose_name="Возраст", validators=[
        MaxValueValidator(90, message='Is too old'),
        MinValueValidator(18, message='Is too young')
    ])
    sex = models.CharField(max_length=1, choices=SEX, verbose_name="Пол")
    email = models.EmailField(null=True, unique=True, verbose_name="Email")
    city = models.CharField(max_length=100, default="Minsk", verbose_name="Город")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.name


class Passport(models.Model):
    passport_id = models.CharField(max_length=40, unique=True, verbose_name="Уникальный номер")
    date_create = models.DateTimeField(auto_created=datetime, verbose_name="Дата создания")
    user = models.OneToOneField("Users", on_delete=models.CASCADE, verbose_name="Пользователь")

    class Meta:
        verbose_name = "Паспорт пользователя"
        verbose_name_plural = "Паспорта пользователей"

    def __str__(self):
        return self.passport_id


class Host(Users):
    max_spend_value = models.PositiveIntegerField(verbose_name="Предложение")

    class Meta:
        verbose_name = "Приглашающий"
        verbose_name_plural = "Приглашающие"

    def __str__(self):
        return self.name

    indexes = [
        models.Index(fields=["name"]),
        models.Index(fields=["max_spend_value"]),
        models.Index(fields=["age"]),
        models.Index(fields=["name_hobby"])
    ]


class Guest(Users):
    min_bill_value = models.PositiveIntegerField(verbose_name="Спрос")

    class Meta:
        verbose_name = "Гость"
        verbose_name_plural = "Гости"

    indexes = [
        models.Index(fields=["name"]),
        models.Index(fields=["min_bill_value"]),
        models.Index(fields=["age]"]),
        models.Index(fields=["name_hobby"])
    ]

    def __str__(self):
        return self.name


class Establishments(models.Model):
    name = models.CharField(max_length=200, verbose_name="Предложение")
    category = models.CharField(max_length=1, choices=CATEGORY, verbose_name="Категория")
    address = models.CharField(max_length=100, null=True, verbose_name="Адрес")
    phone = models.CharField(max_length=100, null=True, verbose_name="Номер")

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    indexes = [
        models.Index(fields=["category"]),
        models.Index(fields=["address"]),
    ]

    def __str__(self):
        return self.name


class Hobbies(models.Model):
    name_hobby = models.CharField(max_length=100, verbose_name="Название хобби")
    category = models.CharField(max_length=100, choices=HOBBIES, verbose_name="Категория")
    user = models.ManyToManyField("Users", verbose_name="Пользователь")

    class Meta:
        verbose_name = "Хобби"
        verbose_name_plural = "Хобби"

    def __str__(self):
        return str(self.name_hobby)


class Appointments(models.Model):
    host = models.ForeignKey("Host", on_delete=models.CASCADE, null=True, verbose_name="Приглашающий")
    guest = models.ForeignKey("Guest", on_delete=models.CASCADE, null=True, verbose_name="Приглашённый")
    establishments = models.ForeignKey("Establishments", on_delete=models.CASCADE, verbose_name="Место")

    class Meta:
        verbose_name = "Свидание"
        verbose_name_plural = "Свидания"

    def __str__(self):
        return f"Cвидание между {self.host} и {self.guest}"


class Rating(models.Model):
    rating = models.PositiveIntegerField(verbose_name="Рейтинг", validators=[
        MaxValueValidator(5, message='Is too much'),
        MinValueValidator(1, message='Is too little')
    ])
    description = models.CharField(max_length=100, verbose_name="Описание")

    class Meta:
        abstract = True


class UserRating(Rating):
    user = models.ForeignKey("Users", on_delete=models.CASCADE, verbose_name="Пользователь")

    class Meta:
        verbose_name = "Рейтинг пользователя"
        verbose_name_plural = "Рейтинг пользователей"

    def __str__(self):
        return str(self.user)


class EstablishmentsRating(Rating):
    establishment = models.ForeignKey("Establishments", on_delete=models.CASCADE, verbose_name="Место")

    class Meta:
        verbose_name = "Рейтинг места"
        verbose_name_plural = "Рейтинг мест"

    def __str__(self):
        return str(self.establishment)
