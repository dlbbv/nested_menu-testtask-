from django.shortcuts import render


def draw_menu(request, path=None, instance=None):
    data = {
        'path': path,
        'instance': instance
    }
    return render(request, 'draw_menu/test.html', context=data)
