from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Comments
from news.forms import CommentForm
from datetime import datetime, timedelta


def news_list(request):
    """Вывод всех новостей
    """
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news": news})


def new_single(request, pk):
    """Вывод полной статьи
    """
    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk, moderation=True)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(new_single, pk)
    else:
        form = CommentForm()
    return render(request, "news/new_single.html",
                  {"new": new,
                   "comments": comment,
                   "form": form})


def news_filter(request, pk):
    """ Фильтр статей по дате
    """
    news = News.objects.all()
    if pk == 1:
        now = datetime.now() - timedelta(minutes=60*24*7)
        news = news.filter(created__gte=now)
    elif pk == 2:
        now = datetime.now() - timedelta(minutes=60*24*30)
        news = news.filter(created__gte=now)
    elif pk == 3:
        news = news
    
    return render(request, "news/news_list.html", {"news": news})
    


