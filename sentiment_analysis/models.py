from django.db import models


# Create your models here.

class Sentence(models.Model):
    sentence = models.TextField()
    positive = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)
    neutral = models.IntegerField(default=0)
    overall = models.CharField(max_length=20)

    def __str__(self):
        return "{} : {}".format(self.sentence, self.overall)
