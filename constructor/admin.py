from django.contrib import admin
from . models import *

@admin.register(Constructor)
class ConstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'inn', 'ogrn', 'title', 'country', 'region', 'city', 'index', 'adress', 'category', 
                    'sub_category', 'heading', 'keywords', 'phone', 'cell_phone', 'metro', 'email', 'site',
                    'vk', 'twtr', 'fb', 'inst', 'x', 'y', 'additional', 'work_time')
    list_display_links = ('id', 'inn', 'title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )