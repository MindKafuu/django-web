from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title', 
        'release_date', 
        'number_of_players', 
        'publisher',
        'description',
        'supported_play_modes',
        'game_file_size',
        'supported_languages',
        'slug',
        'price',
        'in_stock',
        'created',
        'updated'
    ]
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}
