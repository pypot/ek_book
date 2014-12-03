#_*_ coding: utf-8 _*_

import json
import numpy
from numpy import sin, cos, arccos, arcsin

EARTH_R = 6371.004
AK_CODE = 'hGYEy6hgmrw1LPoVt9zKfH4x'

def GetGeoCoord(addr, city):
    requstUrl = "http://api.map.baidu.com/geocoder/v2/?address=%s&city=%s&output=json&ak=%s" % (addr, city, AK_CODE)
    print requstUrl
    socket = None
    try:
        socket = urllib2.urlopen(requstUrl)
    except:
        if socket:
            socket.close()
        return None
    try:
        content = socket.read()
        socket.close()
        rslt = json.loads(content)
        return rslt['result']['location']['lng'], rslt['result']['location']['lat']
    except:
        return None



def CalcGeoCoordDist(coord1, coord2):
    radLng1 = coord1[0] / 180.0 * numpy.pi
    radLng2 = coord2[0] / 180.0 * numpy.pi
    radLat1 = coord1[1] / 180.0 * numpy.pi
    radLat2 = coord2[1] / 180.0 * numpy.pi
    distance = 2 * arcsin((sin((radLat1 - radLat2) / 2.0) ** 2 + cos(radLat1) * cos(radLat2) * (sin((radLng1 - radLng2)/2.0) ** 2 ) ** 0.5)) * EARTH_R
    return distance



def AddrDist(addr1, addr2, city):
    coord1 = GetGeoCoord(addr1, city)
    if not coord1:
        return None
    coord2 = GetGeoCoord(addr2, city)
    if not coord2:
        return None
    return CalcGeoCoordDist(coord1, coord2)



if __name__ == "__main__":
    print AddrDist('大望路地铁站西北口', '金地中心B座', '北京市')