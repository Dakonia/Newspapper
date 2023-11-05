from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    type = models.CharField(max_length=10, default='Новость')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.author:
            # Если автор не установлен, установите его на основе текущего пользователя
            self.author, created = Author.objects.get_or_create(author=self._get_current_user())
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}: {self.category.name[:20]}'

    def _get_current_user(self):
        # Получение текущего пользователя, который выполняет действие
        return User.objects.get(username='ваш_пользователь')

class Article(models.Model):
    type = models.CharField(max_length=10, default='Статья')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.author:
            # Если автор не установлен, установите его на основе текущего пользователя
            self.author, created = Author.objects.get_or_create(author=self._get_current_user())
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}: {self.category.name[:20]}'

    def _get_current_user(self):
        # Получение текущего пользователя, который выполняет действие
        return User.objects.get(username='ваш_пользователь')

class Subscribes(models.Model):
    subscribes = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentArticle = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.text()}: {self.description[:20]}'
