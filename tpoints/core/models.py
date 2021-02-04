from django.db import models
# from resources.models import Resource
# from comments.models import Comment
# from evaluation.models import Evalution
# from location.models import Location


class TurPoint(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    available = models.BooleanField(default=False)
    # resources = models.ManyToManyField(Resource)
    # comments = models.ManyToManyField(Comment)
    # evaluation = models.ManyToManyField(Evalution)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
