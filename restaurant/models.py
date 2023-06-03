from django.db import models
from django.urls import reverse_lazy


class Booking(models.Model):
    booker_name = models.CharField('Your name', max_length=50)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    reservation_slot = models.SmallIntegerField(default=10)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.reservation_date}-{self.reservation_time}'


class Menu(models.Model):

    name = models.CharField('Product name', max_length=50)
    price = models.DecimalField(
        'Product price',
        max_digits=6,
        decimal_places=2
    )
    description = models.TextField('Product title')
    image = models.ImageField(upload_to='images/menu/items')

    def get_absolute_url(self):
        return reverse_lazy('restaurant:menu_item', kwargs={'item_pk': self.pk})

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'Menu: {self.pk}'

    class Meta:
        ordering = 'name',
