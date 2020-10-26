from django.db import models


class ProductGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.SlugField(max_length=64, primary_key=True)
    name = models.CharField(max_length=100)
    group = models.ForeignKey(ProductGroup, on_delete=models.SET_NULL, null=True)
    stock_balance = models.IntegerField()

    def balance_including_reservation(self):
        """
        Метод возвращает кол-во товара на складе минус зарезервированное кол-во
        """
        reservations = Reservation.objects.filter(product_sku=self.sku)
        return self.stock_balance - sum([x.count for x in reservations])

    def __str__(self):
        return self.sku


class Reservation(models.Model):
    email = models.EmailField(blank=False)
    product_sku = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reservations')
    count = models.IntegerField()

    def __str__(self):
        return f'{self.email} - {self.count}'
