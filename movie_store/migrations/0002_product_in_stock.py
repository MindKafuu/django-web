# Generated by Django 4.0.5 on 2022-06-13 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
    ]
