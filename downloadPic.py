__author__ = 'klin'
# -*- coding: utf-8 -*-

import urllib
import urllib2


#
#
#
def downloadPic(picUrl, resPath):
    print 'downloading : %s' % picUrl

    pic = ''
    try:
        req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) '
                                    'Chrome/23.0.1271.64 Safari/537.11',
                      'Accept': 'text/html;q=0.9,*/*;q=0.8',
                      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                      'Accept-Encoding': 'gzip',
                      'Connection': 'close',
                      'Referer': None  # if can't work replace this as url Host
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