# Generated by Django 2.1.7 on 2019-04-19 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]