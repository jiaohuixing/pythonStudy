import requests
from bs4 import BeautifulSoup
import random

def get_agent():
    '''
    模拟header的user-agent字段，
    返回一个随机的user-agent字典类型的键值对
    '''
    agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
    fakeheader = {}
    fakeheader['User-agent'] = agents[random.randint(0, len(agents))]
    return fakeheader

def get_html(url):
    try:
        r = requests.get(url,timeout=30,headers=get_agent())
        r.raise_for_status()
        # r.endcodding = r.apparent_endconding
        r.encoding='utf-8'
        print(r.cookies)
        return r.text
    except:
        return "ERROR"

def parse_html(html):
    soup = BeautifulSoup(html,'html.parser')
    #定义解析规则
    for list in soup.select('#houselist-mod-new .list-item'):
        #输出名称 href
        for ll in list.select('.house-details .houseListTitle'):
            print(ll.get_text(),ll['href'])
        #房子的详细信息，后续进行拆分
        for dd in list.select('.house-details .details-item'):
            print(dd.get_text().strip())

url = 'https://xa.anjuke.com/sale/changanb/p1/#filtersort'

parse_html(get_html(url))