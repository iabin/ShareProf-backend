from django.db import models


class CatSubjectExperience(models.Model):
    description = models.CharField(max_length=50, blank=False, null=False)
    value = models.IntegerField()


class CatSubjectDifficulty(models.Model):
    description = models.CharField(max_length=50, blank=False, null=False)
    value = models.IntegerField()


class CatCountry(models.Model):
    name = models.CharField(max_length=50)


class CatCities(models.Model):
    country = models.ForeignKey(CatCountry,on_delete=models.PROTECT)
    name = models.CharField(max_length=50)






