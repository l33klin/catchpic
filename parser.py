__author__ = 'klin'
# -*- coding: utf-8 -*-

import constants
import htmlClass
from downloadPic import downloadPic


#
#
#
def parsePostsBody(body):
    print 'starting parse posts body...'
    

    return True

# parse caoliu Html
#
#
def parseClHtml(htmlFileName, path):

    title = ''
    titlePre = ''
    postsBodyStart = -1

    fileP = open(path + '/' + htmlFileName, 'r')
    print 'starting parse Html: %s' % (path + '/' + htmlFileName)
    line = fileP.readline()
    while line:
        if line.startswith('<title>'):
            title = line[7:-9]
            titlePre = title[:-36]
            print 'get title : ' + title.decode('GBK')
            # print titlePre.decode('GBK')
        elif line.startswith('<h4>'):
            if line.__contains__(titlePre):
                postsBodyStart = 4
                print line[4:-6].decode('GBK')
        # elif line.

        if postsBodyStart == 0:
            print 'Body: %s' % line.decode('GBK')
            parsePostsBody(line)

        postsBodyStart -= 1
        line = fileP.readline()

    fileP.close()

    return True


# test parse function
#
#
def testParse():

    fileName = '1447785.html'
    parseClHtml(fileName, constants.LOCALPATH)

if __name__ == '__main__':
    testParse()