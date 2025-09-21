from rest_framework import serializers
from .models import Product, ProductPhoto, Wishlist


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ["id", "photo_url"]

class ProductSerializer(serializers.ModelSerializer):
    photos = ProductPhotoSerializer(many=True)

    class Meta:
        model = Product
        fields = ["id", "name", "description", "rating", "photos", "price"]
        
    def create(self, validated_data):
        photos_data = validated_data.pop("photos", [])
        product = Product.objects.create(**validated_data)
        for photo in photos_data:
            ProductPhoto.objects.create(product=product, **photo)
        return product

    def update(self, instance, validated_data):
        photos_data = validated_data.pop("photos", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if photos_data is not None:
            instance.photos.all().delete() 
            for photo in photos_data:
                ProductPhoto.objects.create(product=instance, **photo)

        return instance

class WishlistSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,read_only=True)

    class Meta:
        model = Wishlist
        fields = ["id","name", "user", "products", "added_at"]
