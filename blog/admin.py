from django.contrib import admin
from .models import Comment, Image
# Register your models here.

admin.site.register(Image)
admin.site.register(Comment)