from django.shortcuts import render, get_object_or_404
from .models import Article
import markdown

def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_detail(request, pk):
    articles = Article.objects.all()
    article = get_object_or_404(Article, pk=pk)
    article.article_html = markdown.markdown(article.article) #type: ignore
    return render(
        request,
        "blog/index.html",
        {"articles": articles, "article": article},
    )