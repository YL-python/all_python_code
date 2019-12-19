import os
import requests
from lxml import etree


url_head = 'https://www.wallpapermaiden.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
Xpath_list = '//div[@class="wallpaperBg"]/a/div/img/@src'
max_page = 30


def save_img(img,name):
    img_data = myGet(img)
    with open(name,'wb')as f:
        f.write(img_data)


def findFile(dirs, file):
    flag = False
    for root, dirs, files in os.walk(dirs):
        if files is None:
            continue
        else:
            if file in files:
                flag = True
                break
    return flag


def myGet(url):
    return requests.get(url, headers=headers,timeout=3).content


def main(key):
    url = 'https://www.wallpapermaiden.com/search?term=SSSS&page=XXX'.replace("SSSS",key)
    Seave_path = os.path.join('F:\\图片\\wallpapermaiden', key, "")
    # print(url,Seave_path)
    try:
        os.makedirs(Seave_path)
    except:
        print("创建" + Seave_path + "出问题了")
    for page in range(1,max_page+1):
        page_url = url.replace("XXX",str(page))
        try:
            response = myGet(page_url).decode("utf-8")
        except:
            print("请求网页失败，可能是超时了")
            continue
        xpath_page = etree.HTML(response)
        img_list = xpath_page.xpath(Xpath_list)
        for img_xinxi in img_list:
            img_url = url_head+img_xinxi.replace("-thumb","")
            img_name = img_url.split("/")[-1]
            if findFile(Seave_path,img_name):
                print("图片存在了："+img_name)
            else:
                print("正在下载：" + img_name)
                try:
                    save_img(img_url,Seave_path+img_name)
                except:
                    print("下载图片失败："+img_name)


if __name__ == '__main__':
    # anime girl
    # search = input("搜索：").replace(" ","+")
    search = 'anime girl'.replace(" ","+")
    print(search)
    main(search)
