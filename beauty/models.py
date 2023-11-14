from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    fam = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    otc = models.CharField(max_length=40)
    phone = models.CharField(max_length=11)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Level(models.Model):
    winter = models.CharField(max_length=3, blank=True, null=True)
    summer = models.CharField(max_length=3, blank=True, null=True)
    autumn = models.CharField(max_length=3, blank=True, null=True)
    spring = models.CharField(max_length=3, blank=True, null=True)


class Images(models.Model):
    data = models.ImageField()
    title = models.CharField(max_length=100)


class Beauty(models.Model):
    CHOICES = (
        ('NE', 'new'),
        ('PE', 'pending'),
        ('AC', 'accepted'),
        ('RE', 'rejected'),
    )

    status = models.CharField(max_length=30, choices=CHOICES, default=CHOICES[0][1])

    beauty_title = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    other_titles = models.CharField(max_length=30)
    connect = models.CharField(max_length=30)
    add_time = models.DateTimeField(auto_now_add=True)

    coords = models.OneToOneField(Coords, on_delete=models.PROTECT)
    level = models.OneToOneField(Level, on_delete=models.PROTECT)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    images = models.ManyToManyField(Images)



