# -*- coding: utf-8 -*-

import pymysql
class SQLConn():
    host = None
    port = None
    user = None
    password = None
    database = None
    charset = 'utf8'
    sql_conn = None
    cursorclass = None
    timeout=None
    login_timeout=None
    local_infile=None
    def conn_to_mysql(self):
        self.database = None
        self.cursorclass = None
        self.timeout = 10
        self.local_infile = None
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'root'
        self.database = "process_arrange"
        self.cursorclass = pymysql.cursors.Cursor

        self.sql_conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset,
            cursorclass=self.cursorclass,
            connect_timeout=self.timeout,
            local_infile=self.local_infile,
        )
        return self.sql_conn


    def executeSQL(self, sql, data=None, batchflag=0):
        cursor = self.sql_conn.cursor()
        if batchflag == 0:
            cursor.execute(sql, data)
        elif batchflag == 1:
            cursor.executemany(sql, data)
        cursor.execute('commit;')
        cursor.close()

    def executeQuery(self, sql):
        cursor = self.sql_conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    
    def close(self):
        self.sql_conn.close()
