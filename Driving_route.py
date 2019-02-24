# -*- coding: utf-8 -*-
import requests

url = r'http://api.map.baidu.com/direction/v2/driving?origin=40.01116,116.339303&destination=39.936404,116.452562&ak=rxfKZPe9YAl4kRXfhqRcSWGh92i4rYW0'
response = requests.get(url)
response_json = response.json()
print(type(response_json))

print(response_json['result']['routes'])
