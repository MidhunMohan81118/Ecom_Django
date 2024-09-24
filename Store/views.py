from django.shortcuts import render,get_object_or_404,HttpResponse
from . models import Product
from Category.models import Category
from Cart.models import CartItem
from Cart.views import _cart_id
from django.db.models import Q

from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger

# Create your views here.
def Store(request,category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=categories,is_available=True)
        pagenator = Paginator(products,6) #for pagenation
        page = request.GET.get('page')
        paged_product = pagenator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        pagenator = Paginator(products,3) #for pagenation
        page = request.GET.get('page')
        paged_product = pagenator.get_page(page)
        product_count = products.count()
    context = {
        'Products':paged_product,
        'Product_Count':product_count,
        }

    return render(request,'store/store.html',context)

def product_details(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product=single_product).exists()
        
    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
        'In_cart':in_cart
    }
    return render(request,'store/product_details.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            Products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) |Q(product_name__icontains=keyword))
            #Q is for making search with many conditions. or operation in querry is done using Q.
            product_count = Products.count()
            context={
                'Products':Products,
                'Product_Count':product_count,
            }
    return render(request,'store/store.html',context)  