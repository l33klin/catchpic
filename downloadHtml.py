__author__ = 'klin'

# edit at 2015-04-10
# Download html
#
#

import constants

import urllib
import urllib2
import urlparse
import hashlib


# function: download url
#
#
def download(url, path):

    response = urllib2.urlopen(url)
    html = response.read()
    print html

    fileName = ''
    if url.split('/')[-1].endswith('.html'):
        fileName = url.split('/')[-1]
    else:
        fileName = hashlib.md5(html.encode('utf-8')).hexdigest() + '.html'
    htmlFile = open(path + '/' + fileName, 'w')
    htmlFile.write(html)
    htmlFile.close()

    return True


# test function
#
#
def test():

    url = "http://cl.44kan.info/htm_data/7/1504/1447785.html"
    download(url, constants.LOCALPATH)

    return True


if __name__ == '__main__':
    test()