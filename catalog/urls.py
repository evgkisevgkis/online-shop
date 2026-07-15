from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .apps import CatalogConfig
from .views import ProductListView, ProductDetailView, ContactView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("item/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name='item'),
    path("create", ProductCreateView.as_view(), name="product-create"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="product-update"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="product-delete")

]
