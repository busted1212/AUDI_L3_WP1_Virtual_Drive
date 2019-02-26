# -*- coding: utf-8 -*-
import sys
import time
from baidumap import *
# Created by IAV Shanghai,Xiangming Hao & Chen Zhang
# with the help of Antoine Frot,IAV Munich
# Input: Structural address conforming Baidu Map Convention
# Output: Routes with leg points and description
# Disclaimer to be completed
origin1 = get_geo_address('北京市安贞桥')
destination1 = get_geo_address('北京市安贞桥')

print(origin1)
print(destination1)

# return a dictionary
result = get_driving_route(origin1, destination1)
#print(result['result']['routes'][-1])





# info about the route in general, e.g. distance, duration
print(type(result))
print(result)
route_general = result['result']['routes'][-1]


# info about the detailed routes, in form of a list, each element represent a road
steps = route_general['steps']
# each road contains info about direction and a distance with key points
for step in steps:
    rd_name = step['road_name']
    rd_direction = step['direction'] * 30
    print(rd_direction)
    print(type(rd_direction))
    rd_path = step['path']
    rd_path_sorted = path_analyzer(rd_path)
    for path_point in rd_path_sorted:
        get_panorama(float(path_point[0]), float(path_point[1]), rd_direction - 15)
        time.sleep(2)
        get_static_view(float(path_point[0]), float(path_point[1]))
        time.sleep(2)
    print(rd_path_sorted)

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

