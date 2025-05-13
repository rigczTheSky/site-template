from django.urls import path
from .views import news, domestic, world, about, post_detail, upload_image

urlpatterns = [
    path("", news, name="news"),
    path("domestic", domestic, name="domestic"),
    path("world", world, name="world"),
    path("about", about, name="about"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path('upload_image/', upload_image, name='upload_image'),
]
