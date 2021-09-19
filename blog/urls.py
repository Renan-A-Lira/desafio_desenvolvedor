from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('image/detail/<int:id>', views.image_detail, name='image_detail'),
    path('image/create', views.image_post, name='image_post'),
    path('image/approve/<int:id>', views.approve_image, name='approve_image'),
    path('image/remove/<int:id>', views.remove_image, name='remove_image'),
    path('image/like', views.liked, name='liked_image'),
    path('image/getlike', views.userliked, name='user_liked'),
    path('accounts/register', views.register_request, name='register'),
    path('images/admin', views.image_list_admin, name='image_list_admin')
]