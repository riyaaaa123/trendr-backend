from rest_framework import serializers
from .models import Video
from product.serializers import ProductSerializer


class VideoSerializer(serializers.ModelSerializer):
    # Show product IDs in POST/PUT, and full product details in GET
    products = serializers.PrimaryKeyRelatedField(queryset=ProductSerializer.Meta.model.objects.all(), many=True)

    class Meta:
        model = Video
        fields = ["id", "uploader", "video_url", "caption", "likes", "created_at", "products"]


class VideoDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ["id", "uploader", "video_url", "caption", "likes", "created_at", "products"]
