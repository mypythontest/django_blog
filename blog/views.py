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
        queryset = Article.objects.all()
        articles = self.paginate_queryset(queryset, page_size=4)[1]
        return articles


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
        queryset = Article.objects.filter(category=self.kwargs['category'])
        articles = self.paginate_queryset(queryset, page_size=4)[1]
        return articles

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['is_category'] = True
        context['category'] = self.kwargs['category']
        return context


class TagListView(BaseListView):
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Tag.objects.get(name=self.kwargs['tag']).articles.all()
        articles = self.paginate_queryset(queryset, page_size=4)[1]
        return articles

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context['is_tag'] = True
        context['tag'] = self.kwargs['tag']
        return context


class Me(TemplateView):
    template_name = 'me.html'


class ArchiveView(TemplateView):
    template_name = 'archive.html'


class MessageView(TemplateView):
    template_name = 'message.html'


class SearchView(BaseListView):
    template_name = 'index.html'
    
    def get_queryset(self):
        queryset = Article.objects.filter(title__icontains=self.request.GET.get('search'))
        articles = self.paginate_queryset(queryset, page_size=4)[1]
        return articles


