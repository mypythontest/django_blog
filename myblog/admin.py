from django.contrib import admin
from .models import *
# Register your models here.


class Articlelist(admin.ModelAdmin):
    list_display = ('title', 'desc', 'date_publish',)
    filter_horizontal = ('tag',)
    search_fields = ('title',)

admin.site.register(Article, Articlelist)
admin.site.register(Tag)
admin.site.register(Category)
