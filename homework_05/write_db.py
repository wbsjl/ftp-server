import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', passwd='123456',database = 'stu',charset = 'utf8')
cur = db.cursor()

try:
    sql = 'insert into class_1 values(6,"Bob","rap,sing","A","8888","凑合吧");'
    cur.execute(sql)

    sql = "update class_1 set price = 6666 where name = 'biu';"
    cur .execute(sql)

    sql = "delete from myclass where score < 88;"
    cur.execute(sql)

    db.commit()
except Exception as a:
    db.rollback()
    print(a)

cur.close()
db.close()