from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'category', 'title', 'description', 'price', 'in_stock', 'description', 'get_image', 'get_absolute_url'
        ]
        # OPTIMIZE CODE ABOVE

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'category'
        ]
        # OPTIMIZE CODE ABOVE