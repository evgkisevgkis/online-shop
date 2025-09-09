from django.urls import path

from . import views
from .apps import CatalogConfig
from .views import ProductListView, ProductDetailView, ContactView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("item/<int:pk>/", ProductDetailView.as_view(), name='item'),
    path("create", ProductCreateView.as_view(), name="product-create"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="product-update"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="product-delete")

]
