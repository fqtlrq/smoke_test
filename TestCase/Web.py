import unittest

import requests

from Core.DB import *


class UserCenter(unittest.TestCase):
    """用户中心"""

    host = Get.host('user_center')

    def setUp(self):
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.db = DB()

    def test_passport_saveUserInfo(self):
        """/passport/saveUserInfo"""
        self.analysis(20, True)

    def test_passport_checkPhone(self):
        """/passport/checkPhone"""
        self.analysis(21, True)

    def test_passport_checkLogin(self):
        """/passport/checkLogin"""
        self.analysis(22)

    def test_realAuth_queryRealAuthInfo(self):
        """/realAuth/queryRealAuthInfo"""
        self.analysis(23)

    def test_realAuth_checkCertVaild(self):
        """/realAuth/checkCertVaild"""
        self.analysis(24)

    def test_commons_getVocationList(self):
        """/commons/getVocationList"""
        self.analysis(25)

    def test_commons_getCK(self):
        """/commons/getCK"""
        self.analysis(26)

    def test_passport_queryUserInfoByLogin(self):
        """/passport/queryUserInfoByLogin"""
        self.analysis(27)

    def test_userSet_queryUserInfoByName(self):
        """/userSet/queryUserInfoByName"""
        self.analysis(49)

    def test_userSet_editUserInfo(self):
        """/userSet/editUserInfo"""
        self.analysis(28)

    def test_userSet_updatePhone(self):
        """/userSet/updatePhone"""
        self.analysis(29, True)

    def test_userSet_updateHeadPic(self):
        """/userSet/updateHeadPic"""
        self.analysis(30)

    def test_userSet_updateSignature(self):
        """/userSet/updateSignature"""
        self.analysis(31)

    def test_userSet_updateEmail(self):
        """/userSet/updateEmail"""
        self.analysis(32)

    def test_userSet_queryUserInfo(self):
        """/userSet/queryUserInfo"""
        self.analysis(33)

    def test_userSet_getQuestions(self):
        """/userSet/getQuestions"""
        self.analysis(34)

    def test_userSet_queryQuestionById(self):
        """/userSet/queryQuestionById"""
        self.analysis(35)

    def test_userSet_setPhone(self):
        """/userSet/setPhone"""
        self.analysis(36, True)

    def test_userSet_setEmail(self):
        """/userSet/setEmail"""
        self.analysis(37, True)

    def test_approval_queryCancelUserList(self):
        """/approval/queryCancelUserList"""
        self.analysis(38, True)

    def test_userSet_queryEmailOrPhoneExist(self):
        """/userSet/queryEmailOrPhoneExist"""
        self.analysis(39, True)

    def test_countUserInfo_countRealAuthNum(self):
        """/countUserInfo/countRealAuthNum"""
        self.analysis(40)

    def test_countUserInfo_countRegisterNum(self):
        """/countUserInfo/countRegisterNum"""
        self.analysis(41)

    def test_realAuth_saveRealAuthInfoFirst(self):
        """/realAuth/saveRealAuthInfoFirst"""
        self.analysis(42)

    def test_realAuth_saveRealAuthInfoSecond(self):
        """/realAuth/saveRealAuthInfoSecond"""
        self.analysis(43)

    def test_approval_queryCertsApprovalList(self):
        """/approval/queryCertsApprovalList"""
        self.analysis(44)

    def test_approval_queryAuthApprovalList(self):
        """/approval/queryAuthApprovalList"""
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

    def test_userSet_setsecQuestions(self):
        """/userSet/setsecQuestions"""
        self.analysis(50)

    def test_userSet_checkQuestions(self):
        """/userSet/checkQuestions"""
        self.analysis(51)

    def test_approval_queryAuthApprovalDetail(self):
        """/approval/queryAuthApprovalDetail"""
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


