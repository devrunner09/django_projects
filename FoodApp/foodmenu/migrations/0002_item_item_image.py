# Generated by Django 4.2.2 on 2023-06-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodmenu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://static.vecteezy.com/system/resources/previews/003/170/825/original/isolated-food-plate-fork-and-spoon-design-free-vector.jpg', max_length=500),
        ),
    ]