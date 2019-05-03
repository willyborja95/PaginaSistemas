from rest_framework import serializers
from . import models
from login.models import Category, ItemCategory, Persons, Persons_departaments, Persons_role, Persons_media, Persons_Contacts

class CategorySerializer (serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ('idCategory', 'nameCategory', 'active')        

class ItemCategorySerializer(serializers.ModelSerializer):

    category = serializers.CharField(source='category.nameCategory')

    class Meta():
        model = models.ItemCategory
        fields = ('idItemCategory', 'nameItemCategory', 'active', 'category')

    def create(self, data):
        print("llegoooooo!!!!!!!!!")
        print("llegoooooo!!!!!!!!!")
        print("llegoooooo!!!!!!!!!")
        print("llegoooooo!!!!!!!!!")
        print("llegoooooo!!!!!!!!!")
        print("llegoooooo!!!!!!!!!")
        print("llegoooooo!!!!!!!!!")
        print("llegoooooo!!!!!!!!!")
        print("llegoooooo!!!!!!!!!")
        category = models.Category.objects.get(idCategory = int(data.get('category')['nameCategory']))
        return models.ItemCategory.objects.create(nameItemCategory = data.get('nameItemCategory'), active = data.get('active'), category = category)

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

class Persons_depaSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Persons_departaments
        fields = "__all__"

class Persons_roleSerializer (serializers.ModelSerializer):
    class Meta: 
        model = models.Persons_role
        fields = "__all__"

class Persons_mediaSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Persons_media
        fields = "__all__"

class Persons_ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Persons_Contacts
        fields = "__all__"
