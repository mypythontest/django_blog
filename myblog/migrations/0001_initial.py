# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('desc', models.CharField(max_length=50, verbose_name='文章描述')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章内容')),
                ('click_count', models.IntegerField(default=0, verbose_name='点击次数')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='是否推荐')),
                ('date_publish', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_publish'],
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='分类名称')),
                ('index', models.IntegerField(default=999, verbose_name='显示顺序(从小到大)')),
            ],
            options={
                'ordering': ['index', 'id'],
                'verbose_name_plural': '分类',
                'verbose_name': '分类',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(null=True, max_length=30, verbose_name='用户名', blank=True)),
                ('content', models.TextField(max_length=150, verbose_name='留言内容')),
                ('date_publish', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_publish'],
                'verbose_name_plural': '留言',
                'verbose_name': '留言',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='标签名称')),
                ('weight', models.IntegerField(default=10, verbose_name='标签大小')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': '标签',
                'verbose_name': '标签',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='myblog.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(verbose_name='标签', to='myblog.Tag'),
        ),
    ]
