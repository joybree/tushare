# -*- coding:utf-8 -*- 

import sys
DATA_PATH = "f:\\mypython\\tushare"
sys.path.append(DATA_PATH)  

import pandas as pd
import tushare as ts 
import numpy as np

DATA_PATH = "F:/mypython/tushare/data/"

#df_one_stock_trade = ts.get_k_data("000651")

#df_one_stock_trade.to_csv(PATH+"000651_new.csv")


def avg_bargin_perday(str_stock_code_List):
    avg_bargin=[]
    for str_stock_code in str_stock_code_List:
        df_one_stock_trade = ts.get_k_data(code=str_stock_code, start='2018-02-28',end='2018-03-31')
        print(df_one_stock_trade)
        try:
            close_price_last = np.min(df_one_stock_trade['close'][df_one_stock_trade.date=='2018-02-28'])
            day_len = len(df_one_stock_trade['close'])-1
            print(day_len)
            print(df_one_stock_trade['close'].values[1:])
            #avg_bargin.append((np.sum(df_one_stock_trade['close'].values[1:])/day_len - close_price_last)/close_price_last)
            avg_bargin.append(((np.min(df_one_stock_trade['low'].values[1:])+np.max(df_one_stock_trade['high'].values[1:]))/2 - close_price_last)/close_price_last)
            print(avg_bargin)
        except KeyError:
            return -1
    combin_bargin = np.mean(avg_bargin)
    print(combin_bargin)
    #print(close_price_min)
        #decrease_value = (close_proce_cur-close_price_min)/close_price_min
        #return decrease_value

if __name__ == '__main__':
    code_List=['300666','600867','002410']
    code_List1=['002139','000938','000977']
    avg_bargin_perday(code_List)
    