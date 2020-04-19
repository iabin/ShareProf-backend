from rest_framework import serializers
from shareProf.api.models.log import Log
from shareProf.api.models.log import Ip


class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = ['id', 'operating_system', 'browser', 'device', 'date', 'time', 'ip']


class IpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ip
        fields = ['ip_address_pk', 'country_fk', 'isp']
