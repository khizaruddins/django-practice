from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 128)
    email = models.EmailField(max_length = 128)
    text = models.CharField(max_length = 264)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.ForeignKey(User, on_delete = models.CASCADE)
    designation = models.CharField(max_length = 256)
    pay = models.SmallIntegerField()
