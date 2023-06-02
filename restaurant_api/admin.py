from django.contrib import admin

from restaurant_api.models import MenuItem, Category

admin.site.register(Category)
admin.site.register(MenuItem)
