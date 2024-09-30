from django.shortcuts import render
from catalog.models import Product


def home(request):
    products = Product.objects.order_by('-created')[:5]
    print(products)
    return render(request, 'home.html', {'products': products})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) - {message}')
    return render(request, 'contacts.html')
