from django.urls import path 
from . import views
from .views import RegisterView, CustomTokenObtainPairView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout')
    # path('', views.product_list, name='product-list'),
    # path('<int:pk>/', views.product_detail, name='product-detail'),
]
