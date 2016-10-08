#-*- coding: UTF-8 -*-
#===============================================================================
# '''
# Created on 2016年7月8日
# 
# @author: gaochuyang
# '''
#===============================================================================
from bs4  import BeautifulSoup
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sisterimport" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# 使用html解析器解析html——doc 编码方式为utf-8
soup=BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

print '所有链接'
links=soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()

#提取每个链接对应的名称，url 文字
print '获取tile'
link_node = soup.find('a',href="http://example.com/tillie")
print link_node.get_text()
link_node=soup.find('a',href=re.compile(r"sie")) #r表示正则表达式中出现了反斜线只需要写一个
print link_node.get_text()

#正则表达式模糊匹配

#获取p段落文字
print 'p'




