# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def galeria(request):
    posts = Post.objects.all()
    return render(request, "galeria/gallery.html", {'posts':posts})

def category(request, category_id):
    category = get_object_or_404(Post, id=category_id)
    print(category.image.url)
    return render(request, "galeria/single.html", {'category':category})

