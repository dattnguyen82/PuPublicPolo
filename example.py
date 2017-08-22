from py_public_polo import PyPublicPoloClient

client = PyPublicPoloClient()

##########################################################################################################
### Return ticker
##########################################################################################################
ticker_list = client.get_ticker()
for t in ticker_list:
    print t.to_json()
    

##########################################################################################################
#  Return ticker
#    Sort - available sort keys:
#        name
#        id
#        last
#        lowestAsk
#        highestBid
#        percentChange
#        baseVolume
#        quoteVolume
#        isFrozen
#        high24hr
#        low24hr
##########################################################################################################
ticker_list = client.get_ticker(sort_key='percentChange', reverse=True)
for t in ticker_list:
    print t.to_json()


##########################################################################################################
### Return 24 Hr volume
##########################################################################################################
volume_dict = client.get_24hr_volume()
for k in volume_dict.keys():
    print volume_dict[k]


##########################################################################################################
### Return Orderbook for a currency pair
### currency_pair - Currency Pair in the form X_Y e.g. BTC_BURST
### depth - integer
##########################################################################################################
orderbook_dict = client.get_orderbook(currency_pair='BTC_BURST', depth=20)
print orderbook_dict


##########################################################################################################
### Return last 200 trades for a currency pair within timeframe
### currency_pair - Currency Pair in the form X_Y e.g. BTC_BURST
### start - Unix Timestamp
### end - Unix Timestamp
##########################################################################################################
tradehistory_dict = client.get_tradehistory(currency_pair='BTC_NXT', start=1410158341, end=1410499372)
print tradehistory_dict


##########################################################################################################
### Return candlestick chart data
### currency_pair - Currency Pair in the form X_Y e.g. BTC_BURST
### start - Unix Timestamp
### end - Unix Timestamp
### period in seconds; valid values are 300, 900, 1800, 7200, 14400, and 86400
##########################################################################################################
chartdata_dict = client.get_chartdata(currency_pair='BTC_XMR', start=1405699200, end=1410158341, period=14400)
print chartdata_dict

##########################################################################################################
### Return currencies info
##########################################################################################################
currencies_dict = client.get_currencies()
print currencies_dict

##########################################################################################################
### Return list of loan offers
### currency - Currency abbreviation e.g. BTC
##########################################################################################################
loanorders_dict = client.get_loanorders(currency='ETH')
print loanorders_dict