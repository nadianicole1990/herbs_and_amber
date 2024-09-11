from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('supplies/', views.supplies, name='supplies'),
    path('methods/', views.methods, name='methods'),
    path('tinctures/', views.tinctures_index, name='index'),
    path('tinctures/<int:tincture_id>/', views.tinctures_detail, name='detail'),
    path('herbs/', views.herbs_index, name='herbs_index'),
    path('herbs/<int:herb_id>/', views.herbs_detail, name='herbs_detail'),
    path('tinctures/create/', views.TinctureCreate.as_view(), name='tincture_create'),
    path('tinctures/<int:pk>/update/', views.TinctureUpdate.as_view(), name='tinctures_update'),
    path('tinctures/<int:pk>/delete/', views.TinctureDelete.as_view(), name='tinctures_delete'),
    path('herbs/create/', views.HerbCreate.as_view(), name='herb_create'),
    path('herbs/<int:pk>/update/', views.HerbUpdate.as_view(), name='herbs_update'),
    path('herbs/<int:pk>/delete/', views.HerbDelete.as_view(), name='herbs_delete'),
    path('tinctures/<int:tincture_id>/add_batch/', views.add_batch, name='add_batch'),
]