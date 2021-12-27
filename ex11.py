# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 10:53:38 2021

@author: Administrator
"""
import sqlite3

# 連線資料庫
db3 = sqlite3.connect('即時股價2.db')
db3_version = sqlite3.version
print ("使用sqlite連線的資料庫版本為 : %s " % db3_version)

cursor = db3.cursor()
#確認資料表是否存在
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#創建資料表
sql3 = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql3)
db3.close()
# import p即
# # 打开数据库连接
# db2 = pymysql.connect("localhost", "root", "tsmumc87", "csv_db2", charset='utf8' )


# # 連線資料庫
# # db2 = pymysql.connect(host = "127.0.0.1",
# #                       user = "root",
# #                       passwd = "12345678",
# #                       database = "testdb",
# #                       port = 3307)

# cursor = db2.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print ("使用pymysql連線的資料庫版本為 : %s " % data)
# #確認資料表是否存在
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE_B")
# #創建資料表
# sql2 = """CREATE TABLE EMPLOYEE_B (
#           FIRST_NAME  CHAR(20) NOT NULL,
#           LAST_NAME  CHAR(20),
#           AGE INT,  
#           SEX CHAR(1),
#           INCOME FLOAT )"""

# cursor.execute(sql2)
# db2.close()

# import MySQLdb

# # 打开数据库连接
# db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

# 使用cursor()方法获取操作游标 
# cursor = db1.cursor()

# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")

# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()

# print("Database version : %s " % data)

# # # 关闭数据库连接

# #創建資料表
# sql2 = """CREATE TABLE EMPLOYEE_B (
#           FIRST_NAME  CHAR(20) NOT NULL,
#           LAST_NAME  CHAR(20),
#           AGE INT,  
#           SEX CHAR(1),
#           INCOME FLOAT )"""

# cursor.execute(sql2)
# #確認資料表是否存在
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE_A")
# #創建資料表
# sql1 = """CREATE TABLE EMPLOYEE_A (
#           FIRST_NAME  CHAR(20) NOT NULL,
#           LAST_NAME  CHAR(20),
#           AGE INT,  
#           SEX CHAR(1),
#           INCOME FLOAT )"""

# cursor.execute(sql1)
# db1.close()
# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # Rollback in case there is any error
#    db.rollback()

# # 关闭数据库连接
# db.close()
