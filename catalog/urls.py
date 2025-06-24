from django.urls import path

from . import views
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("item/<int:pk>/", ProductDetailView.as_view(), name='item')
]
