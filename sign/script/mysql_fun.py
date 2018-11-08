#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb


class PublicMysql(object):
    def __init__(self, ip, port, user, pwd, dataName):
        self.__ip = ip
        self.__port = port
        self.__user = user
        self.__passWd = pwd
        self.__dataBaseName = dataName

    def __connect(self):
        self.__db = MySQLdb.connect(host=self.__ip, port=self.__port, user=self.__user, passwd=self.__passWd,
                                  db=self.__dataBaseName,
                                  charset="utf8")

        self.__cursor = self.__db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def select(self, sql):

        self.__connect()
        self.__cursor.execute(sql)
        # 使用 fetchall() 方法获取所有查询结果
        data = self.__cursor.fetchall()
        # 关闭数据库连接
        self.__db.close()

        return data

    def update(self, sql):

        self.__execute(sql)

    def insert(self, sql):

        self.__execute(sql)

    def __execute(self, sql):

        self.__connect()

        try:
            # 执行SQL语句
            self.__cursor.execute(sql)
            # 提交到数据库执行
            self.__db.commit()
        except:
            # 发生错误时回滚
            self.__db.rollback()
            # 关闭数据库连接
            self.__db.close()