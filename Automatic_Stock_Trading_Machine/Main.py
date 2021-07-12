import requests
import urllib3
import json
import numpy as np
import pandas as pd
import datetime

'''
Main machine
widget

'''

urllib3.disable_warnings()

class Machine():
    def __init__(self):
        self.header = {}
        self.url = ""

        self.initialize()
        
    
    def initialize(self):
        self.get_stock()

    def get_stock(self):
        #test 2330.TW 
        codaname = ""
        epoch_time_now = str(int(datetime.datetime.now().timestamp()))
        self.header = {"..."}
        self.url = "..."

        self.html = requests.get(self.url, verify=False, headers=self.header)
        #self.html.encoding="utf-8"
        #self.html.text[:1000]

        self.data = json.loads(self.html.text)
        
        self.tmp_list = self.data['chart']['result'][0]['indicators']['quote'][0]
        self.df = pd.DataFrame({'open'  : self.tmp_list['open'],
                                'close' : self.tmp_list['close'],
                                'low'   : self.tmp_list['low'],
                                'high'  : self.tmp_list['high'],
                                'volume': self.tmp_list['volume']},
                                index = (np.array([datetime.datetime.utcfromtimestamp(x) for x in self.data['chart']['result'][0]['timestamp']])))

        print(self.df)

if __name__ == '__main__':
    machine = Machine()
    print("finish")