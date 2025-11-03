from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import QuoteViewSet

app_name = 'home'

# Router for ViewSet
router = DefaultRouter()
router.register(r'quote', QuoteViewSet, basename='quote')  # Changed from 'quotes' to 'quote' for consistency

urlpatterns = [
    # Frontend views
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('quote/', views.quote, name='quote'),
    path('frontend/', views.frontend_view, name='frontend'),
    
    # CRUD operations
    path('edit/<int:id>/', views.edit_quote, name='edit_quote'),
    path('delete/<int:id>/', views.delete_quote, name='delete_quote'),
    
    # API endpoints - Choose either ViewSet OR function-based views
    # Option 1: ViewSet (recommended)
    path('api/', include(router.urls)),
    
    # Option 2: Function-based views (can be removed if using ViewSet)
    #  path('api/quote/', views.quote_list, name='quote_list'),
    #  path('api/quote/<int:id>/', views.quote_detail, name='quote_detail'),
    path('quote_api/', views.quotes_api, name='quote_api'),
]
