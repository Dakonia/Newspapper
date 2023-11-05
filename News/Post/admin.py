from django.contrib import admin
from .models import Post, Category, Article, Author, Subscribes

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Subscribes)
# Register your models here.
