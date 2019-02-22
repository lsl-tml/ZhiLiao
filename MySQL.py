import csv

from pymysql import connect

dbs = 'penglai'  # 数据库
host="180.178.56.50" # 端口
user='admin'
password='admin'
# dbs = 'ips'  # 数据库
# host="localhost" # 端口
# user='root'
# password=''

class Mysqlcz:
    def __init__(self, database=dbs,
                 host=host,
                 user=user,
                 password=password,
                 charset='utf8mb4',
                 port=3306):
        # 创建链接
        self.conn = connect(database=database,  # 链接
                            host=host,
                            user=user,
                            password=password,
                            charset=charset,
                            port=port)
        self.cur = self.conn.cursor()  # 游标
# 关闭

    def close(self):
        self.cur.close()
        self.conn.close()
# 执行

    def workon(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            # print('数据库执行成功')
            # self.close()
            return True
        except Exception as e:
            self.conn.rollback()
            print('数据库执行失败++++++++++++++++++++++++++++++++++++++++++++++++++++++++', e)
            print(sql)
            self.close()

# 查询

    def getAll(self, sql):
        try:
            self.cur.execute(sql)
            # print('数据库查询执行成功')
            result = self.cur.fetchall()
            print('数据库查询成功')
            self.close()
            return result
        except Exception as e:
            self.conn.rollback()
            print('数据库查询失败++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++', e)
            print(sql)
            self.close()

