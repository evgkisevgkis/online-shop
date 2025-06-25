from django.urls import path

from . import views
from .views import ProductListView, ProductDetailView, ContactView

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("item/<int:pk>/", ProductDetailView.as_view(), name='item')
]
