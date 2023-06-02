from django.urls import path
from . import views


app_name = 'restaurant'
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:item_pk>', views.menu_item_detail, name="menu_item"),
]
