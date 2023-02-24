from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from rest_framework import routers
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, 'products')

urlpatterns = [
    path('', include(router.urls)),  # Dynamic Url with the help of router
    path('documentation/', include_docs_urls(title='CRUD API')),  # Documentation of API ENDPOINTS
]