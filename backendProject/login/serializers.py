from rest_framework import serializers
from . import models
from login.models import Category, ItemCategory

class CategorySerializer (serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ('idCategory', 'nameCategory', 'active')        

class ItemCategorySerializer(serializers.ModelSerializer):

    class Meta():
        model = models.ItemCategory
        fields = ('idItemCategory', 'nameItemCategory', 'active', 'category')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Users

        fields = (
            'username',
            'create_time',
            'update_time'
        )

class PersonsSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Persons
        fields = ('first_name','second_name', 'first_last_name', 'second_last_name')