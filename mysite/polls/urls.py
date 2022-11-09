from django.urls import path, include
from . import views

urlpatterns = [
    # path('osoby/', views.osoba_list),
    # path('osoby/<int:pk>/', views.osoba_detail),
    # path('osoby/<str:znak>/', views.osoba_znak),
    path('osoby/', views.OsobaList.as_view()),
    path('osoby/<int:pk>/', views.OsobaDetail.as_view()),
    path('osoby/<str:znak>/', views.OsobaSignSearch.as_view()),
    path('druzyny/', views.druzyna_list),
    path('druzyny/<int:pk>/', views.druzyna_detail),
]