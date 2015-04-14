__author__ = 'klin'
# -*- coding: utf-8 -*-

import constants

import urllib
import urllib2


#
#
#
def getUrlHost(url):
    host = ''
    if url.startswith('http://'):
        host = url.split('/')[2]
    else:
        print 'Wrong url  starts: %s' % url

    return host


#
#
#
def downloadPic(picUrl, resPath):
    print 'downloading : %s' % picUrl

    pic = ''
    try:
        req_header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 '
                                    '(KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',
                      'Accept': 'image/webp,*/*;q=0.8',
                      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                      'Accept-Encoding': 'gzip, deflate, sdch',
                      'Connection': 'keep-alive',
                      'Cache-Control': 'max-age=0',
                      'Referer': constants.HOST,  # if can't work replace this as url Host
                      'Host': getUrlHost(picUrl)
                      }
        req_timeout = 20
        req = urllib2.Request(picUrl, None, req_header)
        response = urllib2.urlopen(req, None, req_timeout)
        pic = response.read()
    except urllib2.URLError, e:
        print e.reason

    picFileName = picUrl.split('/')[-1]
    picFile = open(resPath + '/' + picFileName, 'w')
    picFile.write(pic)
    picFile.close()

    return './' + resPath.split('/')[-1] + '/' + picFileName


def test():

    print 'test complete!'

if __name__ == '__main__':
    test()