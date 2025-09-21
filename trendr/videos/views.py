from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Video
from .serializers import VideoSerializer
from User.models import User


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
    
    @action(detail=False, methods=["post"])
    def create_reel(self, request):
        """
        Endpoint: /api/videos/create_reel/
        Payload: { "username": "riya", "video_url": "...", "caption": "...", "products": [1,2,3] }
        """
        data = request.data
        print("Incoming data:", data)
        username = data.get("username")
        video_url = data.get("video_url")

        if not username or not video_url:
            return Response(
                {"error": "username and video_url are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(name=username)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            video = Video.objects.create(
                uploader=user,
                video_url=video_url,
                caption=data.get("caption", "")
            )
            
            if "products" in data:
                video.products.set(data["products"])

            return Response(VideoSerializer(video).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
