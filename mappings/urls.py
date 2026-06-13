from django.urls import path
from . import views

urlpatterns = [
    path('', views.mapping_list_create, name='mapping-list-create'),
    path('<int:pk>/', views.mapping_detail, name='mapping-detail'),
]
