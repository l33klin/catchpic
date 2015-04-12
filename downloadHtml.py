__author__ = 'klin'
# -*- coding: utf-8 -*-

# edit at 2015-04-10
# Download html
#
#

import constants
import parser

import urllib
import urllib2
import hashlib
import cookielib
import os


# function: download url and create folder to save resource file
#
#
def downloadHtml(urlSuf, path):

    if not urlSuf.startswith('/'):
        urlSuf = '/' + urlSuf

    # down load url
    url = constants.HOST + urlSuf
    print 'url: %s' % url
    cookieJ = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJ))
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    response = opener.open(req)
    html = response.read()
    #print html

    # write html file to local
    fileName = ''
    if url.endswith('.html'):
        fileName = url.split('/')[-1]
    else:
        fileName = hashlib.md5(html.encode('utf-8')).hexdigest() + '.html'
    htmlFile = open(path + '/' + fileName, 'w')
    htmlFile.write(html)
    htmlFile.close()

    # create folder
    os.mkdir(path + '/' + fileName.split('.')[0])

    return fileName


# test function
#
#
def test():

    url = "/htm_data/7/1504/1447785.html"
    fileName = downloadHtml(url, constants.LOCALPATH)
    # parser.parseClHtml(fileName, constants.LOCALPATH)

    print 'test complete!'

    return True

if __name__ == '__main__':
    test()