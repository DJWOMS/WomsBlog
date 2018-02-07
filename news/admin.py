from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from news.models import News, Category, Tag, Commets


class NewsAdmin(SummernoteModelAdmin):
    summer_note_fields = ('text_min', 'text')

admin.site.register(News, NewsAdmin)

admin.site.register(Category)
admin.site.register(Tag)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')
    
admin.site.register(Commets, CommentAdmin)

