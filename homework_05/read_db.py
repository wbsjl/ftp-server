import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', passwd='123456',database = 'stu',charset = 'utf8')

cur = db.cursor()
sql = 'select id from myclass where age = 13;'

cur.execute(sql)

# one_row = cur.fetchone()
# print(one_row)
#
# many_row = cur.fetchmany(2)
#
# print(many_row)

all_row = cur.fetchall()

print(all_row)



cur.close()
db.close()

