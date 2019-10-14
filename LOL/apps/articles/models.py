from django.db import models
import datetime
from django.utils import timezone


class Article(models.Model):
    articleTitle = models.CharField("Article name", max_length=200)
    articleText = models.TextField("Main text")
    pupDate = models.DateField("Publication date")

    def __str__(self):
        return self.articleTitle

    def was_published_recently(self):
        return self.pupDate >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


# noinspection PyArgumentList
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    authorName = models.CharField("Authors name", max_length=50)
    commentText = models.CharField("Text field", max_length=200)
    pubDate = models.DateField("Publication date")

    def __str__(self):
        return self.authorName
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"