from shareProf.api import models
from shareProf.api.serializers import model_serializers
from rest_framework import viewsets
from rest_framework import permissions


class LogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Log.objects.all()
    serializer_class = model_serializers.LogSerializer
    permission_classes = [permissions.IsAuthenticated]


class IpViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Ip.objects.all()
    serializer_class = model_serializers.IpSerializer
    permission_classes = [permissions.IsAuthenticated]


class CountryViewSet(viewsets.ModelViewSet):
    queryset = models.Country.objects.all().order_by('name')
    serializer_class = model_serializers.CountrySerializer
    http_method_names = ['get']
