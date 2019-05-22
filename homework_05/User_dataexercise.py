import pymysql



class Create:
    def __init__(self,db = None,count=None,host='localhost',user = 'root', passwd='123456',database = 'stu',charset = 'utf8'):
        self.db = db
        self.count = count
        self.host = host
        self.user = user
        self. password = passwd
        self.database = database
        self.charset = charset


    def createdb(self):
        self.db = pymysql.connect(host = self.host, user = self.user, passwd=self.password, database=self.database, charset=self.charset)


    def getinfo(self):
        self.cur = self.db.cursor()
        self.cur2 = self.db.cursor()
        self.username = input('name: ')
        self.password = input('password: ')
        self.sql_1 = 'insert into user (username,password) values (%s,%s);'


    def create_acount(self,count):
        sql = 'select username from user;'

        self.cur.execute(sql)
        print(count)
        for i in range(count):

            try:
                self.one_row = self.cur.fetchone()[0]
                print(self.one_row)
                if self.username == self.one_row:
                    print('already exist')
                    return False
            except Exception as a:
                print('hi')
                continue
        self.cur2.execute(self.sql_1, [self.username, self.password])

        count += 1
        print('created')

    def do_execute(self,count):
        self.createdb()

        self.getinfo()


        # try:
        self.create_acount(count)

        self.db.commit()
        self.cur.close()
        self.db.close()

        # except Exception as e:
        #     self.db.rollback()
        #     print('Failed: ', e)


class Login:
    def __init__(self,db = None,count=None,host='localhost',user = 'root', passwd='123456',database = 'stu',charset = 'utf8'):
        self.db = db
        self.count = count
        self.host = host
        self.user = user
        self. password = passwd
        self.database = database
        self.charset = charset

    def createdb(self):
        self.db = pymysql.connect(host=self.host, user=self.user, passwd=self.password, database=self.database,
                                  charset=self.charset)
        self.count = 1

    def do_execute(self):
        self.createdb()

        self.cur = self.db.cursor()

        self.enterName = input('username: ')
        self.Enterps = input('password: ')
        sql = 'select password from user where username = %s;'
        try:
            self.cur.execute(sql,[self.enterName])
            self.The_password = self.cur.fetchone()[0]
            if self.The_password == self.Enterps:
                print('成功')
            else:
                print('失败')
        except Exception as a:

            print('user does not exist')
            return False




def main():
    print('登录输入＂l＂,注册输入＂c＂\n======================')
    count =1


    while True:

        request = input('c or l:')
        if request == 'c':

            create_acount = Create()
            create_acount.do_execute(count)
            count += 1
        elif request == 'l':
            login = Login()
            login.do_execute()
        else:
            break




if __name__ =='__main__':
    main()


