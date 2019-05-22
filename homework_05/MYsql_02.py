import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', passwd='123456',database = 'stu',charset = 'utf8')

while True:
    cur = db.cursor()
    name = input('name')
    age = input('age')
    gender = input('m or w')
    score = input('score:')
    money = input('money')

    sql = 'insert into myclass(name,age,gender,score,money)values(%s,%s,%s,%s,%s);'

    try:
        cur.execute(sql,[name,age,gender,score,money])
        db.commit()

    except Exception as e:
        db.rollback()
        print('Failed: ',e )

cur.close()
db.close()


