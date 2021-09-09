from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

    template_name = "core/index.html"

class AboutPageView(TemplateView):

    template_name = "core/about.html"

class GalleryPageView(TemplateView):

    template_name = "core/gallery.html"

class ContactPageView(TemplateView):

    template_name = "core/contact.html"

