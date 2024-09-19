from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    path('',views.Store,name='store'),
    path('<slug:category_slug>/',views.Store,name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>',views.product_details,name='product_details'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
