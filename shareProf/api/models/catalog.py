from django.db import models


class SubjectExperience(models.Model):
    description = models.CharField(max_length=50, blank=False, null=False)
    value = models.IntegerField()


class SubjectDifficulty(models.Model):
    description = models.CharField(max_length=50, blank=False, null=False)
    value = models.IntegerField()


class Country(models.Model):
    name = models.CharField(max_length=50)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)






