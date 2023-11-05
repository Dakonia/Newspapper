from django.views.generic import ListView, CreateView
from .models import Post, Article
from .forms import PostForm

class AllPostsAndArticlesView(ListView):
    template_name = 'index.html'
    context_object_name = 'all_posts_and_articles'
    paginate_by = 10

    def get_queryset(self):
        all_posts_and_articles = list(Post.objects.all()) + list(Article.objects.all())
        all_posts_and_articles.sort(key=lambda x: x.data, reverse=True)
        return all_posts_and_articles

class PostList(ListView):
    model = Post
    ordering = 'data'
    template_name = 'postall.html'
    context_object_name = 'post'

class ArticleList(ListView):
    model = Article
    ordering = 'data'
    template_name = 'articleall.html'
    context_object_name = 'article'

class PostCreate(CreateView):
    permission_required = ('new.add_post',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.author
        return super().form_valid(form)
