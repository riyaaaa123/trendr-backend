from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductPhotoViewSet, WishlistViewSet

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("photos", ProductPhotoViewSet)
router.register("wishlist", WishlistViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
