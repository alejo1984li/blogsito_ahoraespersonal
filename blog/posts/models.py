from django.db import models
import uuid
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image_frontpage = models.ImageField(null=True, blank=True, default="")
    content = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=100, default='Anónimo')
    post_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.title