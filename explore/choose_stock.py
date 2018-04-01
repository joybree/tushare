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



def decreasing_thr_judge(thr_value=0.2, str_stock_code="000651"):
    df_one_stock_trade = ts.get_k_data(code=str_stock_code, start='2012-06-30')
    try:
        close_price_min = np.min(df_one_stock_trade['close'])
        close_proce_cur = df_one_stock_trade['close'].values[-1]
        print(df_one_stock_trade)
    except KeyError:
        return -1
    #print(close_proce_cur)
    #print(close_price_min)
    decrease_value = (close_proce_cur-close_price_min)/close_price_min
    return decrease_value



if __name__ == '__main__':
    df_all_stock_basics = ts.get_stock_basics()
    #print(df_all_stock_basics)
    df_all_stock_basics.to_csv(DATA_PATH+"stock_basics.csv",encoding='GBK')
    stock_code_all_Array1 = np.array([])
    stock_code_all_Array2 = np.array([])
    stock_code_all_DataFrame = pd.DataFrame([])
    print(df_all_stock_basics.index)
    Series_str_stock_code = df_all_stock_basics.index

    for str_stock_code in Series_str_stock_code.values:
        decrease_value = decreasing_thr_judge(thr_value=10000000, str_stock_code=str_stock_code)
        #print(str_stock_code)
        #print(decrease_value)
        stock_code_all_Array1=np.append(stock_code_all_Array1,str_stock_code)
        stock_code_all_Array2=np.append(stock_code_all_Array2,decrease_value)
        #print(stock_code_all_Array2)
            #stock_code_all_DataFrame.append(Series_str_stock_code.)
    print("***")
    print(stock_code_all_Array2)
    print(pd.Series(stock_code_all_Array2))
    #df_all_stock_basics['decrease_value'] = pd.Series(stock_code_all_Array2)
    df_all_stock_basics['decrease_value'] = stock_code_all_Array2
    df_all_stock_basics.to_csv(DATA_PATH+'decreasing_stock_info.csv',encoding='GBK')
    with open(DATA_PATH+'decreasing_stock_name.csv', 'wb') as file_handle:
        np.savetxt(file_handle, stock_code_all_Array1, delimiter=",",fmt='s%')
    
    