# Generated by Django 4.2.10 on 2024-03-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_restaurant_image_alter_restaurant_restaurant_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(default=0, max_length=200, unique=True),
        ),
    ]
