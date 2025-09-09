from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ContactForm, ProductForm
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('home')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    def get_success_url(self):
        return reverse_lazy('item', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('home')
