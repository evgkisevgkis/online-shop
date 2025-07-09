from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Article


class ArticleListView(ListView):
    model = Article
    ordering = '-date_created'

class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('name', 'content', 'image', 'is_published')
    success_url = reverse_lazy('blog:blog')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('__all__')
    def get_success_url(self):
        return reverse_lazy('blog:blog-detail', kwargs={'pk': self.object.pk})

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:blog')

