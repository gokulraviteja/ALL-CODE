import os
from bs4 import BeautifulSoup
import urllib.request
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"
opener = AppURLopener()
response = opener.open('https://www.codechef.com/contests')
soup = BeautifulSoup(response.read(),'html.parser' )
ans=str(soup.prettify)
t=0
ans=ans.split("Future Contests")
ans=ans[1]
ans=ans.split("Past Contests")
ans=ans[0].split('tbody')
ans=ans[1]
arr=(ans.split('\n'))

name=[]
starttime=[]
startdate=[]
endtime=[]
enddate=[]
link=[]
st="https://www.codechef.com/"

for i in arr:
    if('tr>' in i):
        continue
    elif('href' in i):
        ss=i.split('"')
        link.append(st+ss[1])
        ss=ss[2][1:]
        k=ss.find('</a')
        ss=ss[:k]
        name.append(ss)
    elif('start_date' in i):
        ss=i.split(' <br/> ')
        p1=ss[1]
        k=p1.find('</td>')
        p1=p1[:k]
        starttime.append(p1)
        p2=ss[0]
        k=p2.find('>')
        p2=p2[k+1:]
        
        startdate.append(p2)
    elif('end_date' in i):
        ss=i.split(' <br/> ')
        p1=ss[1]
        k=p1.find('</td>')
        p1=p1[:k]
        endtime.append(p1)
        p2=ss[0]
        k=p2.find('>')
        p2=p2[k+1:]
        enddate.append(p2)

l=len(name)
for i in range(l):
    print(name[i])
    print(startdate[i],starttime[i])
    print(enddate[i],endtime[i])
    print(link[i])
    print()
    print()




import requests
from bs4 import BeautifulSoup
url = "https://codeforces.com/contests"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify)
st=str(soup.prettify)
st=st.split("Current or upcoming")
st=st[1]
st=st.split("script")
st=st[0]
st=st.split("table")
st=st[1]
st=st.split('<th style="width:15em;"> </th>')
st=st[1]
st=st.split('\n')
for i in st:
    i=i.strip()

name1=[]
date1=[]
time1=[]
period=[]





for i in st:
    if("</td>" in i and len(i)>5):
        name1.append(i[:-9])
    elif("data-locale" in i):
        p=i
        p=p.split('data-locale')
        p=p[1]
        p=p[6:]
        p=p.split("</span>")
        p=p[0]
        p=p.split()
        date1.append(p[0])
        time1.append(p[1])
    else:
        p=i.strip()
        if(len(p)==5 and ':' in i):
            period.append(p)
        
        
cc=name1.count('')
for i in range(cc):
    name1.remove('')
    

l=len(period)
for i in range(l):
    print(name1[i])
    print(date1[i])
    print(time1[i])
    print(period[i])
    print()
    print()







import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

#hackerearth get upcoming

driver=webdriver.Chrome("C:\\Users\\bellapukonda\\Desktop\\auto\\chromedriver.exe")
driver.get("https://www.hackerearth.com/challenges/")

res=driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

soup=BeautifulSoup(res,"html.parser")
box=soup.find('div',{'class':'upcoming challenge-list'})
all_con=box.find_all('div',{'class':'challenge-card-modern'})
for con in all_con:
    c_type=con.find('div',{'class':'challenge-type'}).text
    name=con.find('div',{'class':'challenge-name'}).text
    date=con.find('div',{'class':'date'}).text
    print(name,date)
    






