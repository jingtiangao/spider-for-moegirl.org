#-*- coding: UTF-8 -*-
import urllib2
import cookielib


url ="http://www.baidu.com"
print 'first'
response1= urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print 'second'

request = urllib2.Request(url)
request.add_header("user-agent", "Mozilla")
response2= urllib2.urlopen(request)
print response2.getcode()
print response2.read()

print 'third cookie'
cj=cookielib.CookieJar()

#===============================================================================
# 给urlib2安装处理器
#===============================================================================
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3= urllib2.urlopen(url)
print response3.getcode()
print response3.read()



