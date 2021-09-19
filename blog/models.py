from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.

def upload_image(image, filename):
    return f'{image.author.username}-{filename}'

class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=100, unique=True)
    legenda = models.TextField(max_length=145, blank=True, null=True)
    image_file = models.ImageField(upload_to=upload_image)
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='post_like')

    def approve(self):
        self.approved = True
        self.published_date = timezone.now()
        self.save()


    def __str__(self) :
        return str(self.id)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ForeignKey(Image, on_delete=CASCADE, related_name='comments')
    text = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    