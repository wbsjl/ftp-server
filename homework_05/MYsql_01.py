import pymysql
db =pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',database='stu',charset='utf8')

cur = db.cursor()
cur.execute("insert into stu.myclass values (6,'Money',13,'w',89,120);")

db.commit()

cur.close()
db.close()