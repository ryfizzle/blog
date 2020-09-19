from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView#basically CRUD
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'list.html'

class CreatePost(CreateView):
    model = Post
    template_name = 'create.html'
    fields = [ 'title' , 'body' , 'image'] 
    success_url = reverse_lazy('list')
    # the currently logged in user is automatically set as post author
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'

class PostDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    
    success_url = reverse_lazy('list')
    # check if the currently logged in user is the one who created the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'update.html'
    fields = [ 'title' , 'body' , 'image'] 
    success_url = reverse_lazy('list')
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
     # check if the currently logged in user is the one who created the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
