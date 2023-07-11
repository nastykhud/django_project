from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('item/<int:num>', views.item_info),
    path('items', views.items_info),
]
