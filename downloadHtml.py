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
import sys
import getopt

# get complete url
#
#
def getCompleteUrl(incompleteUrl):

    completeUrl = ''

    if incompleteUrl.startswith('http://'):
        return incompleteUrl
    else:
        if not incompleteUrl.startswith('/'):
            incompleteUrl = '/' + incompleteUrl

    completeUrl = constants.HOST + incompleteUrl
    return completeUrl


# function: download url and create folder to save resource file
#
#
def downloadHtml(urlSuf, path):

    # down load url
    url = getCompleteUrl(urlSuf)
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


#
#
#
def parseOpt():
    opts, args = getopt.getopt(sys.argv[1:], "u:p:h", ["url=",  "path=", 'help'])

    url = ''
    path = ''
    for a, o in opts:
        if a in ('-u', '--url'):
            url = o
        elif a in ('-p', '--path'):
            path = o
        elif a in ('-h', '--help'):
            print 'u(url): url to download;'
            print 'p(path): path to store html file;'
            print 'h(help): just help.'

    return url, path

# test function
#
#
def main(url, path):

    if url == '':
        print 'No URL!!!'
        return False

    if path == '':
        path = constants.LOCALPATH

    fileName = downloadHtml(url, path)
    parser.parseClHtml(fileName, constants.LOCALPATH)

    print 'test complete!'

    return True

if __name__ == '__main__':
    url, path = parseOpt()
    main(url, path)