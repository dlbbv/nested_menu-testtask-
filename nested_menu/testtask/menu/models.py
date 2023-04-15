from django.db import models
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=32, verbose_name='Category name')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, verbose_name='Parent category', related_name='categories')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu', kwargs={'path': self.get_path()})