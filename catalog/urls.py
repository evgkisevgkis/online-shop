from django.urls import path

from . import views
from .views import ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("item/<int:item_id>/", views.item)
]
