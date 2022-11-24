from django.urls import path, include
from . import views

urlpatterns = [
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_detail),
    path('osoby/update/<int:pk>/', views.osoba_edit),
    path('osoby/delete/<int:pk>/', views.osoba_delete),
    path('osoby/<str:znak>/', views.osoba_znak),
    path('druzyny/', views.druzyna_list),
    path('druzyny/<int:pk>/', views.druzyna_detail),
    path('druzyny/<int:pk>/czlonkowie', views.druzyna_czlonkowie),
]