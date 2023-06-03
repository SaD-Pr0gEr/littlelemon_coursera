from django.urls import path
from . import views


app_name = 'restaurant_api'
urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    path('menu-items', views.MenuViewSet.as_view({
        'get': 'list'
    }), name='menu_items'),
    path('menu-items/<int:pk>', views.MenuViewSet.as_view({
        'get': 'retrieve'
    })),
    path('book', views.BookingViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='bookings'),
    path('book/<int:pk>', views.BookingViewSet.as_view({
        'get': 'retrieve',
    }))
]
