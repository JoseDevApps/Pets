from django.urls import path
from .views import HomePageView, AboutPageView, GalleryPageView, ContactPageView
app_name = 'core'
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('galeria/', GalleryPageView.as_view(), name='gallery'),
    path('contacto/', ContactPageView.as_view(), name='contact'),
]