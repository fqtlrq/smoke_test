import urllib.parse
import urllib.request
import json


class Http:
    @staticmethod
    def get_json_response(url, post_data, header):
        post_data = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request(url, post_data, header)
        return json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

    @staticmethod
    def get_header_response(url, post_data):
        post_data = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request(url, post_data)
        return urllib.request.urlopen(req).info().items()
