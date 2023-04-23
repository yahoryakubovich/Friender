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


class Host(Users):
    max_spend_value = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    indexes = [
        models.Index(fields=["name"]),
        models.Index(fields=["max_spend_value"]),
        models.Index(fields=["age"]),
        models.Index(fields=["name_hobby"])
    ]


class Guest(Users):
    min_bill_value = models.PositiveIntegerField()

    indexes = [
        models.Index(fields=["name"]),
        models.Index(fields=["min_bill_value"]),
        models.Index(fields=["age]"]),
        models.Index(fields=["name_hobby"])
    ]

    def __str__(self):
        return self.name


class Passport(models.Model):
    passport_id = models.CharField(max_length=40, unique=True)
    date_create = models.DateTimeField(auto_created=datetime)
    user = models.OneToOneField("Users", on_delete=models.CASCADE)

    def __str__(self):
        return self.passport_id


class Establishments(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=1, choices=CATEGORY)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)

    indexes = [
        models.Index(fields=["category"]),
        models.Index(fields=["address"]),
    ]

    def __str__(self):
        return self.name


class Hobbies(models.Model):
    name_hobby = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=HOBBIES)
    user = models.ManyToManyField("Users")

    def __str__(self):
        return self.name_hobby


class Appointments(models.Model):
    host = models.ForeignKey("Host", on_delete=models.CASCADE, null=True)
    guest = models.ForeignKey("Guest", on_delete=models.CASCADE, null=True)
    establishments = models.ForeignKey("Establishments", on_delete=models.CASCADE)


class Rating(models.Model):
    rating = models.PositiveIntegerField()
    description = models.CharField(max_length=255)

    class Meta:
        abstract = True


class UserRating(Rating):
    user = models.ForeignKey("Users", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class EstablishmentsRating(Rating):
    establishment = models.ForeignKey("Establishments", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.establishment)
