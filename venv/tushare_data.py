# coding=utf-8

import time
import pandas as pd


def get_stock_basic(pro, retry_count=3, pause=2):
    """股票列表 数据"""
    frame = pd.DataFrame()
    for status in ['L', 'D', 'P']:
        for _ in range(retry_count):
            try:
                df = pro.stock_basic(exchange='', list_status=status,
                                     fields='ts_code,symbol,name,area,industry,fullname,enname,market, \
                                    exchange,curr_type,list_status,list_date,delist_date,is_hs')
            except:
                time.sleep(pause)
            else:
                frame = frame.append(df)
                break

    return frame


def get_daily_code(pro, ts_code, start_date, end_date, retry_count=3, pause=2):
    """股票代码方式获取 日线行情 数据"""
    for _ in range(retry_count):
        try:
            df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date,
                           fields='ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount')
        except:
            time.sleep(pause)
        else:
            return df


def get_daily_date(pro, date, retry_count=3, pause=2):
    """日期方式获取 日线行情 数据"""
    for _ in range(retry_count):
        try:
            df = pro.daily(trade_date=date,
                           fields='ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount')
        except:
            time.sleep(pause)
        else:
            return df

