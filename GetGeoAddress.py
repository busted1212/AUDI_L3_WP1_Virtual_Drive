# -*- coding: utf-8 -*-

import requests
from urllib.request import quote

# 百度地图简介
# 百度地图Web服务API为开发者提供http/https接口，
# 即开发者通过http/https形式发起检索请求，获取返回json或xml格式的检索数据。
# 用户可以基于此开发JavaScript、C#、C++、Java等语言的地图应用


# get latitude and longitude of an address given in chinese
# structured address conforming the conventions of baidu
# returns the https resp of an address
def get_geo_address(address):
    _ak = 'rxfKZPe9YAl4kRXfhqRcSWGh92i4rYW0'
    _url_prefix = 'http://api.map.baidu.com/geocoder/v2/?address='
    _output = 'json'
    _address = quote(address)
    _url_complete = _url_prefix + _address + '&output=' + _output + "&ak=" + _ak
    _response = requests.get(_url_complete)
    _response_json = _response.json()
    return (_response_json['result']['location']['lng'],_response_json['result']['location']['lat'])


result = get_geo_address('北京市苏州桥')
print(result)