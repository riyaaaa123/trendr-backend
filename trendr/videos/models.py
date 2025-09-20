from django.db import models
from User.models import User
from product.models import Product


class Video(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="videos")
    video_url = models.URLField()   
    caption = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name="videos") 
    likes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"Video by {self.uploader.name} ({self.id})"
