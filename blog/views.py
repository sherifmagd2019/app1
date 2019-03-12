from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Blog
from .forms import BlogForm


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm

