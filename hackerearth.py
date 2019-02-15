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
    
