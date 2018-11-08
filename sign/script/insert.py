#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sign.script import mysql_fun
def insert_userinfo(username, password):
    s = mysql_fun.PublicMysql("127.0.0.1", 3306, "root", "123456", "test")
    sql = 'INSERT INTO user(name,PASSWORD) VALUE("{0}","{1}");'.format(username, password)

    s.insert(sql)
