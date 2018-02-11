# coding=utf-8
from django.forms import ModelForm
from .models import Comments


class CommentForm(ModelForm):
    """Форма комментариев к статьям
    """
    class Meta:
        model = Comments
        fields = ('text', )