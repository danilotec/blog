from django.db import models

class Author(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=30)
    email = models.EmailField(verbose_name='Email')

    def __str__(self) -> str:
        return self.name

class Article(models.Model):
    title = models.CharField(verbose_name='Titulo',max_length=200)
    article = models.TextField(verbose_name='Artigo')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
