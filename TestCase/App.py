import unittest
from Core.Http import Http
from Core.DB import DB
from Common import Compare, Get


class Api(unittest.TestCase):
    def setUp(self):
        self.db = DB()
        cookie = Get.cookies()
        self.header = {'Cookie': cookie}

    def testAppNative(self):
        host = 'http://10.12.9.27'
        data = self.db.query_all("select * from api where project='app-native-http2.2'")
        for item in data:
            url = host + '/' + item['project'] + item['api_path']
            result = Http.get_json_response(url, eval(item['params']), self.header)
            record = dict()
            record['project'] = item['project']
            record['api_path'] = item['api_path']
            record['api_type'] = item['api_type']
            record['result'] = Compare.expect_to_actual(item['expect'], 'code:' + result['code'])
            self.db.insert(record, 'result')
            self.assertEqual(item['expect'], 'code:' + result['code'], item['api_path'])
