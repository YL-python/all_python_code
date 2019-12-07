"""

https://wallhaven.cc/search?categories=111&purity=100&atleast=1920x1080&topRange=1M&sorting=toplist&order=desc
参数说明
categories=111   0表示不选择 1表示选择  普通 动漫 人物
purity=100   0表示不选择 1表示选择   sfw(工作时可以安全查看)   sketchy（不纯洁的）  还有一个不清楚
topRange=1M   1M  一个月内    6M 六个月内   1y一年内   1w一个星期以内
sorting=toplist   排行榜   views查看数   favorites收藏
order=desc   降序   asc表示升序
page=wallhaven_spider   页码
atleast=1920x1080  最低分辨率


https://w.wallhaven.cc/full/dg/wallhaven-dgeqoj.jpg   图片连接
https://w.wallhaven.cc/full/名字前两个字母/wallhaven-名称

https://wallhaven.cc/w/dgeqoj   详情连接
https://wallhaven.cc/w/图片名称
"""
import requests
from lxml import etree

url = 'https://wallhaven.cc/search?categories=010&purity=100&topRange=6M&sorting=toplist&order=desc&page=2'
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

r = requests.get(url,headers = head).content.decode('utf-8')

data_x = etree.HTML(r)
data = data_x.xpath('//section[@class="thumb-listing-page"]/ul/li/figure/@data-wallpaper-id')
print(data)
# img_name = [i+'.jpg' for i in data]
# img_url = ["https://w.wallhaven.cc/full/{}/wallhaven-{}.jpg".format(i[0:wallhaven_spider],i) for i in data]


# print(img_url)


MAIN_URL = 'https://wallhaven.cc/search?categories=010&purity=100&atleast=1920x1080&topRange=abcd&sorting=efgh&order=desc&page={}'
a = MAIN_URL.replace("abcd","qwe")

print(a)

# print("111".replace("1","2"))