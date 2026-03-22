from django.urls import path
from . import views

app_name = 'magazin'

urlpatterns = [
    path('list/', views.magazin_list, name='magazin_list'),
    path('create/', views.magazin_create, name='magazin_create'),
    path('delete/<int:id>/', views.magazin_delete, name='magazin_delete'),
    path('update/<int:id>/', views.magazin_update, name='magazin_update'),



#   profil oyna
    path('profil/list/', views.profil_list, name='profil_list'),
    path('profil/create/', views.profil_create, name='profil_create'),
    path('profil/<int:id>/update/', views.profil_update, name='profil_update'),
    path('profil/<int:id>/delete/', views.profil_delete, name='profil_delete')
]