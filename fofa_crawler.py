import json

from lxml import etree
import requests
from lxml.doctestcompare import strip
import fofa_config


class Crawler:
    def __init__(self):
        fofa_config.config_init()
        self.headers=fofa_config.headers
        self.url=fofa_config.url

    #爬虫模式爬虫
    def crawler_request(self,i,keyeord,full):
        if i==1:
            self.url=fofa_config.url
            self.url = self.url +str(keyeord) + "&page="
        if full:
            url = self.url + str(i)+"&page_size=10"+'&full=true'
        else:
            url = self.url + str(i)+"&page_size=10"
        # print(url)
        self.htmlpage=requests.get(url,headers=self.headers)
        self.pagecontent=etree.HTML(self.htmlpage.text)
        self.crawler_handle()
        # print(self.overview)

        return self.overview

    #爬虫模式爬取的数据处理函数
    def crawler_handle(self):
        self.overview_url=self.pagecontent.xpath('//body//div[@class="hsxa-fl hsxa-meta-data-list-lv1-lf"]//span[@class="hsxa-host"]//a/@href')
        self.overview_title =self.pagecontent.xpath('//body//div[@class="hsxa-meta-data-list-main-left hsxa-fl"]//p[@class="hsxa-two-line"]/text()')
        self.overview_ip=self.pagecontent.xpath('//body//div[@class="hsxa-clearfix hsxa-pos-rel"]/div[@class="hsxa-meta-data-list-main-left hsxa-fl"]/p[2]/a[1]/text()')
        self.overview_port=self.pagecontent.xpath('//body//div[@class="hsxa-clearfix hsxa-meta-data-list-lv1"]//div[2]//a[@class="hsxa-port"]/text()')
        #overview_domain =self.pagecontent.xpath()
        #overview_serve =self.pagecontent.xpath('//body//div[@class="el-checkbox-group"]//div[@class="hsxa-clearfix hsxa-pos-rel"]/div[@class="hsxa-meta-data-list-main-left hsxa-fl"]/p[@class="hsxa-list-span-wrap"]/a[@class="hsxa-list-span-item"]/span[@class="el-tooltip hsxa-list-span hsxa-list-span-sm"]/text()')
        self.overview_all=[self.overview_url,self.overview_title,self.overview_ip,self.overview_port]
        self.overview = []
        for h in range(0,len(self.overview_url)):
            self.all=[]
            for l in range(0,4):
                self.all.append(strip(self.overview_all[l][h]))

            self.overview.append(self.all)

    #api模式爬虫及数据处理函数
    def api_fofa(self,count,fields,keyeord):
        self.count = count
        self.fofa_email = fofa_config.fofa_email
        self.fofa_key =  fofa_config.fofa_key
        self.fields = fields
        self.query = keyeord
        self.r=requests.get(url="https://fofa.info/api/v1/search/all?email={}&key={}&fields={}&qbase64={}&size={}".format(self.fofa_email ,self.fofa_key ,self.fields, self.query, self.count))
        # print("https://fofa.info/api/v1/search/all?email={}&key={}&fields={}&qbase64={}&size={}".format(self.fofa_email ,self.fofa_key ,self.fields, self.query, self.count))
        self.data = json.loads(self.r.text.encode("GBK", 'ignore').decode('GBK'))
        self.data = self.data['results']

        return self.data



crawler=Crawler()
