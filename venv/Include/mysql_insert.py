import mysql.connector
conn = mysql.connector.connect(user='root', password='870612', host='localhost', port='3306',
                               database='python', use_pure=True)
c = conn.cursor()
"""
c.executemany('insert into user_tb values (null,%s,%s,%s)',
              (('sun', '123456', 'male'),
               ('bai', '123456', 'female'),
               ('zhu', '123456', 'male'),
               ('niu', '123456', 'male'),
               ('tang', '123456', 'male')))
"""
c.execute('select * from user_tb where user_id > %s ', (2, ))
for col in c.description:
    print(col[0], end='\t')
print('\n--------------------')
for row in c:
    print(row)
    print(row[1]+'-->'+row[2])
c.close()
conn.close()

