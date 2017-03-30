import pymysql
import os
from configparser import ConfigParser


class DB:
    def __init__(self):
        db_conf_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Conf', 'DB.ini')
        cf = ConfigParser()
        cf.read(db_conf_path, 'utf-8')
        server = cf.get('mysql', 'server')
        db = cf.get('mysql', 'db')
        user = cf.get('mysql', 'user')
        password = cf.get('mysql', 'password')
        self.conn = pymysql.connect(host=server, port=3306, user=user, passwd=password, database=db, charset='UTF8')
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def query_all(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def query_one(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def insert(self, data, table):
        column = ''
        value = ''
        for k, v in data.items():
            column += k + ','
            value += '\'' + v.replace('\'', '\'\'') + '\','
        column = column.rstrip(',')
        value = value.rstrip(',')

        sql = 'insert into ' + table + ' (' + column + ') values (' + value + ')'
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur.lastrowid
