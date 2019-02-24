# -*- coding: utf-8 -*-
import requests

def get_driving_route(origin, destination):
    _ak = 'rxfKZPe9YAl4kRXfhqRcSWGh92i4rYW0'
    _url_prefix = r'http://api.map.baidu.com/direction/v2/driving?'
    _url_complete = _url_prefix + 'origin=' + str(origin[0]) + ',' + str(origin[1]) + '&destination='+ \
                    str(destination[0]) + ',' + str(destination[1]) +  '&ak=' + _ak
    _response = requests.get(_url_complete)
    _response_json = _response.json()
    return _response_json

a = get_driving_route(1,2)