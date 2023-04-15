from django.urls import path

from .views import draw_menu


urlpatterns = [
    path('draw_menu/', draw_menu),
]