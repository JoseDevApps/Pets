from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404
from galeria import models

def HomePageView(request):
    posts = models.Post.objects.all()
    return render(request, "core/index.html", {'posts':posts})

# class HomePageView(TemplateView):

#     template_name = "core/index.html"

class AboutPageView(TemplateView):

    template_name = "core/about.html"

class GalleryPageView(TemplateView):

    template_name = "core/gallery.html"

class ContactPageView(TemplateView):

    template_name = "core/contact.html"

