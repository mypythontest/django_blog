from .models import *

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView


class BaseListView(ListView):
    context_object_name = 'article_list'
    paginate_by = 5


class ArticleView(BaseListView):
    template_name = 'index.html'
    model = Article


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

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)

        try:
            prev_article = Article.objects.filter(pk__lt=self.object.id).order_by('-pk')[0]
        except IndexError:
            prev_article = None
        try:
            next_article = Article.objects.filter(pk__gt=self.object.id).order_by('pk')[0]
        except IndexError:
            next_article = None

        context['prev_article'] = prev_article
        context['next_article'] = next_article
        return context


class CategoryListView(BaseListView):
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Article.objects.filter(category=self.kwargs['category'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['is_category'] = True
        context['category'] = self.kwargs['category']
        return context


class TagListView(BaseListView):
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Tag.objects.get(name=self.kwargs['tag']).articles.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context['is_tag'] = True
        context['tag'] = self.kwargs['tag']
        return context


class SearchView(BaseListView):
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Article.objects.filter(title__icontains=self.request.GET.get('search'))
        return queryset


class Me(TemplateView):
    template_name = 'me.html'


class ArchiveView(BaseListView):
    template_name = 'archive.html'
    paginate_by = None

    def get_queryset(self):
        articles = Article.objects.all()
        for article in articles:
            article.yeah_month = article.date_publish.strftime('%Y-%m')
        return articles


class MessageView(TemplateView):
    template_name = 'message.html'
