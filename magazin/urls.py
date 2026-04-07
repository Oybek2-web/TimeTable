from django.urls import path
from . import views

app_name = 'magazin'

urlpatterns = [
    path('list/', views.time_table_list, name='time_table_list'),
    path('create/', views.time_table_create, name='time_table_create'),
    path('delete/<int:id>/', views.time_table_delete, name='time_table_delete'),
    path('update/<int:id>/', views.time_table_update, name='time_table_update'),


#   profil oyna

    path('profil/list/', views.profil_list, name='profil_list'),
    path('profil/create/', views.profil_create, name='profil_create'),
    path('profil/<int:id>/update/', views.profil_update, name='profil_update'),
    path('profil/<int:id>/delete/', views.profil_delete, name='profil_delete')
]