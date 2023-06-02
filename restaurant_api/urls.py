from django.urls import path
from . import views


app_name = 'restaurant_api'
urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
]
