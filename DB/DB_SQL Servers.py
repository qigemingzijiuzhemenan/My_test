import pymssql

class Mssql:
    #数据库基本信息
    def __init__(self):
        self.ip = ""
        self.user = ""
        self.password = ""
        self.database = ""
    # 创建连接对象
    def __connect_databases(self):
        try:
            self.conn = pymssql.connect(self.ip,self.user,self.password,self.database)#创建连接
            cursor = self.conn.cursor() #创建游标
            return cursor
        except pymssql.Error as Error:
            print("数据库连接失败：%s"%(Error))
    #查询操作
    def get_data(self,sql):
        try:
            cur = self.__connect_databases()
            cur.execute(sql)             #在游标上执行SQL语句
            name = cur.description
            values = cur.fetchall()          #返回所有数据
            # values = cur.fetchone()          #返回第一条数据
            # values = cur.fetchmany(2)        #返回前两条数据
            data = []
            num = 0
            while num < len(values):
                # print(values[num])
                # d = []
                num_1 = 0
                c = {}
                while num_1 < len(name):
                    c[name[num_1][0]] = values[num][num_1]
                    num_1 += 1
                data.append(c)
                # print(d)
                num += 1
            return data
        except pymssql.Error as Error:
            print("查询出错：%s"%(Error))
        finally:                          #无论怎样都会执行下面的关闭连接数据库的代码
            self.conn.close()
    #插入操作
    def set_data(self,sql,data=None):
        try:
            #单条插入方式
            cur = self.__connect_databases()
            cur.execute(sql)  # 在游标上执行SQL语句
            #多条插入方式
            # cur = self.__connect_databases()
            # cur.executemany(query,data)  # 在游标上执行SQL语句，需要多传一个参数data存放插入的数据

            # 数据库的存储一类引擎为Innodb，执行完成后需执行commit进行事务提交
            # 如果存储引擎为MyISAM，不用执行commit
            # 执行execute时就已经执行事务提交
            self.conn.commit()
        except pymssql.Error as Error:
            print("插入出错：%s"%(Error))
        finally:                          #无论怎样都会执行下面的关闭连接数据库的代码
            self.conn.close()
    #修改操作
    def update_data(self):
        pass
    #删除操作
    def delete_data(self):
        pass


# 测试此模块

# db = Mssql()
# adc = "ActivityTypeId"
# table ="[activity].[Activity]"
# data = db.get_data("select * from %s"%(table))

