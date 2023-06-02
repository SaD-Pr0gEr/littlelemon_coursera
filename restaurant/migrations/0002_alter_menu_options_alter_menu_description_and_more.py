# Generated by Django 4.2.1 on 2023-05-31 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.TextField(verbose_name='Product title'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Product name'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Product price'),
        ),
    ]
