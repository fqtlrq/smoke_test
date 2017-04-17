import hashlib
import os
import random
from configparser import ConfigParser

from Core.Http import Http


def cookies():
    name_list = ['13100000020', '13100000021', '13100000022', '13100000023', '13100000024', '13100000025',
                 '13100000026', '13100000027', '13100000028', '13100000029', '13100000030', '13100000031',
                 '13100000032', '13100000033', '13100000034', '13100000035', '13100000036', '13100000037',
                 '13100000038', '13100000039', '13100000040', '13100000041', '13100000042', '13100000043',
                 '13100000044', '13100000045', '13100000046', '13100000047', '13100000048', '13100000049',
                 '13100000050', '13100000051', '13100000052', '13100000053', '13100000054', '13100000055',
                 '13100000056', '13100000057', '13100000058', '13100000059', '13100000060', '13100000061',
                 '13100000062', '13100000063', '13100000064', '13100000065', '13100000066', '13100000067',
                 '13100000068', '13100000069', '13100000070', '13100000071', '13100000072', '13100000073',
                 '13100000074', '13100000075', '13100000076', '13100000077', '13100000078', '13100000079',
                 '13100000080', '13100000081', '13100000082', '13100000083', '13100000084', '13100000085',
                 '13100000086', '13100000087', '13100000088', '13100000089', '13100000090', '13100000091',
                 '13100000092', '13100000093', '13100000094', '13100000095', '13100000096', '13100000097',
                 '13100000098', '13100000099', '13100000100', '13100000101', '13100000102', '13100000103',
                 '13100000104', '13100000105', '13100000106', '13100000107', '13100000108', '13100000109',
                 '13100000110', '13100000111', '13100000112', '13100000113', '13100000114', '13100000115',
                 '13100000116', '13100000117', '13100000118', '13100000119']

    index = random.randint(0, 99)
    post_data = {'userName': name_list[index], 'userPwd': '1111111q', 'ip': '123', 'appVersion': '2.2.1',
                 'devType': '123', 'devInfo': '123', 'devSign': '132'}
    res = Http.get_header_response('http://10.12.9.27/ehomepay-passport/app/testlogin', post_data)
    for k, v in res:
        if k == 'Set-Cookie':
            return v


def ck_key_value():
    res = Http.get_json_response('http://10.12.9.12:8083/ehomepay_usercenter/commons/getCK', '', {})
    return res['data']['ckKey'], res['data']['ckValue']


def random_value(length):
    seed = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    value = ''
    for i in range(length):
        value += random.choice(seed)
    return value


def base_dir():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def result(host, header, api_info, post_data):
    url = host + '/' + api_info['project'] + api_info['api_path']
    prefix = ''
    if api_info['api_type'] == 'web1':
        prefix = 'json='

    if api_info['api_type'] == 'web3':
        prefix = 'jsonStr='

    if api_info['api_type'] == 'web4':
        prefix = 'xml'

    return Http.get_json_response(url, post_data, header, prefix)


def sign(json_data, key):
    data_sorted = sorted(json_data.keys())
    pre_str = ''
    for k in data_sorted:
        if k == 'sign' or k == 'sign_type':
            continue
        pre_str += k + '=' + json_data[k] + '&'
    pre_str = pre_str.rstrip('&') + key

    md = hashlib.md5()
    md.update(pre_str.encode())
    return md.hexdigest()


def host(project):
    conf = os.path.join(base_dir(), 'Conf', 'Env.ini')
    cf = ConfigParser()
    cf.read(conf, 'utf-8')
    env = cf.get('machine', 'env')
    return cf.get(project, env)
