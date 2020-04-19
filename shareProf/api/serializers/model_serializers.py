from rest_framework import serializers
from shareProf.api.models.log import Log
from shareProf.api.models.log import Ip


class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'


class IpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ip
        fields = '__all__'

