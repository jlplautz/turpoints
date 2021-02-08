from django.db import models


class Resource(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    work_time = models.TextField()
    age_min = models.IntegerField()

    def __str__(self):
        return self.name
