from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from User.models import User
from .models import Product, ProductPhoto, Wishlist
from .serializers import ProductSerializer, ProductPhotoSerializer, WishlistSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductPhotoViewSet(viewsets.ModelViewSet):
    queryset = ProductPhoto.objects.all()
    serializer_class = ProductPhotoSerializer


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def get_queryset(self):

        username = self.request.query_params.get("username")
        if username:
            try:
                user = User.objects.get(name=username)
                return Wishlist.objects.filter(user=user).prefetch_related('products')
            except User.DoesNotExist:
                return Wishlist.objects.none()
        return Wishlist.objects.all().prefetch_related('products')

    @action(detail=False, methods=["POST"], url_path="create")
    def create_wishlist(self, request):
        name = request.data.get("name")
        username = request.data.get("username")

        if not name or not username:
            return Response(
                {"error": "Both name and username are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(name=username)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if Wishlist.objects.filter(user=user, name=name).exists():
            return Response(
                {"error": "Wishlist with this name already exists for this user"},
                status=status.HTTP_400_BAD_REQUEST
            )

        wishlist = Wishlist.objects.create(user=user, name=name)
        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["POST"], url_path="add-product")
    def add_product(self, request, pk=None):

        product_id = request.data.get("product_id")
        wishlist_name = request.data.get("wishlist_name")
        username = request.data.get("username")

        if not product_id:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(name=username)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        wishlist, created = Wishlist.objects.get_or_create(user=user, name=wishlist_name)


        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        wishlist.products.add(product)
        return Response({"success": f"{product.name} added to {wishlist.name}"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"])
    def view_all(self, request):

        wishlists = self.get_queryset()
        serializer = WishlistSerializer(wishlists, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"], url_path="names")
    def get_wishlist_names(self, request):
    
        username = request.query_params.get("username")
        product_id = request.query_params.get("product_id")

        if not username:
            return Response({"error": "username is required"}, status=400)

        try:
            user = User.objects.get(name=username)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        wishlists = Wishlist.objects.filter(user=user)
        result = []

        for wl in wishlists:
            has_product = False
            if product_id:
                has_product = wl.products.filter(id=product_id).exists()
            result.append({"id": wl.id, "name": wl.name, "hasProduct": has_product})

        return Response(result)



            