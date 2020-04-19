from rest_framework import serializers
from shareProf.api.models.comment import CommentInfo
from shareProf.api.models.comment import CommentText


class CommentInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommentInfo
        fields = ['id', 'id_log_fk']


class CommentTextSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommentText
        fields = ['id', 'content']
