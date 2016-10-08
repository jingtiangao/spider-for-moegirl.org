#-*- coding: UTF-8 -*-
#===============================================================================
# '''
# Created on 2016年7月8日
# 解析器
# @author: gaochuyang
# '''
#===============================================================================
from bs4 import BeautifulSoup
import re
import urlparse

class  Htmlparser(object):
    
    
    def _get_new__urls(self, page_url, soup):
        new_urls=set()
        #/view/123.htm
        #links1 =soup.find_all('a',href=re.compile(r"/view/\d+\.htm") )
        #links1 =soup.find_all('a',href=re.compile(r"/%*") )
        links1 =soup.find_all('a',href=re.compile(r"/%+") )
        #links2 =soup.find_all('a',href=re.compile(r"/view/\d+\.htm") )
        #links1 =soup.find_all('a')
        #得到所有的词条url
        cot=1
        for link in links1:
            cot=cot+1
            new_url= link['href']
            #要把不完全的url拼接成完全的url
            new_full_url=urlparse.urljoin(page_url,new_url)
            #join方法将page和new拼到了一起
            new_urls.add(new_full_url)
            if cot==12:
                break
            
        return new_urls
            
            
            
    
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        #把url也放到最终的数据中
        res_data['url']= page_url
        
        #<dd class="lemmaWgt-lemmaTitle-title">
        #<h1>Python</h1>

       # title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title")
        title_node = soup.find('h1',id="firstHeading",class_="firstHeading")
        #title_node = title_node.find('h1')
        #得到标题的标签
        res_data['title']=title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">

        #summary_node = soup.find('div',class_="lemma-summary")
        summary_node = soup.find('div',id="mw-content-text",class_="mw-content-ltr")
        summary_node = soup.find_all('p')
        res_data['summary']=""
        for summary in summary_node:
            ss=summary.get_text()
            res_data['summary'] = res_data['summary']+ss
        
        return res_data
    
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8' )
        new_urls = self._get_new__urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)#建立两个本地方法
        return new_urls,new_data
        
    

