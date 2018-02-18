from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from news.models import News, Category, Tag, Comments


class NewsAdmin(SummernoteModelAdmin):
    """ Новости
    """
    list_display = ("title", "user", "created")
    list_editable = ("user", )
    search_fields = ["title", "user__username"]
    list_filter = ("user", "created")
    summer_note_fields = ('text_min', 'text')


class CommentAdmin(admin.ModelAdmin):
    """ Комментарии
    """
    list_display = ('user', 'new', 'created', 'moderation')


admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Category)
admin.site.register(Tag)
