import requests
import json
from TickerItem import TickerItem

COMMAND_TICKER = 'returnTicker'
COMMAND_24VOLUME = 'return24hVolume'
COMMAND_ORDERBOOK = 'returnOrderBook'
COMMAND_TRADEHISTORY = 'returnTradeHistory'
COMMAND_CHARTDATA = 'returnChartData'
COMMAND_CURRENCIES = 'returnCurrencies'
COMMAND_LOANORDERS = 'returnLoanOrders'


class PyPublicPoloClient:

    apiKey = ''
    secret = ''
    baseUrl = 'https://poloniex.com/public'

    def __init__(self):
        return

    def get_ticker(self, sort_key=None, reverse=False):
        ticker_dict = self.__send_request(COMMAND_TICKER)

        ticker_list = []

        for key in ticker_dict.keys():
            ticker_list.append(TickerItem(key,
                ticker_dict[key]['id'],
                ticker_dict[key]['last'],
                ticker_dict[key]['lowestAsk'],
                ticker_dict[key]['highestBid'],
                ticker_dict[key]['percentChange'],
                ticker_dict[key]['baseVolume'],
                ticker_dict[key]['quoteVolume'],
                ticker_dict[key]['isFrozen'],
                ticker_dict[key]['high24hr'],
                ticker_dict[key]['low24hr']))

        if sort_key is not None:
            ticker_list.sort(key=lambda x: getattr(x, sort_key), reverse=reverse)

        return ticker_list

    def get_24hr_volume(self):
        volume = self.__send_request(COMMAND_24VOLUME)
        return volume

    def get_orderbook(self, currency_pair='BTC_ETH', depth=10):
        command = '%s&currencyPair=%s&depth=%s' % (COMMAND_ORDERBOOK,currency_pair,str(depth))
        orderbook = self.__send_request(command)
        return orderbook

    def get_tradehistory(self, currency_pair='BTC_ETH', start=None, end=None):
        command = '%s&currencyPair=%s&start=%s&end=%s' % (COMMAND_TRADEHISTORY, currency_pair, str(start), str(end))
        tradehistory = self.__send_request(command)
        return tradehistory

    def get_chartdata(self, currency_pair='BTC_ETH', start=None, end=None, period=0):
        command = '%s&currencyPair=%s&start=%s&end=%s&period=%s' % (COMMAND_CHARTDATA, currency_pair, str(start), str(end), str(period))
        chartdata = self.__send_request(command)
        return chartdata

    def get_currencies(self):
        currencies = self.__send_request(COMMAND_CURRENCIES)
        return currencies

    def get_loanorders(self, currency):
        command = '%s&currency=%s' % (COMMAND_LOANORDERS, currency)
        loanorders = self.__send_request(command)
        return loanorders

    def __construct_url(self, command):
        return '%s?command=%s' % (self.baseUrl, command)

    def __send_request(self, command):
        url = self.__construct_url(command)
        print url
        response = requests.request("GET", url)
        result = json.loads(response.text)
        return result
