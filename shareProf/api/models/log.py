from django.db import models


class Ip(models.Model):
    ip_address_pk = models.CharField(max_length=15, primary_key=True)
    country_fk = models.IntegerField()
    isp = models.CharField(max_length=50)


class Log(models.Model):
    ip = models.ForeignKey(Ip, on_delete=models.PROTECT)
    operating_system = models.CharField(max_length=50)
    browser = models.CharField(max_length=50)
    device = models.CharField(max_length=50)
    date = models.DateField(auto_now=True, null=False)
    time = models.TimeField(auto_now=True, null=False)
