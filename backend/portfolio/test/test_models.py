from django.test import TestCase
from portfolio.models import *
# Create your tests here.
import datetime

class StockTestCase(TestCase):

    def setUp(self):
        StockUser.objects.create(
            userID="test_model_1",
            userName="user_name1",
            bank=5000
        )

        StockUser.objects.create(
            userID="test_model_2",
            userName="user_name2",
            bank=5000
        )
        Stock.objects.create(
            symbol="testSymbol",
            lastUpdated = datetime.datetime.now(),
            volume=1000,
            _open=1000.0,
            _high=1000.0,
            _low=1000.0,
            _close=1000.0
        )

    def test_stock_user(self):
        user1 = StockUser.objects.get(userID="test_model_1")
        user2 = StockUser.objects.get(userID="test_model_2")
        queryset = StockUser.objects.all()
        self.assertEqual(user1.userName,"user_name1")
        self.assertEqual(user2.userName, "user_name2")
        self.assertEqual(len(queryset),2)
    def test_stock(self):
        stock = Stock.objects.get(symbol="testSymbol")
        self.assertEqual(stock.volume, 1000)
