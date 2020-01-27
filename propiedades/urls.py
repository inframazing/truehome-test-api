from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.propiedad_form, name='propiedad_insert'),  # For insert
    path('<int:id>/', views.propiedad_form, name='propiedad_update'),  # For update
    path('delete/<int:id>', views.propiedad_delete, name='employee_delete'),  # For delete
    path('list/', views.propiedad_list, name='propiedad_list')  # For display all records
]
