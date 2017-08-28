import requests
import  lxml
import html5lib
from bs4 import BeautifulSoup
import  random
from selenium import  webdriver


url ='https://xa.anjuke.com/sale/changanb/?from=SearchBar'
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
def get_proxy():
    '''
    简答模拟代理池
    返回一个字典类型的键值对，
    '''
    proxy = ["http://116.211.143.11:80",
             "http://183.1.86.235:8118",
             "http://183.32.88.244:808",
             "http://121.40.42.35:9999",
             "http://222.94.148.210:808"]
    fakepxs = {}
    fakepxs['http'] = proxy[random.randint(0, len(proxy))]

    return fakepxs
def get_html(url):
    try:
        r = requests.get(url, timeout=30,headers=get_agent())
        print(r.status_code)
        r.raise_for_status()
        # 这里我们知道百度贴吧的编码是utf-8，所以手动设置的。爬去其他的页面时建议使用：
        # r.endcodding = r.apparent_endconding
        r.encoding = 'utf-8'
        return r.text
    except:
        return " ERROR "
#todo 使用beautifulsoad解析网页，爬取对应的信息；
#todo  学习phantom
#print(get_html(url))
def parse_html(html):
    # soup = BeautifulSoup(html,'lxml')
    soup = BeautifulSoup(html,'html5lib')
    liTags =soup.find(class_='list-item')
    #print(liTags.select('.house-details .houseListTitle')[0].get('href'))
    #house-title
    print(liTags.select('.details-item')[0].select('span')[0].get_text())

# parse_html(get_html(url))
def get_content_by_selenium(url):
    browser = webdriver.PhantomJS()
    browser.get(url)
    browser.implicitly_wait(3)
    houseLists = browser.find_element_by_class_name('houselist-mod houselist-mod-new').find_element_by_tag_name('img').get_attribute('src')
    print(houseLists)
    #print()

get_content_by_selenium(url);

