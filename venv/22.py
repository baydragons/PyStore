import pymysql
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts
from datetime import  datetime
from datetime import timedelta
import time
from sqlalchemy import create_engine
"""
data=[
    ("零基础学Python",'python','79.8','2018-5-20'),
    ("Pychon从入门到精通",'python','69.8','2018-6-18')
]
try:
    cursor.executemany("insert into books(name,category,price,publish_time) values(%s,%s,%s,%s)",data)
    db.commit()
except:
    db.rollback()
"""
def fetchklinedata(code):
    ts.set_token('a7d90bad9a45ab33810054e47c476fe981e4f2169af3d61fdf6317d2')
    # api=ts.pro_api()
    # stocklist=api.stock_basic()['ts_code']
    engine = create_engine('mysql+pymysql://root:870612@localhost:3306/test',encoding="utf-8")
    db = pymysql.connect('localhost', 'root', '870612', 'test')
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS day_data")
    sql = "CREATE TABLE day_data(ts_code varchar(20) NOT NULL,trade_date date NOT NULL,open float NOT NULL,high float NOT NULL,low float NOT NULL,close float NOT NULL,pre_close float NOT NULL,`changed` float NOT NULL,pct_chg float NOT NULL,vol float NOT NULL,amount float NOT NULL)ENGINE=MyISAM;"
    cursor.execute(sql)
    end_date = datetime.strftime(datetime.now(), '%Y%m%d')#获取当前时间
    outputflag = True
    while outputflag:#循环判断，直到返还的数据为空
        data=ts.pro_bar(ts_code=code,end_date=end_date,asset='E',adj=None,freq='D')#请求本次数据
        subset = data[['ts_code','trade_date','open','high','low','close','pre_close','change','pct_chg','vol','amount']]
        tuples = [tuple(x) for x in subset.values]
        #train_data = np.array(data)  # np.ndarray()
        #train_list = train_data.tolist()  # list

        if data.empty == True:
            outputflag = False
        else:
            #计算下次请求数据的截止日期
            next_end_date = datetime.strptime(data.iloc[-1]['trade_date'],'%Y%m%d') - timedelta(hours=24)
            end_date = datetime.strftime(next_end_date, '%Y%m%d')

            #写入sql文件
            #try:
                #print(tuples)
            print(data)
            data.to_sql(name='day', con=engine, index=False, if_exists='append',chunksize=100)
            #print('插入成功')
            #cursor.executemany("insert into day_data(ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",tuples)

            db.commit()

            #except:
             #   db.rollback()

            time.sleep(1)
    db.close()


fetchklinedata('000009.SZ')