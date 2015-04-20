__author__ = 'klin'
# -*- coding: utf-8 -*-

import MySQLdb
import constants


#
#
#
class DBconnector:

    conn = ''
    cursor = ''

    def __init__(self):

        self.conn = MySQLdb.connect(host=constants.MYSQLHOST, user=constants.MYSQLUSER, passwd=constants.MYSQLPASS,
                                    db=constants.MYSQLDB, charset=constants.MYSQLCHARSET)
        self.cursor = self.conn.cursor

        print 'DB connector initial complete'

    def __del__(self):

        self.cursor.close()
        self.conn.close()

        print 'DB connector release'

    def getCursor(self):

        return self.cursor

    def insert(self, sql='', para=''):

        self.cursor.execute(sql, para)

        return True
