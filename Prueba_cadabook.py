from bs4 import BeautifulSoup
import requests
import pandas as pd

res=requests.get("http://books.toscrape.com/").text
soup=BeautifulSoup(res,'html.parser')
#Get the total page count
pagecount=soup.select_one('.current').text.split('of')[-1].strip()

title=[]
ratings=[]
cost=[]
for page in range(1,int(pagecount)+1):
    finalurl="http://books.toscrape.com/catalogue/page-{}.html".format(page)
    res=requests.get(finalurl).text
    soup=BeautifulSoup(res,'html.parser')
    for t,r,c in zip(soup.select('.image_container >a>img'),soup.select('p.star-rating'),soup.select('.image_container >a')):
        title.append(t['alt'])
        ratings.append(r.attrs['class'][-1])
        cost.append(c['href'])

df = pd.DataFrame({"Title":title,"Ratings":ratings,"Cost":cost})
print(df)
df.to_csv('Titlebooks.csv')


---------------------------------------
---------------------------------------


from bs4 import BeautifulSoup
import requests
import pandas as pd

res=requests.get("http://books.toscrape.com/").text
soup=BeautifulSoup(res,'html.parser')
#Get the total page count
pagecount=soup.select_one('.current').text.split('of')[-1].strip()

title=[]
ratings=[]
cost=[]
for page in range(1,int(pagecount)+1):
    finalurl="http://books.toscrape.com/catalogue/page-{}.html".format(page)
    res=requests.get(finalurl).text
    soup=BeautifulSoup(res,'html.parser')
for c in (soup.select('.image_container >a')):
    title.append(c['href'])
    for inter in title :
        url_lib = "http://books.toscrape.com/catalogue/{}".format(inter)   
        res2=requests.get(url_lib).text 
        soup2=BeautifulSoup(res2,'html.parser')
        results = soup2.findAll( "div", {"class": "content"}) 
    for item in results:
                             
                
        products = {
                     
            'book_href' : item.find('p').text,
                     }
ratings.append( products)
df = pd.DataFrame({"Title":title,"Ratings":ratings,"Cost":cost})
print(df)
df.to_csv('Titlebooks.csv')
