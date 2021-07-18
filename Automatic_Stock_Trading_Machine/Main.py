import sys
import os

import requests
import urllib3
import json

import numpy as np
import pandas as pd

import datetime

from PyQt5.QtWidgets import QApplication
from Widget import MainWidget

# |====================================================|
# | SaXCDa                                             |
# | version = "0.0.0"                                  |
# |                                                    |
# |====================================================|
# | Main   : machine                                   |
# | widget : widget                                    |
# |                                                    |
# |====================================================|
# | Main :                                             |
# | add tset mode                                      |
# | code_name can be change                            |
# | Widget :                                           |
# | add new file Widget.py                             |
# |                                                    |
# |====================================================|
# | get datas include all validRanges                  |
# | get datas from all code_name                       |
# | crawler in the Main -> create new file 'Crawler.py'|
# | ...                                                |
# |                                                    |
# |====================================================|


class Machine():
    def __init__(self):
        self.isTestMode = True

        self.widget = MainWidget()
        self.view = self.widget.ViewTab

        self.plot = self.view.plot_1

        self.plotGroup = self.widget.PlotGroup

        '''remember to add user-agent 😂'''
        self.user_agent = ""
        self.url = ""

        self.open = []
        self.close = []
        self.low = []
        self.high = []
        self.volume = []

        self.initialize()

        self.assignEvents()

        self.testMode(self.isTestMode)
    
    def initialize(self):
        self.get_stock()
        self.sort_out()
        self.draw_plot()

    def assignEvents(self):
        self.plotGroup.plotButton_1.clicked.connect(self.Open_plot)
        self.plotGroup.plotButton_2.clicked.connect(self.Close_plot)
        self.plotGroup.plotButton_3.clicked.connect(self.Low_plot)
        self.plotGroup.plotButton_4.clicked.connect(self.High_plot)
        self.plotGroup.plotButton_5.clicked.connect(self.Volume_plot)

    def get_stock(self):
        self.code_name = ""
        self.time_now = datetime.datetime.now()
        self.epoch_time_now = str(int(self.time_now.timestamp()))
        
        urllib3.disable_warnings()

        self.url = ""
        self.header = {"User-agent" : self.user_agent}
        self.html = requests.get(self.url, verify=False, headers=self.header)
        #self.html.encoding="utf-8"
        #self.html.text[:1000]

        self.data = json.loads(self.html.text)
        
        self.tmp_list = self.data['chart']['result'][0]['indicators']['quote'][0]
        self.epoch_list = (np.array([datetime.datetime.utcfromtimestamp(x) for x in self.data['chart']['result'][0]['timestamp']]))
        self.df = pd.DataFrame({'open'  : self.tmp_list['open'],
                                'close' : self.tmp_list['close'],
                                'low'   : self.tmp_list['low'],
                                'high'  : self.tmp_list['high'],
                                'volume': self.tmp_list['volume']},
                                index = self.epoch_list)

    def testMode(self, isTest):
        if isTest:
            print(self.code_name)
            print(self.user_agent)
            print(self.time_now, ",", self.epoch_time_now, end='\n\n')
            print(self.df)

    def sort_out(self):
        self.open   = self.df['open']
        self.close  = self.df['close']
        self.low    = self.df['low']
        self.high   = self.df['high']
        self.volume = self.df['volume']
        
    def Open_plot(self):
        cnt_list = list(range(1, len(self.open)+1))
        self.plot.ax.cla()
        self.plot.ax.plot(cnt_list, self.open, 'r')
        self.plot.ax.set_title(self.code_name)
        self.plot.ax.set_ylabel('price')

        self.plot.canvas.draw()

    def Close_plot(self):
        cnt_list = list(range(1, len(self.close)+1))
        self.plot.ax.cla()
        self.plot.ax.plot(cnt_list, self.close, 'r')
        self.plot.ax.set_title(self.code_name)
        self.plot.ax.set_ylabel('price')

        self.plot.canvas.draw()
    
    def Low_plot(self):
        cnt_list = list(range(1, len(self.low)+1))
        self.plot.ax.cla()
        self.plot.ax.plot(cnt_list, self.low, 'r')
        self.plot.ax.set_title(self.code_name)
        self.plot.ax.set_ylabel('price')

        self.plot.canvas.draw()

    def High_plot(self):
        cnt_list = list(range(1, len(self.high)+1))
        self.plot.ax.cla()
        self.plot.ax.plot(cnt_list, self.high, 'r')
        self.plot.ax.set_title(self.code_name)
        self.plot.ax.set_ylabel('price')

        self.plot.canvas.draw()

    def Volume_plot(self):
        cnt_list = list(range(1, len(self.volume)+1))
        self.plot.ax.cla()
        self.plot.ax.plot(cnt_list, self.volume, 'r')
        self.plot.ax.set_title(self.code_name)
        self.plot.ax.set_ylabel('price')

        self.plot.canvas.draw()

    def draw_plot(self):
        self.Open_plot()
        self.Close_plot()
        self.Low_plot()
        self.High_plot()
        self.Volume_plot()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    machine = Machine()
    machine.widget.show()
    
    print("Wait for window to open...")
    os._exit(app.exec_())