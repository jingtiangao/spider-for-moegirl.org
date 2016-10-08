#-*- coding:UTF-8 -*-
#===============================================================================
# '''
# Created on 2016年7月8日
# url 管理器
# @author: gaochuyang
# '''
#===============================================================================
class  UrlManager(object):
    def __init__(self):
        self.new_urls = set()#未爬取的url
        self.old_urls = set()#爬过的url
    #向管理器中添加一个url
    def add_new_url(self,url):
        if url is None:
            return 
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url) 
            
            
        
    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
    def has_new_url(self):
        return len(self.new_urls)!=0

    
    def get_new_url(self):
        new_urls = self.new_urls.pop()#pop方法会获取一个url并移除它
        self.old_urls.add(new_urls)
        return new_urls

    
  
    
    
    
    
    
    
    
    
    