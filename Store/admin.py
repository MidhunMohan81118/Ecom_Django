from django.contrib import admin
from .models import Product  # Ensure your Product model is imported correctly

# Register your models here.
class ProductAdmin(admin.ModelAdmin):  # Use admin.ModelAdmin, not models.ModelAdmin
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)
