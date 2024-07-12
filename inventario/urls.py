from django.urls import path
from . import views

urlpatterns = [
    path("inventario", views.inventario_view, name='inventario'),
    path('update/<int:pk>/<str:action>/', views.update_quantity, name='update_quantity'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]
