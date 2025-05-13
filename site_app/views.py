import os
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'main/index.html')

def news(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "site_app/index.html", context)

def domestic(request):
    posts = Post.objects.filter(category__name='Domestic').order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "site_app/index.html", context)

def world(request):
    posts = Post.objects.filter(category__name='World').order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "site_app/index.html", context)

def about(request):
    post = Post.objects.filter(category__name='About').order_by('-created_on').first()
    context = {
        "post": post,
    }
    return render(request, "site_app/about.html", context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, "site_app/detail.html", context)

@csrf_exempt 
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('file'):
        image = request.FILES['file']
        image_name = image.name
        save_path = os.path.join(settings.MEDIA_ROOT, image_name)

        with open(save_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

        image_url = settings.MEDIA_URL + image_name
        return JsonResponse({'location': image_url})

    return JsonResponse({'error': 'Invalid request'}, status=400)
