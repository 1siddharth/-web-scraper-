import requests
from bs4 import BeautifulSoup
from newspaper import Article
import pandas as pd
linklist =[]
filist =[]

def mainclass():
    url  = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen/"
    code=requests.get(url)
    soup = BeautifulSoup(code.text, 'html5lib')
    soup.prettify()
    hel = soup.find_all("article" ,{"class": "MQsxIb xTewfe tXImLc R7GTQ keNKEd keNKEd dIehj EjqUne"})
    a=0
    for aa in hel:
        ok2 = aa.find_all("a",{"class": "DY5T1d"})
        for tag in ok2:
            link = tag.get('href',None)
            if link is not None:
                str(link)
                link = "https://news.google.com"+ link[1:]
                if a>1:
                    if (len(linklist[a-1]) != len(link)):
                        linklist.append(link)
                        a+=1
                else:
                    linklist.append(link)
                    a+=1
 

        
linkl =[]
titlel =[]
suml =[]
datel =[]

print("here")
def extraction():
    i=0
    for ok in linklist:
        code=requests.get(ok)
        if code.status_code == 200 and i>8:
            filist.append(ok)
            toi_article = Article(ok, language="en")
            toi_article.download()
            toi_article.parse()
            toi_article.nlp()
            linkl.append(ok)
            titlel.append(toi_article.title)
            suml.append(toi_article.summary)
           
            datel.append(toi_article.publish_date)
            print("done "+ str(i))
            i+=1
        else:
            break
        
            
def tableform():
    print("here")
    df = pd.DataFrame({'link':linkl,'title':titlel,'summary':suml, 'datetime':datel})
    print("waiting foe tbl")
    df
    print(df)
li = ["hi","hello"]
# li is list here pleas make a list to seach
def searchf(li):
    for i in li:
        
        for se in titlel:
            
            if(se.find(i) != -1):
                print(se)


    
mainclass()
extraction()
tableform()
searchf(li)
     
    
    
    
    
    