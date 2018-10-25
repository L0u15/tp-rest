from django.contrib.auth.models import User, Group
from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ('url', 'id', 'description', 'deadline','done','priority','tags', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.HyperlinkedRelatedField(many=True, view_name='todo-detail',read_only=True,allow_null=True)

    class Meta:
        model = User
        fields = ('url','username','todos')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')