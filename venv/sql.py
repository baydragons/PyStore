import mysql.connector
conn = mysql.connector.connect(user='root', password='870612', host='localhost', port='3306',
                               database='stock_basic', use_pure=True)
c = conn.cursor()
"""
c.execute('''create table user_tb(
            user_id int primary key auto_increment,
            name varchar(255),
            pass varchar(255),
            gender varchar(255))''')

c.execute('''create table order_tb(
            order_id int primary key auto_increment,
            item_name varchar(255),
            item_price double,
            item_number double,
            user_id int,
            foreign key(user_id) references user_tb(user_id))''')
"""
c.execute('''create table stock_basic(
            ts_code varchar(255) primary key,
            symbol  varchar(255),
            name  varchar(255),
            area  varchar(255),
            industry  varchar(255),
            fullname  varchar(255),
            enname  varchar(255),
            market  varchar(255),
            exchange  varchar(255),
            curr_type  varchar(255),
            list_status  varchar(255),
            list_date  varchar(255),
            delist_date  varchar(255),
            is_hs  varchar(255))''')


c.close()
conn.close()
