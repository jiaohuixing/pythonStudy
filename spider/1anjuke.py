import requests
from bs4 import BeautifulSoup
import random,time


url = 'https://xa.anjuke.com/sale/changanb/p1/#filtersort'
session=requests.session()
houseLists=[]
global next_url
global spider
spider = True
next_url = url
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
        r = session.get(url,timeout=30,headers=get_agent())
        r.raise_for_status()
        # r.endcodding = r.apparent_endconding
        r.encoding='utf-8'
        #print(r.text)
        return r.text
    except:
        return "ERROR"

def parse_html(html):
    soup = BeautifulSoup(html,'html.parser')
    #解析下一页
    try:
        next_url=soup.select('.multi-page .aNxt')[0].attrs['href']
        # print('开始解析：'+ next_url)
    except Exception as e:
        print('异常了：'+ e)
        spider = False

    if (not spider):
        return
    #定义解析规则
    for list in soup.select('#houselist-mod-new .list-item'):
        #输出名称 href
        house = []
        for ll in list.select('.house-details .houseListTitle'):
            #print(ll.get_text(),ll['href'])
            house.append(ll.get_text().strip())
            house.append(ll['href'])
        #房子的详细信息，后续进行拆分
        for dd in list.select('.house-details .details-item'):
            #print(dd.get_text().strip())
            #可以使用geocoding反查经度纬度
            house.append(dd.get_text().replace('\ue147','').replace('\xa0','').replace('\n','').strip())
        # print(house)
        #房子tag 如果没有tags-bottom,则用 details-bottom
        try:
            for tt in list.select('div.tags-bottom'):
                house.append(tt.get_text().strip())
        except Exception as e:
            print(e)
            try:
                for tt in list.select('.details-item details-bottom'):
                    house.append(tt.get_text().strip())
            except:
                house.append('null')
        #房子价格 pro-price
        for pp in list.select('div.pro-price'):
            house.append(pp.get_text().strip())

        houseLists.append(house)
    print('共爬取{}条'.format(len(houseLists)))
    # for house in houseLists:
    #     print(house[0])

def main_spider():
    while (spider):
        print('开始解析：' + next_url)
        parse_html(get_html(next_url))
        time.sleep(3)

main_spider()