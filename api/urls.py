from django.urls import path
from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  assetview

router = DefaultRouter()
router.register(r'assets',  assetview)

urlpatterns = [
    path('', include(router.urls)),
]