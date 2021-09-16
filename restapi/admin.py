from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class adminCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class adminProduct(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}