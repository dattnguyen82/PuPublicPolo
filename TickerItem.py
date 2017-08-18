
class TickerItem:
    name = None
    id = None
    last = None
    lowestAsk = None
    highestBid = None
    percentChange = None
    baseVolume = None
    quoteVolume = None
    isFrozen = None
    high24hr = None
    low24hr = None

    def __init__(self, name, id, last, lowest_ask, highest_bid, percent_change, base_volume, quote_volume, is_frozen, high_24_hr, low_24_hr):
        self.name = name
        self.id = id
        self.last = last
        self.lowestAsk = lowest_ask
        self.highestBid = highest_bid
        self.percentChange = percent_change
        self.baseVolume = base_volume
        self.quoteVolume = quote_volume
        self.isFrozen = is_frozen
        self.high24hr = high_24_hr
        self.low24hr = low_24_hr

    def to_json(self):
        json = '{'
        json+= '"name": "' + self.name + '",'
        json += '"last": ' + self.last + ','
        json += '"lowestAsk": ' + self.lowestAsk + ','
        json += '"highestBid": ' + self.highestBid + ','
        json += '"percentChange": ' + self.percentChange + ','
        json += '"baseVolume": ' + self.baseVolume + ','
        json += '"quoteVolume": ' + self.quoteVolume + ','
        json += '"isFrozen": ' + self.isFrozen + ','
        json += '"high24hr": ' + self.high24hr + ','
        json += '"low24hr": ' + self.low24hr
        json += '}'
        return json

