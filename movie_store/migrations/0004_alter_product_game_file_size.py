# Generated by Django 4.0.5 on 2022-06-13 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_store', '0003_remove_product_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='game_file_size',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
