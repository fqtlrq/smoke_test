import unittest
from Core.DB import DB
from Common import Get


class UserCenter(unittest.TestCase):
    def setUp(self):
        self.host = 'http://10.12.9.12:8083'
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.db = DB()

    def saveUserInfo(self):
        item = self.db.query_one("select * from api where id=20")
        post_data = eval(item['params'])
        post_data['loginName'] = Get.random_value(11)
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def checkPhone(self):
        item = self.db.query_one("select * from api where id=21")
        post_data = eval(item['params'])
        post_data['phone'] = Get.random_value(20)
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def checkLogin(self):
        item = self.db.query_one("select * from api where id=22")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def queryRealAuthInfo(self):
        item = self.db.query_one("select * from api where id=23")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def checkCertVaild(self):
        item = self.db.query_one("select * from api where id=24")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def getVocationList(self):
        item = self.db.query_one("select * from api where id=25")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def getCK(self):
        item = self.db.query_one("select * from api where id=26")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def queryUserInfoByLogin(self):
        item = self.db.query_one("select * from api where id=27")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def editUserInfo(self):
        item = self.db.query_one("select * from api where id=28")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def updatePhone(self):
        item = self.db.query_one("select * from api where id=29")
        post_data = eval(item['params'])
        post_data['phone'] = Get.random_value(11)
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def updateHeadPic(self):
        item = self.db.query_one("select * from api where id=30")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def updateSignature(self):
        item = self.db.query_one("select * from api where id=31")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def updateEmail(self):
        item = self.db.query_one("select * from api where id=32")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def queryUserInfo(self):
        item = self.db.query_one("select * from api where id=33")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def getQuestions(self):
        item = self.db.query_one("select * from api where id=34")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def queryQuestionById(self):
        item = self.db.query_one("select * from api where id=35")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def setPhone(self):
        item = self.db.query_one("select * from api where id=36")
        post_data = eval(item['params'])
        post_data['phone'] = Get.random_value(11)
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def setEmail(self):
        item = self.db.query_one("select * from api where id=37")
        post_data = eval(item['params'])
        post_data['email'] = Get.random_value(11) + '@ehomepay.com.cn'
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def queryCancelUserList(self):
        item = self.db.query_one("select * from api where id=38")
        post_data = eval(item['params'])
        post_data['email'] = Get.random_value(11) + '@ehomepay.com.cn'
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])

    def queryEmailOrPhoneExist(self):
        item = self.db.query_one("select * from api where id=39")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])
