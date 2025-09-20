from rest_framework import serializers
from .models import Video
from product.serializers import ProductSerializer

class VideoSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    uploader_name = serializers.CharField(source="uploader.name", read_only=True)

    class Meta:
        model = Video
        fields = ["id", "uploader", "video_url", "caption", "likes", "created_at", "products","uploader_name"]
