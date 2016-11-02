from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django_blog.settings import SLOGAN, SITE_NAME


# 全局传递的数据
def base(request):
    cat = Category.objects.all()
    tag_list = Tag.objects.all()
    recommendation = Article.objects.filter(is_recommend=True)[:7]
    site_name = SITE_NAME
    slogan = SLOGAN
    return locals()


# 获取文章列表
def article_view(request):
    article_list = Article.objects.all()
    article_list = get_page(request, article_list)
    return render(request, 'index.html', {'article_list': article_list})


# 文章详细
def content_detail(request, title):
    content = get_object_or_404(Article, title=title)
    content.click_count += 1
    content.save()
    return render(request, 'content.html', {'content': content})


# 文章分类
def get_category(request, category):
    is_cat = True
    category = get_object_or_404(Category, name=category)
    article_list = get_page(request, category.article_set.all())
    return render(request, 'index.html', {'article_list': article_list, 'is_cat': is_cat})


def me(request):
    return render(request, 'me.html')


# 文章归档
def get_archive(request):
    return render(request, 'archive.html')


# 标签
def get_tag(request, tag):
    is_tag = True
    tag = get_object_or_404(Tag, id=tag)
    article_list = get_page(request, tag.article_set.all())
    return render(request, 'index.html', locals())


# 搜索
def search(request):
    is_search = True
    title = request.GET.get('search')
    article_list = get_page(request, Article.objects.filter(title__icontains=title))
    return render(request, 'index.html', locals())


# 留言
def message(request):
    return render(request, 'message.html')


# 分页函数
def get_page(request, article_list, num=4):
    paginator = Paginator(article_list, num)
    try:
        page = request.GET.get('page')
        article_list = paginator.page(page)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    return article_list
