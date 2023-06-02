from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import BookingForm
from .models import Menu


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    form: ModelForm = BookingForm()
    if request.method == 'POST':
        form: ModelForm = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)


def menu(request: HttpRequest) -> HttpResponse:
    menu_items: list[Menu] = Menu.objects.all()
    return render(
        request,
        'menu.html',
        {'menu_items': menu_items}
    )


def menu_item_detail(request: HttpRequest, item_pk: int) -> HttpResponse:
    menu_item: Menu = get_object_or_404(Menu, pk=item_pk)
    return render(
        request,
        'menu_detail.html',
        {
            'menu_item': menu_item,
            'sitemap_links': [
                {
                    'name': 'Home',
                    'link': reverse_lazy('restaurant:home')
                },
                {
                    'name': 'Menu',
                    'link': reverse_lazy('restaurant:menu')
                },
                {
                    'name': menu_item.name,
                    'link': request.path,
                    'current_path': True
                },
            ]
        }
    )
