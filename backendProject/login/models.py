from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title

class Category (models.Model):
    idCategory = models.IntegerField(primary_key=True)
    nameCategory = models.CharField(max_length= 255)
    active = models.PositiveSmallIntegerField()	

    def __str__(self):
        return self.nameCategory

class ItemCategory (models.Model):
    item_category_id = models.IntegerField(primary_key=True) 
    name_item = models.CharField(max_length= 255)
    active = models.PositiveSmallIntegerField()	
    category_category_id = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.name_item