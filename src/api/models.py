import time

from django.db import models


# Create your models here.


# def file_directory_path(instance, filename):
#     return f'src/api/static/files/file_{time.time()}_{filename}'


def file_directory_path(instance, filename):
    return f'src/api/static/files/file_{time.time()}_{filename}'


class FileCSV(models.Model):
    file = models.FileField(upload_to=file_directory_path, verbose_name='Ваш файл')


class Customer(models.Model):
    login = models.CharField(max_length=100, unique=True, verbose_name='Покупатель')


class PurchaseDate(models.Model):
    date = models.DateTimeField()
    customer = models.ManyToManyField(Customer)


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название товара')
    total = models.IntegerField()


class ItemAndCustomer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количеств')
