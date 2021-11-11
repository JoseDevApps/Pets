from django.urls import path
from . import views
from .views import HomePageView, AboutPageView, GalleryPageView, ContactPageView
app_name = 'core'
urlpatterns = [
    path('', views.HomePageView, name="index"),
    path('about/', AboutPageView.as_view(), name='about'),

    path('contacto/', ContactPageView.as_view(), name='contact'),
]