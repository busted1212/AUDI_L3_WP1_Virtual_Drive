from urllib.request import quote
import requests
import numpy
import sys


def get_geo_address(address):
    # get latitude and longitude of an address given in chinese
    # structured address conforming the conventions of baidu
    # returns the latitude and longitude of an address
    _ak = 'rxfKZPe9YAl4kRXfhqRcSWGh92i4rYW0'
    _url_prefix = 'http://api.map.baidu.com/geocoder/v2/?address='
    _output = 'json'
    _address = quote(address)
    _url_complete = _url_prefix + _address + '&output=' + _output + "&ak=" + _ak
    _response = requests.get(_url_complete)
    _response_json = _response.json()
    return (_response_json['result']['location']['lat'],_response_json['result']['location']['lng'])


def get_driving_route(origin, destination):
    # input: lng and lat of both origin and destination
    # return the parsed result in a json file
    _ak = 'rxfKZPe9YAl4kRXfhqRcSWGh92i4rYW0'
    _url_prefix = r'http://api.map.baidu.com/direction/v2/driving?'
    _url_complete = _url_prefix + 'origin=' + str(numpy.round(origin[0],decimals=6)) + ',' +\
                    str(numpy.round(origin[1], decimals=6)) + '&destination=' + \
                    str(numpy.round(destination[0], decimals=6)) + ',' + str(numpy.round(destination[1], decimals=6))\
                    + '&waypoints=39.968273,116.314721|39.874614,116.317766|39.963255,116.460972'\
                    '&ak=' + _ak
    print(_url_complete)
    _response = requests.get(_url_complete)
    _response_json = _response.json()
    return _response_json


def get_panorama(lng, lat, heading):
    # given geo-address of a specific point. retrieve a panorama.
    _filename = 'pano@lng=' + str(lng) + 'lat=' + str(lat)
    _dir = 'D:/工作/baiduMapCrawler/BSV/Panorama/'
    _path = _dir + _filename + '.jpeg'
    _ak = 'rxfKZPe9YAl4kRXfhqRcSWGh92i4rYW0'
    _url_prefix = r'http://api.map.baidu.com/panorama/v2?'
    _url_complete = _url_prefix + '&ak=' + _ak + '&width=1024&height=512&location=' + str(numpy.round(lng, decimals=6))\
                    + ',' + str(numpy.round(lat, decimals=6)) + '&heading=' + str(heading) + '&pitch=38' + '&fov=90'
    _response = requests.get(_url_complete)
    if _response.status_code == 200:
        with open(_path, 'wb') as f:
            f.write(_response.content)
    else:
        sys.exit("HTTP response error, error code" + _response.status_code)


#
def get_static_view(lng, lat):
    # given geo-address of a specific point, retrieve a static view with a marker centered in the pic
    _filename = 'static@lng=' + str(lng) + 'lat=' + str(lat)
    _dir = 'D:/工作/baiduMapCrawler/BSV/StaticImage/'
    _path = _dir + _filename + '.jpeg'
    _ak = 'rxfKZPe9YAl4kRXfhqRcSWGh92i4rYW0'
    _url_prefix = r'http://api.map.baidu.com/staticimage/v2?'
    _url_complete = _url_prefix + '&ak=' + _ak + '&width=1024&height=512&location='+ '&width=1024&height=1024'+ \
        '&center='+ str(numpy.round(lng, decimals=6)) + ',' + str(numpy.round(lat, decimals=6)) + '&zoom=12'+ '&markers='\
        + str(numpy.round(lng, decimals=6)) + ',' + str(numpy.round(lat, decimals=6))
    _response = requests.get(_url_complete)
    if _response.status_code == 200:
        with open(_path, 'wb') as f:
            f.write(_response.content)


def path_analyzer(path):
    # given a path on the driving route(a string), split the string to discrete points and store in a list
    _steps = path.split(';')
    _path_sorted = []
    for j in _steps:
        _key_point = j.split(',')
        _path_sorted.append(_key_point)
    return _path_sorted


def angle_calculate(point1, point2):
    # given two geo-points(lng, lat), calculate the angle of the line between the two
    # with respect to the the horizontal line
    # type check
    _lng_pt1 = point1[0]
    _lat_pt1 = point1[1]
    _lng_pt2 = point2[0]
    _lat_pt2 = point2[1]
    _x = numpy.sin(_lng_pt2 - _lng_pt1) * numpy.cos(_lat_pt2)
    _y = numpy.cos(_lat_pt1) * numpy.sin(_lat_pt2) - numpy.sin(_lng_pt1) * numpy.cos(_lng_pt2)\
         * numpy.cos(_lng_pt2 - _lng_pt1)
    _A = numpy.arctan2(_x, _y)
    _Bearing = numpy.mod(_A, 360)
