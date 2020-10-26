from django.urls import path

from rest_api import views

urlpatterns = [
    path('', views.ProductsListView.as_view()),
    path('product/<slug:sku>/', views.ProductRUD.as_view()),
    path('product/', views.ProductCreateView.as_view()),

    path('groups/', views.GroupsListView.as_view()),
    path('groups/group/<int:pk>/', views.GroupRUD.as_view()),
    path('groups/group/', views.GroupCreateView.as_view()),

    path('reservations/', views.ReservationsListView.as_view()),
    path('reservations/reservation/<int:pk>/', views.ReservationRUD.as_view()),
    path('reservations/reservation/', views.ReservationCreateView.as_view()),
]