from django.db import models

# Create your models here.
tipe_incident = [
    ("IN", "Incident"),
    ("RQ", "Request"),
]

level_choices = [
    ("Low", "Bajo"),
    ("Mid", "Medio"),
    ("Hi", "Alta"),
    ("VHi", "Critico"),
]


class Incident(models.Model):
    tipe = models.CharField(max_length=2, choices=tipe_incident)
    level = models.CharField(max_length=3, choices=level_choices)
    url = models.URLField()
    project = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.tipe} --> {self.level}"


class Attach(models.Model):
    comment = models.CharField(max_length=254)
    image = models.ImageField(upload_to='imagen')

    def __str__(self):
        return self.comment, self.image


class UserContact(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.EmailField()
    cel_phone = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
