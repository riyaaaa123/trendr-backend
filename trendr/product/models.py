import uuid
from datetime import timedelta
from django.utils import timezone
from django.db import models
from User.models import User


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)

    def __str__(self):
        return self.name


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="photos")
    photo_url = models.URLField()

    def __str__(self):
        return f"{self.product.name} photo"


class Wishlist(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlists")
    products = models.ManyToManyField(Product, blank=True, related_name="wishlists")
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "name")

    def __str__(self):
        return f"{self.name} - {self.user.name}"

def default_expiry():
    return timezone.now() + timedelta(days=2)

class WishlistShare(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name="shares")
    shared_by = models.ForeignKey(User, on_delete=models.CASCADE)
    share_code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=default_expiry)  # <- use function here

    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"{self.wishlist.name} shared by {self.shared_by.name}"