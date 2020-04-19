from django.db import models
from . import catalog


class Institution(models.Model):
    country = models.ForeignKey(catalog.Country, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    acronym = models.CharField(max_length=30)


class School(models.Model):
    name = models.CharField(max_length=50)
    institution = models.ForeignKey(Institution,
                                    on_delete=models.PROTECT)


class Department(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.PROTECT)


class Professor(models.Model):
    city = models.ForeignKey(catalog.City, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    last_name_1 = models.CharField(max_length=50)
    last_name_2 = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)


class Subject(models.Model):
    name = models.CharField(max_length=50)
