from django.db import models
from datetime import datetime

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
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX)
    email = models.EmailField(null=True, unique=True)
    city = models.CharField(max_length=100, default="Minsk")

    def __str__(self):
        return self.name


class UserRating(models.Model):
    rating = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey("Users", on_delete=models.CASCADE)

    def __str__(self):
        return self.rating


class Passport(models.Model):
    passport_id = models.CharField(max_length=40, unique=True)
    date_create = models.DateTimeField(auto_created=datetime)
    user = models.OneToOneField("Users", on_delete=models.CASCADE)

    def __str__(self):
        return self.passport_id


class Establishments(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY)

    def __str__(self):
        return self.name


class EstablishmentsRating(models.Model):
    rating = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    establishment = models.ForeignKey("Establishments", on_delete=models.CASCADE)

    def __str__(self):
        return self.rating


class Hobbies(models.Model):
    name_hobby = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=HOBBIES)
    user = models.ManyToManyField("Users")

    def __str__(self):
        return self.name_hobby


class Appointments(models.Model):
    user1 = models.ForeignKey("Users", on_delete=models.CASCADE)
    establishments = models.ForeignKey("Establishments", on_delete=models.CASCADE)
