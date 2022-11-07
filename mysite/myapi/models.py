from django.db import models


class Champions(models.Model):
    name = models.CharField(max_length=100)
    div = models.CharField(max_length=45)

    def __str__(self):
        return self.name
