from django.contrib import admin
from .models import Payment,Order,Order_Product

# Register your models here.
class OrderProductInline(admin.TabularInline):
    model = Order_Product
    readonly_fields=('payment','user','quantity','product','product_price','variation')
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display=['order_number','fullname','phone','email','city','order_total','tax','status','is_ordered','created_at',]
    list_filter=['status','is_ordered']
    search_fields=['order_number','first_name','last_name','phone','email']
    list_per_page=20
    inlines=[OrderProductInline]


admin.site.register(Order,OrderAdmin)
admin.site.register(Order_Product)
admin.site.register(Payment)