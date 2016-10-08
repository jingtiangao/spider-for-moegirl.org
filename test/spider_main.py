#-*- coding: UTF-8 -*-
#===============================================================================
# '''
# Created on 2016年7月8日
#  爬虫调度程序
# @author: gaochuyang
# '''
#===============================================================================

from test import url_manager, html_downloader, html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.Htmlparser()
        self.outputer = html_outputer.HtmlOutputer()
        
    def craw(self,root_url):#调度程序
        count = 1 #用count记录当前爬取的是第几个Url
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            #百度百科有的网页已经无法访问，需要加入异常处理
            try:
                new_url = self.urls.get_new_url()
                print'craw %d : %s' %(count,new_url) 
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
               
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 2:
                    break
                count =count +1
            except:
                print 'craw failed'   
        self.outputer.output_html()
if __name__=="__main__":
    #root_url = "http://baike.baidu.com/view/21087.htm"
    #root_url = "http://baike.baidu.com/subview/88845/8261070.htm"
    root_url="https://zh.moegirl.org/Fate/stay_night"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    
            
                
