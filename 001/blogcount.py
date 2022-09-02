#coding=utf-8
import urllib
from urllib.request import urlopen
from distutils.filelist import findall
from bs4 import BeautifulSoup
import yaml

def getLinkList():
    f = open('/www/wwwroot/project/001/link.yml', 'r')
    ystr = f.read()

    ymllist = yaml.load(ystr, Loader=yaml.FullLoader)
    for item in ymllist:
        for link in item['link_list']:
            try:
                count = getCount(link['link'])
                print(link['name']+ ' ' + count + '：' + link['link'])
            except:
                count = '不是btf，无法查找'
    

def getCount(site):
    if not site.endswith('/'):
        site += '/'
    # html
    headers = {'user-agent':'mozilla/5.0'}
    add = urllib.request.Request(url=site,headers=headers)
    htmlr = urllib.request.urlopen(url=add,timeout=10)
    html = htmlr.read()
    soup = BeautifulSoup(html, "html.parser")

    # print(html)
    # postcount = soup.find('div', class_='length-num').get_text()
    webinfo = soup.find('div', class_='webinfo-item')
    webinfopostcount = webinfo.find('div', class_='item-count').get_text()

    if webinfopostcount:
        return webinfopostcount
    else:
        return "找不到"

getLinkList()