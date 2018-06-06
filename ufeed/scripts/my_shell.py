# -*- coding: utf-8 -*-
import re
import urllib3
import datetime
from bs4 import BeautifulSoup
from login.models import Userdata, Crawldata
import requests

#/Users/LeeTaeHun/DjangoProjects/myvenv/bin/python manage.py runscript -v2 my_shell
#/Users/LeeTaeHun/DjangoProjects/myvenv/bin/python /Users/LeeTaeHun/DjangoProjects/YOUFEED/manage.py runscript -v2 my_shell
#* * * * * (sleep 30 ; /Users/LeeTaeHun/DjangoProjects/myvenv/bin/python /Users/LeeTaeHun/DjangoProjects/YOUFEED/manage.py runscript -v2 my_shell)
#http://www.kaist.ac.kr/_prog/_board/?code=kaist_student&site_dvs_cd=kr&menu_dvs_cd=0603&site_dvs_cd=kr&menu_dvs_cd=0603
#http://www.kaist.ac.kr/_prog/_board/?mode=V&no=80761&code=kaist_student&site_dvs_cd=kr&menu_dvs_cd=0603&skey=&sval=&site_dvs=&GotoPage=

def run():

    userdatas = Userdata.objects.all()
    for d in userdatas:
        user_key = d.key
        user_url = d.url
        user = d.user

        print(user_url)

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        http = urllib3.PoolManager()
        html = http.request('GET', user_url)
        soup = BeautifulSoup(html.data, "html.parser")
        bodyTag = soup.body

        if bodyTag == None:
            print("bodyTag is Null, " + user_url)
            print("-------------")
            continue

        for s in bodyTag('script'):
            s.extract()

        result_title = bodyTag.findAll(text=re.compile(user_key))
        if len(result_title) == 0:
            print("result_title is none PASS")
            print("-------------")
            continue
        else:

            result_href = bodyTag.find(text=re.compile(user_key)).parent
            if result_href.get('href') == None:
                result_href = bodyTag.find(text=re.compile(user_key)).parent.parent
                if result_href.get('href') == None:
                    result_href = bodyTag.find(text=re.compile(user_key)).parent.parent.parent
                    if result_href.get('href') == None:
                        result_href = bodyTag.find(text=re.compile(user_key)).parent.parent.parent.parent


            result_href = result_href.get('href')
            if result_href == None:
                print("href is none PASS")
                continue

            result_url = getResultUrl(user_url, result_href)


            # DB check
            count = hasCrawlData(user, result_title[0].strip(), result_url)
            if count == 0:
                print("DB insert")
                now = datetime.datetime.now()
                nowDatetime = now.strftime('%Y-%m-%d %H:%M')
                Crawldata.objects.create(user=user, title=result_title[0].strip(), url=result_url, reg_date=nowDatetime)
                header = {'Content-Type':'application/json', 'Authorization':'key=AAAApnMgDVI:APA91bEHuLeHP4y80Ksn5ofyL1307Id_GumdSt9TzZetcse-ZAbuIlVP-uzM0_Sv-ZmCPT03Z4ukztD9TRdVHuGpXsu7SFhNbkvv0trybby3CzHLO_mepw5S9LzUtnathLazZMbWW_Cd'}
                data = {"data": {        "message": {"title": result_title[0].strip(), "contents": result_url, "imgurl":"http://work.kr/data/icon.png", "link": ""}}, "to": "/topics/notice" }
                requests.post('http://fcm.googleapis.com/fcm/send', headers=header, json=data)
            else:
                print("DB Already insert ")

            print("-------------")


def hasCrawlData(user, title, url):
    crawlData = Crawldata.objects.all()
    crawlData = crawlData.filter(user=user, title=title, url=url)
    # print(len(crawlData))
    # for model_instance in crawlData:
    #     print(model_instance)  # 화면에 출력할 때 DB에 쿼리 (lazy)
    return len(crawlData)

def getResultUrl(user_url, result_href):
    result_url = ''
    if result_href[0:1] == '/':
        result_url = urllib3.util.get_host(user_url)[0] + "://" + urllib3.util.get_host(user_url)[1] + result_href
    elif result_href[0:1] == '.':
        result_url = urllib3.util.split_first(user_url, '?')[0] + result_href
    elif result_href[0:4] == 'http':
        result_url = result_href
    else:
        result_url = urllib3.util.get_host(user_url)[0] + "://" + urllib3.util.get_host(user_url)[1] + '/' + result_href

    #print("result_url = " + result_url)
    return result_url