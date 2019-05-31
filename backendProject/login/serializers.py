from rest_framework import serializers
from . import models
from login.models import Category, ItemCategory, Persons, Persons_departaments, Persons_role, Persons_media, Persons_Contacts, Subject_matter, Pre_requirements, Site, Info_site, Content, Content_media

class CategorySerializer (serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = "__all__"  

class ItemCategorySerializer(serializers.ModelSerializer):
    
    category = serializers.PrimaryKeyRelatedField(queryset=models.Category.objects.all())

    class Meta:
        model = models.ItemCategory
        fields = "__all__"   

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Users
        fields = "__all__"

class PersonsSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Persons
        fields = "__all__"

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

class Subject_matter_Serializer (serializers.ModelSerializer):

    universitycareer = serializers.PrimaryKeyRelatedField(queryset=models.ItemCategory.objects.all())

    class Meta:
        model = models.Subject_matter
        fields = "__all__"

class Pre_requirements_Serializer (serializers.ModelSerializer):

    subject_matter_id_id = serializers.PrimaryKeyRelatedField(queryset=models.Subject_matter.objects.all())
    subject_matter_requeriment_id = serializers.PrimaryKeyRelatedField(queryset=models.Subject_matter.objects.all())

    class Meta:
        model = models.Pre_requirements
        fields = "__all__"

class Site_Serializer (serializers.ModelSerializer):
    class Meta:
        model = models.Site
        fields = "__all__"

class Info_site_Serializer (serializers.ModelSerializer):
    class Meta:
        model = models.Info_site
        fields = "__all__"

class Content_Serializer (serializers.ModelSerializer):
    '''
    content_universitycareer = serializers.PrimaryKeyRelatedField(queryset=models.ItemCategory.objects.all())
    type_event = serializers.PrimaryKeyRelatedField(queryset=models.ItemCategory.objects.all())
    academic_period = serializers.PrimaryKeyRelatedField(queryset=models.ItemCategory.objects.all())
    '''
    class Meta:
        model = models.Content
        fields = "__all__"

class Content_media_Serializer (serializers.ModelSerializer):

    item_category_item_category_id = serializers.PrimaryKeyRelatedField(queryset=models.ItemCategory.objects.all())

    class Meta: 
        model = models.Content_media
        fields = "__all__"