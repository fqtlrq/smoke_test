import unittest

from Core.DB import *


class UserCenter(unittest.TestCase):
    """
    用户中心
    """
    host = Get.host('user_center', 'test')

    def setUp(self):
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.db = DB()

    def test_saveUserInfo(self):
        self.analysis(20, True)

    def test_checkPhone(self):
        self.analysis(21, True)

    def test_checkLogin(self):
        self.analysis(22)

    def test_queryRealAuthInfo(self):
        self.analysis(23)

    def test_checkCertVaild(self):
        self.analysis(24)

    def test_getVocationList(self):
        self.analysis(25)

    def test_getCK(self):
        self.analysis(26)

    def test_queryUserInfoByLogin(self):
        self.analysis(27)

    def test_queryUserInfoByName(self):
        self.analysis(49)

    def test_editUserInfo(self):
        self.analysis(28)

    def test_updatePhone(self):
        self.analysis(29, True)

    def test_updateHeadPic(self):
        self.analysis(30)

    def test_updateSignature(self):
        self.analysis(31)

    def test_updateEmail(self):
        self.analysis(32)

    def test_queryUserInfo(self):
        self.analysis(33)

    def test_getQuestions(self):
        self.analysis(34)

    def test_queryQuestionById(self):
        self.analysis(35)

    def test_setPhone(self):
        self.analysis(36, True)

    def test_setEmail(self):
        self.analysis(37, True)

    def test_queryCancelUserList(self):
        self.analysis(38, True)

    def test_queryEmailOrPhoneExist(self):
        self.analysis(39, True)

    def test_countRealAuthNum(self):
        self.analysis(40)

    def test_countRegisterNum(self):
        self.analysis(41)

    def test_saveRealAuthInfoFirst(self):
        self.analysis(42)

    def test_saveRealAuthInfoSecond(self):
        self.analysis(43)

    def test_queryCertsApprovalList(self):
        self.analysis(44)

    def test_queryAuthApprovalList(self):
        self.analysis(45)

    # def test_approveAuthAndUpdateCertInfo(self):
    #     '''
    #     1.查询证件审核下的待审核approveId
    #     2.进行驳回操作
    #     3.更新证件信息使其重新变为待审核状态
    #     :return:
    #     '''
    #     item = self.db.query_one("select * from api where id=44")
    #     post_data = eval(item['params'])
    #     record, result = Get.test_steps(self.host, self.header, item, post_data)
    #     approve_id = result['data']['data'][0]['approvalId']
    #     self.run_test(46, others={'approveId': approve_id})
    #     self.run_test(47)

    def test_setsecQuestions(self):
        self.analysis(50)

    def test_checkQuestions(self):
        self.analysis(51)

    def test_queryAuthApprovalDetail(self):
        self.analysis(52)

    def analysis(self, case_id, random=False):
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
                # if 'others' in others:
                # if 'approveId' in others['others']:
                #     post_data['approvalId'] = others['others']['approveId']
        result = Get.result(self.host, self.header, item, post_data)
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])


class PosCashier(unittest.TestCase):
    """
    POS收银台
    """
    partner_flow = ''
    host = Get.host('pos_cashier', 'test')

    def setUp(self):
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.db = DB()

    def test_payByOrderPos_1prePay(self):
        res_data = self.analysis(53, random_key='partnerFlow')
        PosCashier.partner_flow = res_data['partnerFlow']

    def test_payByOrderPos_cancelPay(self):
        self.analysis(54, ref_data={'partnerFlow': PosCashier.partner_flow})

    def test_payByOrderPos_queryPay(self):
        self.analysis(55, encrypt_sign=False)

    def test_payByOrderPos_queryBatch(self):
        self.analysis(56, encrypt_sign=False)

    def analysis(self, case_id, random_key='', ref_data={}, encrypt_sign=True):
        item = self.db.query_one("select * from api where id=" + str(case_id))
        post_data = eval(item['params'])
        if random_key == '':
            pass
        else:
            post_data[random_key] = Get.random_value(20)

        if ref_data == {}:
            pass
        else:
            for k, v in ref_data.items():
                post_data[k] = v

        if encrypt_sign is True:
            post_data['sign'] = Get.sign(post_data, 'seNJ00')

        result = Get.result(PosCashier.host, self.header, item, post_data)
        self.assertEqual(item['expect'], 'returnCode:' + str(result['returnCode']), item['api_path'])
        return result
