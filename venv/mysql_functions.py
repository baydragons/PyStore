# coding=utf-8

import pandas as pd
import tushare_data as td
import time


def truncate_update(engine, data, table_name):
    """删除mysql表所有数据，to_sql追加新数据"""
    conn = engine.connect()
    conn.execute('truncate ' + table_name)
    data.to_sql(table_name, engine, if_exists='append', index=False)


def update_stock_basic(engine, pro, retry_count, pause):
    """更新 股票信息 所有数据"""
    data = td.get_stock_basic(pro, retry_count, pause)
    truncate_update(engine, data, 'stock_basic')


def get_ts_code(engine):
    """查询ts_code"""
    return pd.read_sql('select ts_code from stock_basic', engine)


def delete_daily(engine, start_date, end_date):
    """删除 日线行情 数据"""
    conn = engine.connect()
    conn.execute('delete from daily where  trade_date between ' + start_date + ' and ' + end_date)


def update_all_daily(engine, pro, codes, start_date, end_date, retry_count, pause):
    """股票代码方式更新 日线行情"""
    for value in codes['ts_code']:
        df = td.get_daily_code(pro, value, start_date, end_date, retry_count, pause)
        df.to_sql('daily', engine, if_exists='append', index=False)
        time.sleep(0.6)


def update_daily_date(engine, pro, date, retry_count, pause):
    """日期方式更新 日线行情"""
    df = td.get_daily_date(pro, date, retry_count, pause)
    df.to_sql('daily', engine, if_exists='append', index=False)
