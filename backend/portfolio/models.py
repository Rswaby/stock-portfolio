from django.db import models

# Create your models here.


class StockUser(models.Model):
    userID = models.CharField(max_length=1000, primary_key=True)
    userName = models.CharField(max_length=100)
    bank = models.IntegerField()

    def __str__(self):
        return str(self.userName)


class Stock(models.Model):
    symbol = models.CharField(max_length=10, primary_key=True)
    lastUpdated = models.DateTimeField()
    volume = models.IntegerField()
    _open = models.FloatField()
    _high = models.FloatField()
    _low = models.FloatField()
    _close = models.FloatField()

    def __str__(self):
        return self.symbol


class Transactions(models.Model):
    user = models.ForeignKey(StockUser, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True)
    shares = models.IntegerField(null=True)
    amount_payed = models.FloatField(null=True)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
