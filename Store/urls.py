from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    path('',views.Store,name='store'),
    path('category/<slug:category_slug>/',views.Store,name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>',views.product_details,name='product_details'),
    path('search',views.search,name='search'),  
    path('submit_review/<int:id>/',views.submit_review,name='review_submiting')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
