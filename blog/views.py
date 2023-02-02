from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post


# for listing the blogs
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# for details of the blogs
class PostDetailView(DetailView):
    model = Post


# for creating new blogs
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # setting the author of post to user of this particular instance
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# for updating the blogs
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # setting the author of post to user of this particular instance
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True if self.get_object().author_id == self.request.user.pk else False


# for deleting the blogs
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        return True if self.get_object().author_id == self.request.user.pk else False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})