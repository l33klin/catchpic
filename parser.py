__author__ = 'klin'
# -*- coding: utf-8 -*-

import constants
import htmlClass
from downloadPic import downloadPic


#
#
#
def parsePostsBody(body, resPath):
    print 'starting parse posts body...'

    bodyAfterReplace = body
    startIndex = body.find('<img src=')
    while startIndex != -1:
        endIndex = body[startIndex + 10:].find('\'')
        picUrl = body[startIndex + 10: startIndex + 10 + endIndex]
        print picUrl
        picLocal = downloadPic(picUrl, resPath)
        print 'Replace %s as %s' % (picUrl, picLocal)
        bodyAfterReplace = bodyAfterReplace.replace(picUrl, picLocal)

        startIndex = body.find('<img src=', startIndex + 1)

    # print 'Replaced body: %s' % bodyAfterReplace
    return bodyAfterReplace

# parse caoliu Html
#
#
def parseClHtml(htmlFileName, path):

    title = ''
    titlePre = ''
    postsBodyStart = -1
    replacedHtml = ''

    fileP = open(path + '/' + htmlFileName, 'r')
    print 'starting parse Html: %s' % (path + '/' + htmlFileName)
    line = fileP.readline()
    while line:
        if line.startswith('<title>'):
            title = line[7:-9]
            titlePre = title[:-36]
            print 'get title : ' + title.decode('GBK')
            if constants.SIMPLIFY:
                replacedHtml += line
            # print titlePre.decode('GBK')
        elif line.startswith('<h4>'):
            if line.__contains__(titlePre):
                postsBodyStart = 4
                print line[4:-6].decode('GBK')
                if constants.SIMPLIFY:
                    replacedHtml += line
        # elif line.

        if postsBodyStart == 0:
            # print 'Body: %s' % line.decode('GBK')
            resPath = path + '/' + htmlFileName.split('.')[0]
            line = parsePostsBody(line, resPath)
            if constants.SIMPLIFY:
                replacedHtml += line

        postsBodyStart -= 1
        if not constants.SIMPLIFY:
            replacedHtml += line
        line = fileP.readline()

    fileP.close()

    fileP = open(path + '/' + htmlFileName, 'w')
    fileP.write(replacedHtml)
    fileP.close()

    print 'rewrite html complete'
    return True


# test parse function
#
#
def testParse():

    fileName = '1447785.html'
    parseClHtml(fileName, constants.LOCALPATH)

if __name__ == '__main__':
    testParse()