from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'title',
            'description',
            'price',
            'in_stock',
            'description',
            'get_image',
            'get_absolute_url',
            'get_thumbnail'
        ]
        # OPTIMIZE CODE ABOVE

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'get_absolute_url', 'products'
        ]
        # OPTIMIZE CODE ABOVE