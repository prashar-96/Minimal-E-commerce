from django.contrib import admin

from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_by', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    raw_id_fields = ('created_by',)
    exclude = ['created_by']  # hide from admin form
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set created_by during the first save
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


from django.contrib import admin
from .models import Product
from django.contrib.auth import get_user  # ✅ This is key

