from django.db import models

class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.name
