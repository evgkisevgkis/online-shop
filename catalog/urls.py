from django.urls import path
from django.views.decorators.cache import never_cache, cache_page
from django.conf import settings

from . import views
from .apps import CatalogConfig
from .views import ProductListView, ProductDetailView, ContactView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

if settings.FULL_CACHE:
    urlpatterns = [
        path("", ProductListView.as_view(), name="home"),
        path("contacts/", ContactView.as_view(), name="contacts"),
        path("item/<int:pk>/", ProductDetailView.as_view(), name='item'),
        path("create", never_cache(ProductCreateView.as_view()), name="product-create"),
        path("update/<int:pk>", never_cache(ProductUpdateView.as_view()), name="product-update"),
        path("delete/<int:pk>", ProductDeleteView.as_view(), name="product-delete")
    ]
else:
    urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("item/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name='item'),
    path("create", ProductCreateView.as_view(), name="product-create"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="product-update"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="product-delete")
    ]
