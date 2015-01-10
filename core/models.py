from django.db import models

# Create your models here.
class Section(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    position = models.IntegerField()

    def __str__(self):
        return self.title