import unittest
import time
from Core.Http import Http
from Core.DB import DB
from Common import Compare, Get


class EHomePayPassport(unittest.TestCase):
    def setUp(self):
        self.db = DB()
        self.host = 'http://10.12.9.27'
        self.header = {}

    def testLogin(self):
        data = self.db.query_one("select * from smoke where api_path='/app/testlogin'")
        result = Http.get_json_response(self.host + '/' + data['project'] + data['api_path'], eval(data['params']),
                                        self.header)
        record = dict()
        record['project']=data['project']
        record['api_path'] = data['api_path']
        record['api_type'] = data['api_type']
        record['result'] = Compare.expect_to_actual(data['expect'], 'code:' + result['code'])
        self.db.insert(record, 'result')
        self.assertEqual(data['expect'], 'code:' + result['code'], data['api_path'])
