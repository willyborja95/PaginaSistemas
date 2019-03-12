from rest_framework import serializers
from . import models

class TodoSerializer(serializers.ModelSerializer):

    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Todo.objects.all())

    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Todo