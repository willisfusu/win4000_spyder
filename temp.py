# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import requests
from lxml import etree
from bs4 import BeautifulSoup as bs


workpath="C:\Work\Image"
def mkwp(pat):
    wp=workpath+"\\" +pat
    if not os.path.exists(wp):
        os.mkdir(wp)
    return wp
def download_imgae(src,path,name):
    url=src
    new_path=path
    resp_content=requests.get(url,headers=headers).content
    index=name
    img_path=new_path+ "\\" + str(index)+".jpg"
    with open(img_path,"wb+") as f:
        f.write(resp_content)
    print("完成图片%d下载"%(index))
    
def get_img_url_list(url):
    base_url=url
    resp_detail=requests.get(base_url,headers=headers)
    soup=bs(resp_detail.content,"lxml")
    li_list2=soup.select("#scroll > li >a >img")
    url_list=[]
    for li in li_list2:
        img_src=li["data-original"]
        img_src=img_src.replace("_130_170","")
        url_list.append(img_src)
    return url_list
    
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        }
url="http://www.win4000.com/meinvtag26_1.html"
html=requests.get(url, headers=headers)
resp=html.content
resp_html=etree.HTML(resp)
li_list=resp_html.xpath(".//div[4]/div/div[3]/div[1]/div[1]/div[2]/div/div/ul/li")
base_url_list=[]
base_title_list=[]
for li in li_list:
    base_url=li.xpath(".//a/@href")
    base_title=li.xpath(".//a/img/@title")
    base_url_list.extend(base_url)
    base_title_list.extend(base_title)
print("已经获取当前页面所有链接")

for url in base_url_list:
    index=base_url_list.index(url)
    base_title=base_title_list[index]
    new_path=mkwp(base_title)
    url_list=get_img_url_list(url)
    print("已经获取第%d个链接池"%(index)) 
    for src in url_list:
        inde=url_list.index(src)
        download_imgae(src,new_path,inde)

       