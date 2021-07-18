'''
{"chart":
    {"result":
        [{"meta":
            {"currency":null,
             "symbol":"APPL",
             "exchangeName":"YHD",
             "instrumentType":"MUTUALFUND",
             "firstTradeDate":null,
             "regularMarketTime":1561759658,
             "gmtoffset":-14400,
             "timezone":"EDT",
             "exchangeTimezoneName":"America/New_York",
             "priceHint":2,
             "currentTradingPeriod":
                {"pre":{"timezone":"EDT","start":1625817600,"end":1625837400,"gmtoffset":-14400},
                 "regular":{"timezone":"EDT","start":1625837400,"end":1625860800,"gmtoffset":-14400},
                 "post":{"timezone":"EDT","start":1625860800,"end":1625875200,"gmtoffset":-14400}
                },
             "dataGranularity":"1d",
             "range":"",
             "validRanges":["1mo","3mo","6mo","ytd","1y","2y","5y","10y","max"]

            },
            "indicators":{"quote":[{}],"adjclose":[{}]}}

        ],
        "error":null

    }
}

{'chart': 
    {'result': 
        [{'meta': 
            {'currency': 'TWD', 
            'symbol': '2330.TW', 
            'exchangeName': 'TAI', 
            'instrumentType': 'EQUITY', 
            'firstTradeDate': 946947600, 
            'regularMarketTime': 1625808608, 
            'gmtoffset': 28800, 
            'timezone': 'CST', 
            'exchangeTimezoneName': 'Asia/Taipei', 
            'regularMarketPrice': 584.0, 
            'chartPreviousClose': 69.649, 
            'priceHint': 2, 
            'currentTradingPeriod': 
                {'pre': {'timezone': 'CST', 'start': 1626051600, 'end': 1626051600, 'gmtoffset': 28800}, 
                'regular': {'timezone': 'CST', 'start': 1626051600, 'end': 1626067800, 'gmtoffset': 28800}, 
                'post': {'timezone': 'CST', 'start': 1626067800, 'end': 1626067800, 'gmtoffset': 28800}
                }, 
            'dataGranularity': '1d', 
            'range': '', 
            'validRanges': ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']}, 
            'timestamp': [], 
            'indicators': {'quote': [{'open': [], 'high': [], 'low': [], 'close': [], 'volume': []}], 
            'adjclose': [{'adjclose': []}]}}], 
            'error': None
            
    }
            
}

index=(np.array(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((self.data['chart']['result'][0]['timestamp']))))))

'''
'''
{"chart":
    {"result":
        [{"meta":
            {"currency":"TWD",
            "symbol":"2330.TW",
            "exchangeName":"TAI",
            "instrumentType":"EQUITY",
            "firstTradeDate":946947600,
            "regularMarketTime":1626146357,
            "gmtoffset":28800,
            "timezone":"CST",
            "exchangeTimezoneName":"Asia/Taipei",
            "regularMarketPrice":607.0,
            "chartPreviousClose":592.0,
            "previousClose":593.0,
            "scale":3,
            "priceHint":2,
            "currentTradingPeriod":
                {"pre":{"timezone":"CST","end":1626138000,"start":1626138000,"gmtoffset":28800},
                "regular":{"timezone":"CST","end":1626154200,"start":1626138000,"gmtoffset":28800},
                "post":{"timezone":"CST","end":1626154200,"start":1626154200,"gmtoffset":28800}},
            "tradingPeriods":[[{"timezone":"CST","end":1625549400,"start":1625533200,"gmtoffset":28800}],
                            [{"timezone":"CST","end":1625635800,"start":1625619600,"gmtoffset":28800}],
                            [{"timezone":"CST","end":1625722200,"start":1625706000,"gmtoffset":28800}],
                            [{"timezone":"CST","end":1625808600,"start":1625792400,"gmtoffset":28800}],
                            [{"timezone":"CST","end":1626067800,"start":1626051600,"gmtoffset":28800}],
                            [{"timezone":"CST","end":1626154200,"start":1626138000,"gmtoffset":28800}]],
            "dataGranularity":"1m","range":"","validRanges":["1d","5d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"]},
            "timestamp":

'''