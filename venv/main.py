# coding=utf-8

import pandas as pd
import tushare as ts
import mysql.connector
from sqlalchemy import create_engine

from mysql_tables_structure import Base
import mysql_functions as mf

# 创建数据库引擎
engine = create_engine('mysql+mysqlconnector://root:870612@localhost:3306/stock_basic')
conn = engine.connect()

# 创建mysql所有表结构
Base.metadata.create_all(engine)

# 连接 tushare
ts.set_token("a7d90bad9a45ab33810054e47c476fe981e4f2169af3d61fdf6317d2")
pro = ts.pro_api()

# 股票列表
mf.update_stock_basic(engine, pro, 3, 2)


# 根据需要增删 日线行情 数据  单次提取*4000*条
mf.delete_daily(engine, '19901219', '20191231')
codes = mf.get_ts_code(engine)
mf.update_all_daily(engine, pro, codes, '19901219', '20001231', 3, 2)
mf.update_daily_date(engine, pro, '20190702', 3, 2)





