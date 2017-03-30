from Core.DB import DB

db = DB()

data = {'project': 'ehomepay-passport',
        'api_path': '/app/logout',
        'api_type': 'app',
        'params': "{'appVersion':'2.2.0','userId':'1000550'}",
        'expect': 'code:0'}

print(db.insert(data, 'api'))
