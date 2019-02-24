# -*- coding: utf-8 -*-
import requests
from urllib.request import quote
import numpy


def get_driving_route(origin, destination):
    _ak = 'rxfKZPe9YAl4kRXfhqRcSWGh92i4rYW0'
    _url_prefix = r'http://api.map.baidu.com/direction/v2/driving?'
    _url_complete = _url_prefix + 'origin=' + str(numpy.round(origin[0],decimals=6)) + ',' + str(numpy.round(origin[1],decimals=6))\
                    + '&destination='+ str(numpy.round(destination[0],decimals=6)) + ',' + str(numpy.round(destination[0],decimals=6))\
                    +  '&ak=' + _ak
    print(_url_complete)
    _response = requests.get(_url_complete)
    _response_json = _response.json()
    return _response_json


def get_geo_address(address):
    _ak = 'rxfKZPe9YAl4kRXfhqRcSWGh92i4rYW0'
    _url_prefix = 'http://api.map.baidu.com/geocoder/v2/?address='
    _output = 'json'
    _address = quote(address)
    _url_complete = _url_prefix + _address + '&output=' + _output + "&ak=" + _ak
    _response = requests.get(_url_complete)
    _response_json = _response.json()
    return (_response_json['result']['location']['lng'],_response_json['result']['location']['lat'])


origin = get_geo_address('北京市海淀区上地十街10号')
destination = get_geo_address('北京市海淀区上丹棱街12号')

print(origin)
print(destination)

result = get_driving_route(origin, destination)
print(result)

