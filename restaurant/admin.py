from django.contrib import admin
from restaurant.models import Menu, Booking


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price']
    list_display_links = ['name']
    list_editable = ['price']


admin.site.register(Booking)
