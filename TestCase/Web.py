import unittest

from Common import Get
from Core.DB import DB


class UserCenter(unittest.TestCase):
    def setUp(self):
        self.host = 'http://10.12.9.12:8083'
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.db = DB()

    def test_saveUserInfo(self):
        self.run_test(20, 'phone')

    def test_checkPhone(self):
        self.run_test(21, 'phone')

    def test_checkLogin(self):
        self.run_test(22)

    def test_queryRealAuthInfo(self):
        self.run_test(23)

    def test_checkCertVaild(self):
        self.run_test(24)

    def test_getVocationList(self):
        self.run_test(25)

    def test_getCK(self):
        self.run_test(26)

    def test_queryUserInfoByLogin(self):
        self.run_test(27)

    def test_editUserInfo(self):
        self.run_test(28)

    def test_updatePhone(self):
        self.run_test(29, 'phone')

    def test_updateHeadPic(self):
        self.run_test(30)

    def test_updateSignature(self):
        self.run_test(31)

    def test_updateEmail(self):
        self.run_test(32)

    def test_queryUserInfo(self):
        self.run_test(33)

    def test_getQuestions(self):
        self.run_test(34)

    def test_queryQuestionById(self):
        self.run_test(35)

    def test_setPhone(self):
        self.run_test(36, 'phone')

    def test_setEmail(self):
        self.run_test(37, 'email')

    def test_queryCancelUserList(self):
        self.run_test(38, 'email')

    def test_queryEmailOrPhoneExist(self):
        self.run_test(39)

    def run_test(self, case_id, random_type=''):
        item = self.db.query_one("select * from api where id=" + case_id)
        post_data = eval(item['params'])

        if random_type == '':
            pass
        elif random_type == 'email':
            post_data['email'] = Get.random_value(11) + '@ehomepay.com.cn'
        elif random_type == 'phone':
            post_data['phone'] = Get.random_value(11)

        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])
