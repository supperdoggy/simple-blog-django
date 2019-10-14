from django.shortcuts import render
from django.utils import timezone
from django.http import Http404, HttpResponseRedirect
from .models import Article
from django.urls import reverse


def index(request):
    latestArticles_list = Article.objects.order_by('-pupDate')[:5]
    return render(request, "articles/list.html", {"latestArticles_list": latestArticles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")

    latestCommentsList = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latestCommentsList': latestCommentsList})


def leaveComment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)

    except:
        raise Http404("Статья не найдена")
    a.comment_set.create(authorName=request.POST['name'], commentText=request.POST['text'], pubDate=timezone.now())

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))
