# from django.urls import path
# from .views import (
#     ProductListView, ProductDetailView, ProductCreateView, ProductUpdateDestroyView,
#     CategoryListView, CategoryDetailView,  CategoryListView

# )

# urlpatterns = [
#     path('products/', ProductListView.as_view(), name='product-list'),
#     path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
#     path('products/create/', ProductCreateView.as_view(), name='product-create'),
#     path('products/<int:pk>/manage/', ProductUpdateDestroyView.as_view(), name='product-manage'),
#     path('categories/', CategoryListView.as_view(), name='category-list'),
#     path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
# ]



from django.urls import path
from .views import (
    ProductListView, 
    ProductDetailView,
    ProductCreateView,
    ProductUpdateDestroyView,
    CategoryListView,
    CategoryDetailView
)

urlpatterns = [
    # Product endpoints
    path('', ProductListView.as_view(), name='product-list'),  # GET /api/products/
    path('create/', ProductCreateView.as_view(), name='product-create'),  # POST /api/products/create/
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  # GET /api/products/1/
    path('<int:pk>/manage/', ProductUpdateDestroyView.as_view(), name='product-manage'),  # PUT/DELETE /api/products/1/manage/
    
    # Category endpoints
    path('categories/', CategoryListView.as_view(), name='category-list'),  # GET/POST /api/products/categories/
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),  # GET/PUT/DELETE /api/products/categories/1/
]