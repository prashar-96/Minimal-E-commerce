from django.contrib import admin

from django.contrib import admin
from .models import Product, Category
from django.utils.functional import SimpleLazyObject
from django.contrib.auth import get_user_model

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_by', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    raw_id_fields = ('created_by',)
    exclude = ['created_by']  # hide from admin form
    
    def save_model(self, request, obj, form, change):
         def save_model(self, request, obj, form, change):
          user = request.user
        
          if isinstance(user, SimpleLazyObject):
            user = user._wrapped

          if not change:
            obj.created_by = user  # ✅ Safe to assign now

         obj.save()
        # if not obj.pk:  # Only set created_by during the first save
        #     user = get_user(request)
        #     obj.created_by = request.user
        # super().save_model(request, obj, form, change)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


from django.contrib import admin
from .models import Product
from django.contrib.auth import get_user  # ✅ This is key

