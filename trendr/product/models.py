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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")
