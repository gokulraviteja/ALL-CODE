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
