# -*- coding: utf-8 -*-
import requests
import numpy


# given geo-address of a specific point. retrieve a statics
# Dev-files see http://lbsyun.baidu.com/index.php?title=static


def get_static_view(lng, lat):
    _filename = 'static@lng=' + str(lng) + 'lat=' + str(lat)
    _dir = 'D:/工作/baiduMapCrawler/BSV/StaticImage/'
    _path = _dir + _filename + '.jpeg'
    _ak = 'rxfKZPe9YAl4kRXfhqRcSWGh92i4rYW0'
    _url_prefix = r'http://api.map.baidu.com/staticimage/v2?'
    _url_complete = _url_prefix + '&ak=' + _ak + '&width=1024&height=512&location='+ '&width=1024&height=1024'+ \
        '&center='+ str(numpy.round(lng, decimals=6)) + ',' + str(numpy.round(lat, decimals=6)) + '&zoom=18'+ '&markers='\
        + str(numpy.round(lng, decimals=6)) + ',' + str(numpy.round(lat, decimals=6))
    _response = requests.get(_url_complete)
    if _response.status_code == 200:
        with open(_path, 'wb') as f:
            f.write(_response.content)


if __name__ == '__main__':
  get_static_view(116.460962, 39.963295)



