import unittest

from Common import Get
from Core.DB import DB


class UserCenter(unittest.TestCase):
    def setUp(self):
        self.host = 'http://10.12.9.12:8083'
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.db = DB()

    def test_saveUserInfo(self):
        self.run_test(20, True)

    def test_checkPhone(self):
        self.run_test(21, True)

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

    def test_queryUserInfoByName(self):
        self.run_test(49)

    def test_editUserInfo(self):
        self.run_test(28)

    def test_updatePhone(self):
        self.run_test(29, True)

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
        self.run_test(36, True)

    def test_setEmail(self):
        self.run_test(37, True)

    def test_queryCancelUserList(self):
        self.run_test(38, True)

    def test_queryEmailOrPhoneExist(self):
        self.run_test(39, True)

    def test_countRealAuthNum(self):
        self.run_test(40)

    def test_countRegisterNum(self):
        self.run_test(41)

    def test_saveRealAuthInfoFirst(self):
        self.run_test(42)

    def test_saveRealAuthInfoSecond(self):
        self.run_test(43)

    def test_queryCertsApprovalList(self):
        self.run_test(44)

    def test_queryAuthApprovalList(self):
        self.run_test(45)

    def test_approveAuthAndUpdateCertInfo(self):
        '''
        1.查询证件审核下的待审核approveId
        2.进行驳回操作
        3.更新证件信息使其重新变为待审核状态
        :return: 
        '''
        item = self.db.query_one("select * from api where id=44")
        post_data = eval(item['params'])
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        approve_id = result['data']['data'][0]['approvalId']
        self.run_test(46, others={'approveId': approve_id})
        self.run_test(47)

    def test_setsecQuestions(self):
        self.run_test(50)

    def test_checkQuestions(self):
        self.run_test(51)

    def test_queryAuthApprovalDetail(self):
        self.run_test(52)

    def run_test(self, case_id, random=False, **others):
        item = self.db.query_one("select * from api where id=" + str(case_id))
        post_data = eval(item['params'])
        if random is True:
            if 'email' in post_data:
                post_data['email'] = Get.random_value(11) + '@ehomepay.com.cn'
            if 'phone' in post_data:
                post_data['phone'] = Get.random_value(11)
            if 'loginName' in post_data:
                post_data['loginName'] = Get.random_value(11)
            if 'bindInfo' in post_data:
                post_data['bindInfo'] = Get.random_value(11)
        if 'others' in others:
            if 'approveId' in others['others']:
                post_data['approvalId'] = others['others']['approveId']
        record, result = Get.test_steps(self.host, self.header, item, post_data)
        self.db.insert(record, 'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])
