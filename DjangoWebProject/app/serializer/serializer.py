from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import Relevance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class RelevanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relevance
        fields = ('item1','item2')