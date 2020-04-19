from rest_framework import viewsets
from rest_framework import permissions
from shareProf.api.models.comment import CommentInfo
from shareProf.api.models.comment import CommentText
from shareProf.api.models.comment import Ratting
from shareProf.api.serializers.comment_serializers import CommentTextSerializer
from shareProf.api.serializers.comment_serializers import CommentRattingSerializer
from shareProf.api.serializers.comment_serializers import CommentInfoSerializer


class CommentInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CommentInfo.objects.all()
    serializer_class = CommentInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentTextViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CommentText.objects.all()
    serializer_class = CommentTextSerializer
    permission_classes = [permissions.IsAuthenticated]


class RattingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ratting.objects.all()
    serializer_class = CommentRattingSerializer
    permission_classes = [permissions.IsAuthenticated]