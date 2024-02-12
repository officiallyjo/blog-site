from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

from django.views.generic import ListView,DetailView



# Create your views here.


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-Date"]
    context_object_name = "posts"


    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-Date"]
    context_object_name = "all_posts"


class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    