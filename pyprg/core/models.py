from django.db import models
from pyprg.resources.models import Resource
from pyprg.comments.models import Comment
from pyprg.evaluation.models import Evaluation
from pyprg.location.models import Location


class TurPoint(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    available = models.BooleanField(default=False)
    resources = models.ManyToManyField(Resource)
    comments = models.ManyToManyField(Comment)
    evaluation = models.ManyToManyField(Evaluation)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name, self.location, self.resources
