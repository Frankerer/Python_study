from pymysql import Connection
#引入链接功能

#获取MySql 数据库的链接对象
conn = Connection(
    host = "localhost",
    port= 3306,
    user="root",
    password="123456",
    #autocommit = True#设置数据更改自动确认
)
print(conn.get_server_info())

#建立游标对象来使用数据库
cursor = conn.cursor()

#选择需要操作的数据库
conn.select_db("test")

#使用游标对象来执行sql语句
# cursor.execute(
#     "create table teacher(id int,name varchar(255),wage float)"
# )

#进行数据更改
cursor.execute("insert into teacher value (1001,'guan',10086)")
    #通过commit确认数据更改
conn.commit()


cursor.execute(
    "select * from teacher"
)

#接收数据库的元组结果((1003, 'lu', 1236.11), (1004, 'zha', 236.12), (1001, 'ang', 123.12), (1002, 'zhan', 5646.16))
result = cursor.fetchall()
for line in result:
    print(line)

#关闭链接
conn.close()