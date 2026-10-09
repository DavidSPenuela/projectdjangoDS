from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    #category = serializers.StringRelatedField()
    category = serializers.SlugRelatedField(
        slug_field='name', 
        queryset=Category.objects.all()
    )
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category')
        #fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'