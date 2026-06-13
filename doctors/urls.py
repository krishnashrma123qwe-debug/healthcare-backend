from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.DoctorViewSet, basename='doctor')

urlpatterns = [
    path('', include(router.urls)),
]
