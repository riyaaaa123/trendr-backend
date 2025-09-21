from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Video
from .serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Video.objects.all().order_by("-created_at")
    serializer_class = VideoSerializer

    def get_serializer_class(self):
        return VideoSerializer

    @action(detail=True, methods=["get"])
    def products(self, request, pk=None):
        """Custom endpoint: /api/videos/<id>/products/ → products in this video"""
        video = self.get_object()
        serializer = VideoSerializer(video)
        return Response(serializer.data["products"])

    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        """Custom endpoint: /api/videos/<id>/like/ → increment likes"""
        video = self.get_object()
        video.likes += 1
        video.save()
        return Response({"likes": video.likes})
