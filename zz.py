#/usr/bin/python
from urllib import request
from lxml import etree
from selenium import webdriver
import time

# 京东手机商品页面
url = "http://item.jd.com/1312640.html"

# 下面的xslt是通过集搜客的谋数台图形界面自动生成的
xslt_root = etree.XML("""\
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" >
<xsl:template match="/">
<商品>
<xsl:apply-templates select="//*[@id='itemInfo' and count(.//*[@id='summary-price']/div[position()=2]/strong/text())>0 and count(.//*[@id='name']/h1/text())>0]" mode="商品"/>
</商品>
</xsl:template>

<xsl:template match="//*[@id='itemInfo' and count(.//*[@id='summary-price']/div[position()=2]/strong/text())>0 and count(.//*[@id='name']/h1/text())>0]" mode="商品">
<item>
<价格>
<xsl:value-of select="*//*[@id='summary-price']/div[position()=2]/strong/text()"/>
<xsl:value-of select="*[@id='summary-price']/div[position()=2]/strong/text()"/>
<xsl:if test="@id='summary-price'">
<xsl:value-of select="div[position()=2]/strong/text()"/>
</xsl:if>
</价格>
<名称>
<xsl:value-of select="*//*[@id='name']/h1/text()"/>
<xsl:value-of select="*[@id='name']/h1/text()"/>
<xsl:if test="@id='name'">
<xsl:value-of select="h1/text()"/>
</xsl:if>
</名称>
</item>
</xsl:template>
</xsl:stylesheet>""")

# 使用webdriver.PhantomJS
browser = webdriver.PhantomJS(executable_path='C:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
browser.get(url)
time.sleep(3)

transform = etree.XSLT(xslt_root)

# 执行js得到整个dom
html = browser.execute_script("return document.documentElement.outerHTML")
doc = etree.HTML(html)
# 用xslt从dom中提取需要的字段
result_tree = transform(doc)
print(result_tree)

import codecs
import re
import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
import random
import matplotlib.pyplot as plt


# url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=543803699362&sellerId=1652490016&order=3&currentPage='
def get_ip_list(url_ip, headers_ip):
    web_data = requests.get(url_ip, headers=headers_ip)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[0].text + ':' + tds[1].text)
        # print("ip_list",ip_list)
    return ip_list
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    # print("proxies",proxies)
    return proxies


def get_maxpage(url):
    ip_list = get_ip_list(url_ip, headers_ip=headers_ip)
    proxies = get_random_ip(ip_list)
    r = requests.get(url=url,proxies=proxies)
    html = r.content.decode('gb2312', 'ignore')
    html = str(html)
    file = codecs.open("tmallpage.txt", "w")
    file.write(html)
    file.close()
    maxpage = re.findall(r'"lastPage":(.*?),', html)
    print("maxpage:", maxpage)
    if maxpage==['0']:
        print("这个产品没有用户进行评论")
        return 0
    else:
        sumpage = maxpage.pop()
        print("sumpage",sumpage)
        return sumpage

def crawlpage(url,sumpage):
    for i in range(int(sumpage)):
        i = str(i)
        print(i)
        url1 = url + i
        print('url1:', url1)
        r = requests.get(url=url1)
        html = r.content.decode('gb2312', 'ignore')
        html = str(html)
        file = codecs.open("tmallpage.txt", "w")
        file.write(html)
        file.close()
        print("当前抓取页面:", url1, "状态:", r)

        # 写入文件
        html = str(html)
        file = codecs.open("page.txt", "w")
        file.write(html)
        file.close()

        content_1 = re.findall(r',"rateContent":(.*?)",', html)
        print("len:", len(content_1))
        print("Content:", content_1)

        nickname = re.findall(r',"displayUserNick":(.*?),', html)
        print("len:", len(nickname))
        print("UserNickname:", nickname)

        tamllSweetLevel = re.findall(r',"tamllSweetLevel":(.*?),', html)
        print("len:", len(tamllSweetLevel))
        print("tamllSweetLevel:", tamllSweetLevel)

        referenceTime = re.findall(r',"rateDate":(.*?),', html)
        print("len:", len(referenceTime))
        print("referenceTime:", referenceTime)

        table = pd.DataFrame({"referenceTime": referenceTime, "tamllSweetLevel": tamllSweetLevel,
                              'nickname': nickname, 'content_1': content_1,
                              })
        table = table.set_index('referenceTime')
        table.head()
        print("存入csv....")
        table.to_csv(itemId+'jd_table_textmaxpage.csv', mode='a', header=False)
        print("存完....")


        mobile_t=table.loc[table["mobile"] == "true"]
        #在table中筛选没有使用移动设备的条目并创建新表
        mobile_f=table.loc[table["mobile"] == "false"]
        #按月汇总使用移动设备的数据
        mobile_t_m=mobile_t.resample('M',how=len)
        #按月汇总不使用移动设备的数据
        mobile_f_m=mobile_f.resample('M',how=len)
        #提取使用移动设备的按月汇总nickname
        mobile_y=mobile_t_m['nickname']
        #提取没有使用移动设备的按月汇总nickname
        mobile_n=mobile_f_m['nickname']

        plt.subplot(2, 1, 1)
        plt.plot(mobile_y,'go',mobile_y,'g-',color='#99CC01',linewidth=3,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
        plt.ylabel('移动设备评论数量')
        plt.title('PC&mobile')
        plt.subplot(2, 1, 2)
        plt.plot(mobile_n,'go',mobile_n,'g-',color='#99CC01',linewidth=3,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
        plt.xlabel('month')
        plt.ylabel('PC')
        plt.show()


if __name__=='__main__':
    startime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("startime is:", startime)
    url0='https://rate.tmall.com/list_detail_rate.htm?itemId='
    url2='&sellerId=1652490016&order=3&currentPage='
    itemId ='543756148809'
    url = url0+itemId+url2
    print("url==========",url)

    url_ip='http://www.kuaidaili.com'
    headers_ip = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
    }

    sumpage=get_maxpage(url)
    crawlpage(url,sumpage)
    print("done......")
    donetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("endtime is:", donetime)