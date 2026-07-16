from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from blog.apps import BlogConfig
from django.conf import settings
from django.views.decorators.cache import never_cache

app_name = BlogConfig.name

if settings.FULL_CACHE:
    urlpatterns = [
        path("", ArticleListView.as_view(), name="blog"),
        path("<int:pk>", ArticleDetailView.as_view(), name="blog-detail"),
        path("create", never_cache(ArticleCreateView.as_view()), name="blog-create"),
        path("update/<int:pk>", never_cache(ArticleUpdateView.as_view()), name="blog-update"),
        path("delete/<int:pk>", ArticleDeleteView.as_view(), name="blog-delete")
    ]
else:
    urlpatterns = [
    path("", ArticleListView.as_view(), name="blog"),
    path("<int:pk>", ArticleDetailView.as_view(), name="blog-detail"),
    path("create", ArticleCreateView.as_view(), name="blog-create"),
    path("update/<int:pk>", ArticleUpdateView.as_view(), name="blog-update"),
    path("delete/<int:pk>", ArticleDeleteView.as_view(), name="blog-delete")
    ]