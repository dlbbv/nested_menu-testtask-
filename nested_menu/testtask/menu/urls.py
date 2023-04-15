from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
import mptt_urls

from .models import Category
from .views import category


urlpatterns = [
    re_path(r'^home/$/', TemplateView.as_view(template_name='menu/test.html'), name='menu'),
    re_path(r'^home/(?P<path>.*)', mptt_urls.view(model=Category,
                                             view=category,
                                             slug_field='slug',
                                             trailing_slash=False), name='menu'),
    path('admin/', admin.site.urls),
]
