from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Article


class ArticleListView(ListView):
    model = Article
    ordering = '-date_created'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        if self.object.views_count == 100:
            self.send_notification(self.object)
        return self.object

    def send_notification(self, article):
        subject = f'Статья {article.name} набрала 100 просмотров'
        message = 'Ура, статья набрала 100 просмотров.'
        from_email = 'evgeny-kiselev-95@yandex.ru'
        recipient_list = ['evgkisevgkis@gmail.com']
        send_mail(subject, message, from_email, recipient_list)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ('name', 'content', 'image', 'is_published')
    success_url = reverse_lazy('blog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.name)
            new_article.save()
            return super().form_valid(form)


class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    model = Article
    fields = ('__all__')
    permission_required = 'blog.change_article'
    def get_success_url(self):
        return reverse_lazy('blog:blog-detail', kwargs={'pk': self.object.pk})


class ArticleDeleteView(UserPassesTestMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('blog:blog')
    
    def test_func(self):
        return self.request.user.is_superuser

