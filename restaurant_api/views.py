from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from restaurant.models import Booking
from .models import MenuItem, Category
from .serializers import MenuSerializer, CategorySerializer, BookingSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all().order_by('id')
    serializer_class = BookingSerializer
    filterset_fields = ['reservation_date']
    permission_classes = [IsAuthenticated]


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class MenuViewSet(ModelViewSet):
    queryset = MenuItem.objects.all().order_by('pk')
    serializer_class = MenuSerializer
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']
