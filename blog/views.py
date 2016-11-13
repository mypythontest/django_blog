from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView


class BaseListView(ListView):
    context_object_name = 'article_list'


class ArticleView(BaseListView):
    template_name = 'index.html'

    def get_queryset(self):
        articles = Article.objects.all()
        return paginate(self.request, articles)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'
    slug_url_kwarg = 'title'
    slug_field = 'title'

    def get_object(self, queryset=None):
        article = super(ArticleDetailView, self).get_object(queryset)
        article.click_count += 1
        article.save()
        return article


class CategoryListView(BaseListView):
    template_name = 'index.html'

    def get_queryset(self):
        articles = Article.object.filter(category=self.kwargs['category'])
        return paginate(self.request, articles)

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['is_category'] = True


class Me(TemplateView):
    template_name = 'me.html'


class ArchiveView(TemplateView):
    template_name = 'archive.html'


class TagListView(BaseListView):
    template_name = 'index.html'

    def get_queryset(self):
        articles = Article.object.filter(tag=self.kwargs['tag'])
        return paginate(self.request, articles)

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context['is_tag'] = True


def search(request):
    is_search = True
    title = request.GET.get('search')
    article_list = paginate(request, Article.objects.filter(title__icontains=title))
    return render(request, 'index.html', locals())


class MessageView(TemplateView):
    template_name = 'message.html'


def paginate(request, article_list, num=4):
    paginator = Paginator(article_list, num)
    try:
        page = request.GET.get('page')
        article_list = paginator.page(page)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    return article_list
