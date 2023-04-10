from django.db import models

SEX = [
    ("M", "Male"),
    ("F", "Female")
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



