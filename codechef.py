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