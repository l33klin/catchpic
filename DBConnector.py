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
                                    db=constants.MYSQLDB)
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)

        print 'DB connector initial complete'

    def __del__(self):

        self.cursor.close()
        self.conn.close()

        print 'DB connector release'

    def getCursor(self):

        return self.cursor

    def insert(self, sql='', para=''):

        self.cursor.execute(sql, para)
        self.conn.commit()

        return True

    def insertPageInfo(self, title='', m_type='', level=0, favor=0):

        self.cursor.execute('use %s' % constants.MYSQLDB)
        sqlCmd = 'insert into %s values(100, %%s, %%s, %%s, %%s)' % constants.PAGETABLE
        print sqlCmd
        values = [title, m_type, level, favor]
        self.insert(sqlCmd, values)

        return True

def test():

    db = DBconnector()

    db.insertPageInfo('test title', 'ZS', 2, 1)

    return True

if __name__ == '__main__':
    test()