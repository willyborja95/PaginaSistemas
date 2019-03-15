from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Users

        fields = (
            'username',
            'email',
            'name',
            'lastname',
            'create_time',
            'update_time'
        )

class Category (serializers.ModelSerializer):
    class meta:
        model = models.Category
        fields = ('idCategory', 'nameCategory', 'active ')        

class ItemCategory (serializers.ModelSerializer):
    class meta:
        model = models.ItemCategory
        fields = ('item_category_id', 'name_item', 'active', 'category_category_id')
