from django import template

from menu.models import Category


register = template.Library()


@register.inclusion_tag('draw_menu/menu.html')
def draw_menu(name=None):
    name = Category.objects.get(name=name)
    return {'cats': name}
