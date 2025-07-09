from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("", ArticleListView.as_view(), name="blog"),
    path("<int:pk>", ArticleDetailView.as_view(), name="blog-detail"),
    path("create", ArticleCreateView.as_view(), name="blog-create"),
    path("update/<int:pk>", ArticleUpdateView.as_view(), name="blog-update"),
    path("delete/<int:pk>", ArticleDeleteView.as_view(), name="blog-delete")
]