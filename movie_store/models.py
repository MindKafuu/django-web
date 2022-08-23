from pyexpat import model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='product')
    title = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    number_of_players = models.IntegerField()
    publisher = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    supported_play_modes = models.TextField()
    game_file_size = models.DecimalField(max_digits=4, decimal_places=2)
    supported_languages = models.TextField()
    slug = models.SlugField(max_length=255)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.title
