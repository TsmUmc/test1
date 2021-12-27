# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:12:04 2021

@author: Administrator
"""

from datetime import datetime
import backtrader as bt
from dateutil.relativedelta import relativedelta
import yfinance as yf
  
class TestStrategy(bt.Strategy):
    def __init__(self):
        self._next_buy_date = datetime(2010, 1, 5)
  
    def next(self):
        if self.data.datetime.date() >= self. _next_buy_date.date():
            self. _next_buy_date += relativedelta(months=1)
            self.buy(size=1)
  
cerebro = bt.Cerebro()
data = bt.feeds.PandasData(dataname=yf.download('2603.TW', '2019-01-01', '2021-12-15', auto_adjust=True))
  
cerebro.adddata(data) 
cerebro.addstrategy(TestStrategy)
cerebro.broker.set_cash(cash=10000)
cerebro.run()
cerebro.plot() 