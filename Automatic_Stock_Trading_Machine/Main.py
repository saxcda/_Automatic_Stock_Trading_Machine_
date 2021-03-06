import requests
import urllib3

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
        #use 2330.TW 
        self.header = {"..."}
        self.url = "..."

        html = requests.get(self.url, verify=False, headers=self.header)
        html.encoding="utf-8"

        print(html.text)

if __name__ == '__main__':
    machine = Machine()
    print("finish")