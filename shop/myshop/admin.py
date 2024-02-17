from django.contrib import admin
from django.utils.safestring import mark_safe
import os
from .models import Category, Product, ContactUser, Store, Gallery


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image_show', 'price']
    list_filter = ['category']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name', )}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return ""

    def image_size(self, obj):
        if obj.image:
            size = os.path.getsize(obj.image.path)/1024
            return "{:.1f} KB".format(size)
        return "Unknown"

    image_show.__name__ = "Картинка"
    image_size.short_description = "Размер файла"


@admin.register(ContactUser)
class ContactUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone_number', 'phone_number_2', 'email']
    search_fields = ['name', 'address', 'phone_number', 'phone_number_2', 'email']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'description']
    search_fields = ['name', 'phone_number', 'description']


@admin.register(Gallery)
class PhotoGallery(admin.ModelAdmin):
    list_display = ['name', 'alt']
    search_fields = ['name', 'alt']
