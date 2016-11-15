from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.urlresolvers import reverse


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名称')

    def get_absolute_url(self):
        return reverse('tag', args=[self.name])

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name

    def articles_count(self):
        return self.articles.count()


# 文章分类
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称', unique=True)

    def get_absolute_url(self):
        return reverse('category', args=[self.name])

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题', unique=True)
    desc = models.CharField(max_length=50, verbose_name='文章描述')
    content = RichTextUploadingField(config_name='default', verbose_name='文章内容')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    category = models.ForeignKey(Category, blank=False, null=False, verbose_name='分类', to_field='name')
    tag = models.ManyToManyField(Tag, verbose_name='标签', related_name='articles')

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.title])

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title




