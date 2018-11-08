#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sign.script import mysql_fun


def select_user(username, password):
    s = mysql_fun.PublicMysql("127.0.0.1", 3306, "root", "123456", "test")
    sql = 'select name,password from user where name="{0}";'.format(username)

    result = s.select(sql)

    if len(result) == 0:

        return False
    else:

        for i in result:

            if i["password"] == password:

                return True


            else:
                return False


def select_event():
    s = mysql_fun.PublicMysql("127.0.0.1", 3306, "root", "123456", "test")
    sql = 'select * from event ;'

    result = s.select(sql)

    return result