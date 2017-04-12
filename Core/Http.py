import urllib.parse
import urllib.request
import requests
import json


class Http:
    @staticmethod
    def get_json_response(url, post_data, header, prefix=''):
        if prefix == '':
            post_data = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request(url, post_data, header)
            json_result = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

        else:
            json_str = prefix + json.dumps(post_data)
            res = requests.post(url, data=json_str, headers=header).content.decode()
            json_result = json.loads(res)
        return json_result

    @staticmethod
    def get_header_response(url, post_data):
        post_data = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request(url, post_data)
        return urllib.request.urlopen(req).info().items()
