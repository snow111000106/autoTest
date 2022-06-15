#coding=utf-8
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os,re
from urllib.request import quote

def headers(referer):
    headers = {
        'Host': 'api.map.baidu.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                       ' Chrome/77.0.3865.120 Safari/537.36',
        'Referer': '{0}'.format(referer)
    }
    return headers

def each_chapter():
    url = 'https://zhaopin.baidu.com/quanzhi'
    city = '厦门'
    city_sug = quote(city)
    qu = '厦门测试工程师'
    qu_sug = quote(qu)
    all_url = url + '?query='+qu_sug + '&city_sug='+city_sug +'&zp_fr=aladdin-5463-zp_exact_new'
    print(all_url)
    res = requests.get(url, headers(all_url))
    res.encoding = 'utf-8'
    sel = BeautifulSoup(res.text, 'lxml')
    print(sel)

if __name__ == '__main__':
    each_chapter()
