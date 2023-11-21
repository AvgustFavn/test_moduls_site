from django.shortcuts import render
from models_site.models import Product

from models_site.utils import load_data


def home(req):
    # load_data()
    products = Product.objects.all()
    return render(req, 'main.html', context={'products': products})
