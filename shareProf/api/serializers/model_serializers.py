from rest_framework import serializers
from shareProf.api import models


class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Log
        fields = '__all__'


class IpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Ip
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = '__all__'
