__author__ = 'Administrator'
# _*_ coding:utf-8 _*_
from bs4 import BeautifulSoup
import re
import os
from  urllib import request
class MySpider(object):
    max_last=1
    max_now=1

    def __init__(self,url,name):
        self.url=url
        self.name=name

    def begin(self):
        mylist=[]
        for k in range(0,26):
            start=5
            req=request.Request(self.url+str(k)+'.html')
            result=request.urlopen(req)
            soup=BeautifulSoup(result.read().decode('gbk'))
            tags=soup('a')
            save=True
            for x in tags:
                ss=re.search('http:.*meinv.*html',str(x))

                if not ss==None:
                    if save:
                        mylist.append(ss.group())
                        save=False
                    else:
                        save=True

        else:
            print('begin stage 2')
        #start download every url in mylist
        i=0
        for uu in mylist:

            imgs=[]
            ll=getResource(uu)

            title=re.search('href="\d+.*html',ll[:50])
            link=uu
            result=getResource(link)
            while(title!=None):
                tts=re.findall('http:.*?jpg',result)
                for kk in tts:
                    imgs.append(kk)

                l=re.search('http://www.5442.com/meinv/.*/',link)
                temp=title.group()
                k=l.group()+temp[6:]
                print(k)
                result=getResource(k)
                title=re.search('href="\d+.*html',result[:50])
                link=k



            else:
                img_link=re.findall('http:.*jpg?',result)
                for x in img_link:
                    imgs.append(str(x))
            print('begin download img')
            self.download(imgs,i)

            i+=1

    def download(self,lists,i):

        j=0
        if os.path.exists('I:'+os.sep+'rosis'+os.sep+str(i)):
            os.remove('I:'+os.sep+'rosis'+os.sep+str(i))
        else:
            os.makedirs('I:'+os.sep+'rosis'+os.sep+str(i))

        for url in lists[:-1]:
            try:
                with open('I:'+os.sep+'rosis'+os.sep+str(i)+os.sep+str(j)+'.jpg','wb') as f:
                    print(str(url))
                    req=request.Request(url)
                    requ=request.urlopen(req)
                    f.write(requ.read())
                    j+=1
            except:
                pass



def getResource(uu):
    lala=request.Request(uu)
    rere=request.urlopen(lala)
    sou=BeautifulSoup(rere.read().decode('gbk'))
    tags=sou.find(id='contents')
    ll=''
    for k in tags:
        ll+=str(k)
    return ll

app=MySpider('http://www.5442.com/tag/rosi/','heheh')

app.begin()

