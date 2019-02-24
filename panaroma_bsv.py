# -*- coding: utf-8 -*-
import requests
import numpy


# given geo-address of a specific point. retrieve a panorama.
def get_panorama(lng, lat, heading):
    _filename = 'pano@lng=' + str(lng) + 'lat=' + str(lat)
    _dir = 'D:/工作/baiduMapCrawler/BSV/Panorama/'
    _path = _dir + _filename + '.jpeg'
    _ak = 'rxfKZPe9YAl4kRXfhqRcSWGh92i4rYW0'
    _url_prefix = r'http://api.map.baidu.com/panorama/v2?'
    _url_complete = _url_prefix + '&ak=' + _ak + '&width=512&height=256&location=' + str(numpy.round(lng, decimals=6)) \
                    + ',' + str(numpy.round(lat, decimals=6)) + '&heading=' + str(heading) + '&pitch=2.5' + '&fov=90'
    _response = requests.get(_url_complete)
    if _response.status_code == 200:
        with open(_path, 'wb') as f:
            f.write(_response.content)


if __name__ == '__main__':
    get_panorama(116.460962, 39.963295, 90)

