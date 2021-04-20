import datetime
from django.db import models
from django.utils import timezone


class Story(models.Model):

    heading = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    storyTxt = models.CharField(max_length=200)

    def __str__(self):
        return self.heading

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
