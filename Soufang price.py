
# coding: utf-8

# In[1]:

import requests
from bs4 import BeautifulSoup
head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

res=requests.get("http://zu.fang.com/house/g21-s31-kw%b9%dc%d7%af%ce%f7%c0%ef/",headers=head)
soup=BeautifulSoup(res.text,"lxml")
x=0
for x in (0,1,2,3,4,5,6,7,8,9):
    
    print soup.select('.floatr')[x].text.strip()
x+=1


# In[2]:




# In[ ]:



