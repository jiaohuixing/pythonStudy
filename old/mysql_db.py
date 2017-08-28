import pymysql

conn=pymysql.connect(user='root',passwd='1234',host='localhost',db='test',charset='utf8')
print('success')
cur = conn.cursor()
cur.execute('select * from s产品')
for r in cur:
    print('row_number:',(cur.rownumber))
    print("id:"+str(r[0])+"name:"+str(r[1]))
cur.close()
conn.close();
