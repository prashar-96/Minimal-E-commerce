from django.urls import path
from .views import CartView, AddToCartView, UpdateCartItemView, RemoveFromCartView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/', AddToCartView.as_view(), name='add-to-cart'),
    path('items/<int:pk>/update/', UpdateCartItemView.as_view(), name='update-cart-item'),
    path('items/<int:pk>/remove/', RemoveFromCartView.as_view(), name='remove-cart-item'),
]