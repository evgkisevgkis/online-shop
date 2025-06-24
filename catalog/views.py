from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return self.model.objects.order_by('-created')[:5]


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) - {message}')
    return render(request, 'catalog/contacts.html')


def item(request, item_id):
    one_item = Product.objects.get(pk=item_id)
    context = {
        'one_item': one_item,
    }
    return render(request, 'catalog/item.html', context)
