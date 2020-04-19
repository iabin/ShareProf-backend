from rest_framework import serializers
from shareProf.api.models.comment import CommentInfo
from shareProf.api.models.comment import CommentText
from shareProf.api.models.comment import Ratting


class CommentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentInfo
        fields = '__all__'
        depth = 1


class CommentTextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommentText
        fields = '__all__'


class CommentRattingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ratting
        fields = '__all__'


