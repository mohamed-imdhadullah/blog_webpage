from dataclasses import fields
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
#post update, delete
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#login required for create, update, delete post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#fuction views
def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

#class view
class PostListView(ListView):
    model = Post
    # app/model_viewtype.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    #post ordering
    ordering = ['-date_posted']
    #adding next, previous page and set 5 post to single page
    paginate_by = 5

#for user post list view
class UserPostListView(ListView):
    model = Post
    # app/model_viewtype.html
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    #adding next, previous page and set 5 post to single page
    paginate_by = 5

    #for query set
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
   

#detail view
class PostDetailView(DetailView):
    model = Post

#create view
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content',]

    #save post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#update view
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content',]

    #save post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #testing the current user for their posts
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#delete view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url ='/'

    #testing the current user for their posts
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





