from cmath import log
from django.conf import settings
import requests

class APIKeyMissingError(Exception):
    pass


BASE_URL = "https://www.alphavantage.co/query"
def make_api_call(symbol, function, interval ="5min"):
    if settings.API_KEY == None:
        raise APIKeyMissingError(
                "All methonds require an API key. "
                "Go to https://www.alphavantage.co/ "
                "to retreive and api key then add to .env file in app directory"
                )
        
    if function == 'TIME_SERIES_INTRADAY':
        params={'function':function,'symbol':symbol,'interval':interval,'apikey':settings.API_KEY}
        res = requests.get(BASE_URL,params=params)
        print(f'sending request for {function}')
        return res.json()

    if function == 'SYMBOL_SEARCH':
        params={'function':function,'keywords':symbol,'apikey':settings.API_KEY}
        res = requests.get(BASE_URL,params=params)
        print(f'sending request for {function}')
        return res.json()


class AlphaApi():

    @staticmethod
    def search_symbol(symbol):
                return make_api_call(symbol,"SYMBOL_SEARCH")
    
    @staticmethod
    def get_intra_day(symbol):
        return make_api_call(symbol,"TIME_SERIES_INTRADAY")