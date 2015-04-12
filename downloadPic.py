__author__ = 'klin'
# -*- coding: utf-8 -*-

import urllib2


#
#
#
def downloadPic(picUrl, resPath):
    print 'downloading : %s' % picUrl

    pic = ''
    try:
        response = urllib2.urlopen(picUrl)
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