class PosCashierWeb(unittest.TestCase):
    """POS收银台"""

    partner_flow = ''
    host = Get.host('pos_cashier_web')

    def setUp(self):
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.db = DB()

    def test_payByOrderPos_1prePay(self):
        """/payByOrderPos/prePay"""

        res_data = self.analysis(53, random_key='partnerFlow')
        PosCashierWeb.partner_flow = res_data['partnerFlow']

    def test_payByOrderPos_cancelPay(self):
        """/payByOrderPos/cancelPay"""

        self.analysis(54, ref_data={'partnerFlow': PosCashierWeb.partner_flow})

    def test_payByOrderPos_queryPay(self):
        """/payByOrderPos/queryPay"""

        self.analysis(55, encrypt_sign=False)

    def test_payByOrderPos_queryBatch(self):
        """/payByOrderPos/queryBatch"""

        self.analysis(56, encrypt_sign=False)

    def test_allinpay_orderQueryInfo(self):
        """/allinpay/orderQueryInfo"""
        item = self.db.query_one("select * from api where id=58")
        post_url = '%s/%s%s' % (PosCashierWeb.host, item['project'], item['api_path'])
        post_data = item['params']
        res = requests.post(post_url, data=post_data, headers=self.header).content.decode()
        r1 = item['expect'].split(';')[0]
        r2 = item['expect'].split(';')[1]
        r_value = 'Pass' if r1 in res or r2 in res else 'Fail'
        self.db.insert(
            {'project': item['project'], 'api_path': item['api_path'], 'api_type': item['api_type'], 'result': r_value},
            'result')

        expect = '!!!@@@'
        if r1 in res:
            expect = r1
        if r2 in res:
            expect = r2
        self.assertIn(expect, res, item['api_path'])

    def analysis(self, case_id, random_key='', ref_data={}, encrypt_sign=True):
        item = self.db.query_one("select * from api where id=" + str(case_id))
        if item['api_type'] != 'web4':
            post_data = eval(item['params'])
        else:
            post_data = item['params']

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

        result = Get.result(PosCashierWeb.host, self.header, item, post_data)

        r_value = 'Pass' if item['expect'] == 'returnCode:' + str(result['returnCode']) else 'Fail'
        self.db.insert(
            {'project': item['project'], 'api_path': item['api_path'], 'api_type': item['api_type'], 'result': r_value},
            'result')
        self.assertEqual(item['expect'], 'returnCode:' + str(result['returnCode']), item['api_path'])
        return result


class PosCashierSpBill(unittest.TestCase):
    """对账"""
    host = Get.host('pos_cashier_spbill')

    def setUp(self):
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.db = DB()

    def test_runspbill(self):
        """/allinpay/runspbill"""
        self.analysis(57)

    def test_allinpay_spbillresult(self):
        """/allinpay/spbillresult"""
        self.analysis(59)

    def test_allinpay_spbilldetail(self):
        """/allinpay/spbilldetail"""
        self.analysis(60)

    # def test_allinpay_updateSpbillStatus(self):
    #     """/allinpay/updateSpbillStatus"""
    #     self.analysis(61)

    def test_allinpay_sysRefundTotal(self):
        """/allinpay/sysRefundTotal"""
        self.analysis(62)

    def test_allinpay_addRefundFile(self):
        """/allinpay/addRefundFile"""
        self.analysis(63)

    def test_allinpay_sysRefundTotalDetail(self):
        """/allinpay/sysRefundTotalDetail"""
        self.analysis(64)

    def analysis(self, case_id):
        item = self.db.query_one("select * from api where id=" + str(case_id))
        post_data = eval(item['params'])

        result = Get.result(PosCashierSpBill.host, self.header, item, post_data)
        r_value = 'Pass' if item['expect'] == 'code:' + str(result['code']) else 'Fail'
        self.db.insert(
            {'project': item['project'], 'api_path': item['api_path'], 'api_type': item['api_type'], 'result': r_value},
            'result')
        self.assertEqual(item['expect'], 'code:' + str(result['code']), item['api_path'])
