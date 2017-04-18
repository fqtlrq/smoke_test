from Core.DB import DB

db = DB()

data = {'project': 'poscashier_spbill',
        'api_path': '/allinpay/sysRefundTotalDetail',
        'api_type': 'web2',
        'params': "{}",
        'expect': 'code:200'}
print(db.insert(data, 'api'))
