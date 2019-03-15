from rest_framework import serializers
from . import models
from login.models import Category, ItemCategory

class TodoSerializer(serializers.ModelSerializer):

    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Todo.objects.all())

    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Todo

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('idCategory', 'nameCategory', 'active ')        

class ItemCategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = models.ItemCategory
        fields = ('item_category_id', 'name_item', 'active', 'category_category_id')
