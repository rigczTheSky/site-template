from django.urls import path
from .views import blog_index, blog_detail, upload_image

urlpatterns = [
    path("", blog_index, name="blog_index"),
    path("post/<int:pk>/", blog_detail, name="blog_detail"),
    path('upload_image/', upload_image, name='upload_image'),
]
