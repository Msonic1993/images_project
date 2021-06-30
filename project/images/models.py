from django.contrib.auth.models import User
from django.db import models




class Plans (models.Model):
    def __str__ (self):
        return self.name

    name = models.CharField (max_length = 148)
    users = models.ManyToManyField (User)

    class Meta:
        ordering = [ 'name' ]


class Sizes (models.Model):
    def __str__ (self):
        return self.name

    name = models.CharField(max_length = 148)
    size = models.IntegerField()
    plan = models.ManyToManyField(Plans)

    class Meta:
        ordering = [ 'size' ]


class Storage (models.Model):
    def __str__ (self):
        return self.fileName

    fileName = models.CharField (max_length = 148)
    path = models.CharField (max_length = 300)
    file = models.FileField(upload_to='media/', null=True, blank=True)
    owner = models.ForeignKey (User, on_delete = models.CASCADE)
