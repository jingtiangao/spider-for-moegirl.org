#-*- coding: UTF-8 -*-
#===============================================================================
# '''
# Created on 2016年7月8日
# 
# @author: gaochuyang
#===============================================================================
# # '''
#===============================================================================
#===============================================================================
import json
import codecs

import unicodedata
class  HtmlOutputer(object):
    def __init__(self):
        self.datas=[] #这里datas是一个List 用append添加
    
    def collect_data(self,data):#收集数据
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):#收集数据存入文件中
        count=1;
        for item in self.datas: 
            str1='data/'
            str2 = str(count)
            str3 = '.json'
            str1 += str2
            str1 += str3
            self.file = codecs.open(str1, mode='wb',encoding='utf-8')
            line = json.dumps(item)
            self.file.write(line.decode("unicode_escape"))
            count+=1
        
#===============================================================================
#         fout=open('output.html','w')
#         fout.write("<html>")
#         fout.write("""<head>
# <meta charset="UTF-8">
# <meta http-equiv="X-UA-Compatible" content="IE=Edge" /></head>""")
#         fout.write("<body>")
#         fout.write("<table>")
#         #用表格的形式输出
#         #python 默认编码是aciii要把它转码成utf-8
#         for data in self.datas:
#             fout.write("<tr>")
#             fout.write("<td>%s</td>"%data['url'])
#             fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
#             fout.write("<td>%s</td>"%data['summary'].encode('utf-8'))
#             fout.write("</tr>")
#         fout.write("</table>")
#         fout.write("</body>")
#         fout.write("</html>")
#         fout.close()
#===============================================================================
    
    
    
