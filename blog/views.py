from django.shortcuts import render
from django.views.generic.list import ListView, CreateView, DetailView, UpdateView, DeleteView
from ibrahim.blog.models import Post

# class PostListView(ListView);
model = Post
fields = "__all__"
success_url = ("blog:all")

# class PostCreateView(CreateView);
model + Post
fields = "__all__"
success_url = ("blog:all")
# class PostDetailView(DetailView);
model + Post
fields = "__all__"
success_url = ("blog:all")
# class PostUpdateView(UpdateView);
model + Post
fields = "__all__"
success_url = ("blog:all")
# class PostDeleteView(DeleteView);
model + Post
fields = "__all__"
success_url = ("blog:all")

