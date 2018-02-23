#-*- coding:UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_html_text(url):
    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebK\
        it/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
    }
    req = requests.get(url,headers = headers)
    return req.text

def get_all_inf(html_text,list1):
    soup = BeautifulSoup(html_text,'html5lib')
    inf = soup.select('.list-videos .item a')
    favorable = soup.select('.list-videos .item a .rating.positive')
    time = soup.select('.list-videos .item a .duration')
    for title,addr,fav,tm in zip(inf,inf,favorable,time):
        inf_oo = {
            '标题':title['title'],
            '时长':tm.text,
            '好评率':fav.text,
            '链接':addr['href']
        }
        list1.append(inf_oo)
    return list1


def get_excel(inf_list):
    data = pd.DataFrame(inf_list)
    data.to_excel('OhMyGod.xlsx',sheet_name='推荐')

def main():
    one = "http://www.kedou07.com/latest-updates/{}/"
    inf_list = list()
    for x in range(2,3):
        url = one.format(x)
        html = get_html_text(url)
        get_all_inf(html,inf_list)
        get_excel(inf_list)
main()





