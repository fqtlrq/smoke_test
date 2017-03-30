from Core.DB import DB

db = DB()

data = {'project': 'app-native-http2.2',
        'api_path': '/newRealAuth/updateSignature',
        'api_type': 'app',
        'params': "{'appVersion':'2.2.0','reserveInfo':'abc'}",
        'expect': 'code:你啊好哦'}

print(db.insert(data, 'api'))
