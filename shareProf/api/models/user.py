from django.db import models
from django.contrib.auth.models import User
from shareProf.api.models import catalog


class UserInfo(models.Model):
    id = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    last_name_1 = models.CharField(max_length=50)
    last_name_2 = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    country = models.ForeignKey(catalog.CatCountry,
                                on_delete=models.PROTECT)
    birth_date = models.DateField()
    verified = models.BooleanField(default=False)


