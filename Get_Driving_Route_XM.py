# -*- coding: utf-8 -*-

import requests
from urllib.request import quote
import numpy
import sys
import time
# Created by IAV Shanghai,Xiangming Hao & Chen Zhang
# with the help of Antoine Frot,IAV Munich
# Input: Structural address conforming Baidu Map Convention
# Output: Routes with leg points and description
# Disclaimer to be completed


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
    return (_response_json['result']['location']['lat'],_response_json['result']['location']['lng'])


# input: lng and lat of both origin and destination
def get_driving_route(origin, destination):
    _ak = 'rxfKZPe9YAl4kRXfhqRcSWGh92i4rYW0'
    _url_prefix = r'http://api.map.baidu.com/direction/v2/driving?'
    _url_complete = _url_prefix + 'origin=' + str(numpy.round(origin[0],decimals=6)) + ',' + str(numpy.round(origin[1],decimals=6))\
                    + '&destination='+ str(numpy.round(destination[0],decimals=6)) + ',' + str(numpy.round(destination[1],decimals=6))\
                    + '&waypoints=39.898521,116.468116|39.973509,116.446125|39.969286,116.317263'\
                    + '&tactics=4'\
                    '&ak=' + _ak
    print(_url_complete)
    _response = requests.get(_url_complete)
    _response_json = _response.json()
    return _response_json


# given geo-address of a specific point. retrieve a panorama.
def get_panorama(lng, lat, heading):
    _filename = 'pano@lng=' + str(lng) + 'lat=' + str(lat)
    _dir = r'D://工作//AUDI_L3_WP1_Virtual_Drive//BSV//Panorama//'
    _path = _dir + _filename + '.jpeg'
    _ak = 'rxfKZPe9YAl4kRXfhqRcSWGh92i4rYW0'
    _url_prefix = r'http://api.map.baidu.com/panorama/v2?'
    _url_complete = _url_prefix + '&ak=' + _ak + '&width=1024&height=512&location=' + str(numpy.round(lng, decimals=6)) \
                    + ',' + str(numpy.round(lat, decimals=6)) + '&heading=' + str(heading) + '&pitch=38' + '&fov=90'
    _response = requests.get(_url_complete)
    if _response.status_code == 200:
        with open(_path, 'wb') as f:
            f.write(_response.content)
    else:
        sys.exit("HTTP response error, error code" + _response.status_code)
    return numpy.round(lng, decimals=6), numpy.round(lat, decimals=6), _url_complete


def get_static_view(lng, lat):
    _filename = 'static@lng=' + str(lng) + 'lat=' + str(lat)
    _dir = r'D://工作//AUDI_L3_WP1_Virtual_Drive//BSV//StaticImage//'
    _path = _dir + _filename + '.jpeg'
    _ak = 'rxfKZPe9YAl4kRXfhqRcSWGh92i4rYW0'
    _url_prefix = r'http://api.map.baidu.com/staticimage/v2?'
    _url_complete = _url_prefix + '&ak=' + _ak + '&width=1024&height=512&location='+ '&width=1024&height=1024'+ \
        '&center='+ str(numpy.round(lng, decimals=6)) + ',' + str(numpy.round(lat, decimals=6)) + '&zoom=17'+ '&markers='\
        + str(numpy.round(lng, decimals=6)) + ',' + str(numpy.round(lat, decimals=6))
    _response = requests.get(_url_complete)
    if _response.status_code == 200:
        with open(_path, 'wb') as f:
            f.write(_response.content)


def path_analyzer(path):
    _steps = path.split(';')
    _path_sorted = []
    for j in _steps:
        _key_point = j.split(',')
        _path_sorted.append(_key_point)
    return _path_sorted


origin1 = get_geo_address('北京市南三环西路90号')
destination1 = get_geo_address('北京市南三环西路90号')
origin2 = (116.339478, 39.854562)
destination2 = (116.339478, 39.854562)
print(origin2)
print(destination2)

# return a dictionary
result = get_driving_route(origin1,destination1)

# info about the route in general, e.g. distance, duration
print(type(result))
print(result)
route_general = result['result']['routes'][-1]


# info about the detailed routes, in form of a list, each element represent a road
steps = route_general['steps']
# each road contains info about direction and a distance with key points
gps_url_list = [] # list for storing gps and url
for step in steps:
    rd_name = step['road_name']
    rd_direction = step['direction'] * 30
    print(rd_name)
    print(rd_direction)
    # print(type(rd_direction))
    rd_path = step['path']
    rd_path_sorted = path_analyzer(rd_path)
    for path_point in rd_path_sorted:
        print(path_point)
        #print(rd_direction)
        pano_lng, pano_lat, pano_url = get_panorama(float(path_point[0]), float(path_point[1]), rd_direction)
        time.sleep(2)
        get_static_view(float(path_point[0]), float(path_point[1]))
        time.sleep(2)
        gps_url_list.append([pano_lng, pano_lat, pano_url])
    print(rd_path_sorted)
print(len(gps_url_list))


with open('your_file.txt', 'w') as f:
    for item in gps_url_list:
        f.write("%s\n" % item)
# print(len(route_detailed['steps']))
# steps_real = route_detailed['steps'][0]
# print(steps_real)
# for z in steps_real:
#     print(z)


# this block of code will request the bsv and save it
# to be modularized
# for i in result['result']['routes'][-1]['steps']:
#     print(len(i['path']))
#     print(type(i['path']))
#     steps = i['path'].split(';')
#     print(steps)
#     for j in steps:
#         key_points = j.split(',')
#         print(key_points[0], key_points[1])
#         get_panorama(float(key_points[0]), float(key_points[1]))

