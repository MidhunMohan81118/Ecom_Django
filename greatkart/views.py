from django.http import HttpResponse
from django.shortcuts import render
from Store.models import Product,ReviewRating

# def home(request):
#     products = Product.objects.all().filter(is_available=True).order_by('created_date')

#     # Review details
#     for product in products:
#         reviews = ReviewRating.objects.filter(product_id=product.id,status=True)

#     context ={
#         'products': products,
#         'reviews':reviews,
#     }
#     return render(request,'home.html',context)/

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    # Initialize reviews as an empty dictionary or list (depending on the structure you want)
    reviews = {}

    # Review details
    for product in products:
        product_reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
        reviews[product.id] = product_reviews  # Store reviews for each product by its ID

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)
