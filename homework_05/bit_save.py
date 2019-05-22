import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', passwd='123456',database = 'stu',charset = 'utf8')

cur = db.cursor()

# with open('luoli.jpg','rb') as fd:
#     data = fd.read()
#
# try:
#     sql = 'insert into Images values(1,"luoli.jpg",%s) '
#     cur.execute(sql,[data])
#     db.commit()
#
# except Exception as a:
#     db.rollback()
#     print('failed',a)
#
#
#
# cur.close()
# db.close()


sql = "select * from Images where filename = 'luoli.jpg';"

cur.execute(sql)
image = cur.fetchone()
with open(image[1],'wb')as fd:
    fd.write(image[2])

cur.close()
db.close()
