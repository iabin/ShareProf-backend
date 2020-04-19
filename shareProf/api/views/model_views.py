from shareProf.api.models.log import Log
from shareProf.api.models.log import Ip
from shareProf.api.serializers import model_serializers
from rest_framework import viewsets
from rest_framework import permissions


class LogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Log.objects.all()
    serializer_class = model_serializers.LogSerializer
    permission_classes = [permissions.IsAuthenticated]


class IpViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ip.objects.all()
    serializer_class = model_serializers.IpSerializer
    permission_classes = [permissions.IsAuthenticated]