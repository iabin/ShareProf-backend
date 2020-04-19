from django.db import models


class CatClassExperience(models.Model):
    description = models.CharField(max_length=50, blank=False, null=False)
    value = models.IntegerField()


class CatClassDifficulty(models.Model):
    description = models.CharField(max_length=50, blank=False, null=False)
    value = models.IntegerField()
