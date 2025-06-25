from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ContactForm
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return self.model.objects.order_by('-created')[:5]


class ContactView(CreateView):
    template_name = 'catalog/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts')


class ProductDetailView(DetailView):
    model = Product

