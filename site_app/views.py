import os
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'main/index.html')

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "site_app/index.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, "site_app/detail.html", context)

@csrf_exempt  # TinyMCE nie przesyła CSRF tokena, więc wyłączamy na ten widok
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('file'):
        image = request.FILES['file']
        image_name = image.name
        save_path = os.path.join(settings.MEDIA_ROOT, image_name)

        # Zapis pliku
        with open(save_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

        image_url = settings.MEDIA_URL + image_name
        return JsonResponse({'location': image_url})

    return JsonResponse({'error': 'Invalid request'}, status=400)
