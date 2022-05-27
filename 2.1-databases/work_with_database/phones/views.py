from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    sort_dict = {'name': 'name', 'min_price': 'price', 'max_price': '-price'}
    if sort:
        item = Phone.objects.all().order_by(sort_dict.get(sort))
    else:
        item = Phone.objects.all()

    context = {
        'phones': item
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    item = Phone.objects.filter(slug=slug)
    context = {
        'phones': item
    }
    return render(request, template, context)
