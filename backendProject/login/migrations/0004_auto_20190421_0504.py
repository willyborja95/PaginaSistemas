# Generated by Django 2.1.7 on 2019-04-21 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20190421_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Category'),
        ),
    ]