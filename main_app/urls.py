from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tinctures/', views.tinctures_index, name='index'),
    path('tinctures/<int:tincture_id>/', views.tinctures_detail, name='detail'),
    path('tinctures/create/', views.TinctureCreate.as_view(), name='tincture_create'),
    path('tinctures/<int:pk>/update/', views.TinctureUpdate.as_view(), name='tinctures_update'),
    path('tinctures/<int:pk>/delete/', views.TinctureDelete.as_view(), name='tinctures_delete'),
]