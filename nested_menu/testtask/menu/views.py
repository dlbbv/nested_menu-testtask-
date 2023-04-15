from django.shortcuts import render

from .models import Category


def category(request, path, instance):
    return render(request, 'menu/test.html', {
        'instance': instance,
        'children': instance.get_children() if instance else Category.objects.root_nodes(),
        'menu': Category.objects.root_nodes()
    })