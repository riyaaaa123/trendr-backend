from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    is_influencer = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
