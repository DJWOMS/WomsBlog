from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from news.models import News, Category, Tag, Comments


class NewsAdmin(SummernoteModelAdmin):
    summer_note_fields = ('text_min', 'text')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')


admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Category)
admin.site.register(Tag)
