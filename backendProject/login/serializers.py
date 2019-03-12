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

class Category (serializers.ModelSerializer):
    class meta:
        model = models.Category
        fields = ('idCategory', 'nameCategory', 'active ')        

class ItemCategory (serializers.ModelSerializer):
    class meta:
        model = models.ItemCategory
        fields = ('item_category_id', 'name_item', 'active', 'category_category_id')
