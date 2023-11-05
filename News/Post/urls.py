from django.urls import path
from .views import AllPostsAndArticlesView, PostList, ArticleList, PostCreate

urlpatterns = [
    path('', AllPostsAndArticlesView.as_view(), name='all_posts_and_articles'),
    path('post/', PostList.as_view(), name='post_list'),  # Добавьте URL-маршрут для постов
    path('article/', ArticleList.as_view(), name='article_list'),  # Добавьте URL-маршрут для статей
    path('create/', PostCreate.as_view(), name='post_create'),
]
