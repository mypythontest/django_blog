# coding=utf8

from django_blog.settings.base import SLOGAN, SITE_NAME
from .models import Category, Tag, Article


def base(request):
    categories = Category.objects.all()
    tag_list = Tag.objects.all()
    recommendation = Article.objects.filter(is_recommend=True)[:7]
    site_name = SITE_NAME
    slogan = SLOGAN
    return locals()
