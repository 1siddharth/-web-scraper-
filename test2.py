import requests 
from bs4 import BeautifulSoup
import time
import sys
import pandas as pd
from time import gmtime, strftime ,localtime

storechange =[]
names=[]
def dataready():
    
    changes=[]
    percentChanges=[]
    marketCaps=[]
    lastprice=[]


    CryptoCurrenciesUrl = "https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9"
    r= requests.get(CryptoCurrenciesUrl)
    data=r.text
    soup=BeautifulSoup(data)
    print("ch1") 
    counter = 4
    for i in range(40, 404, 14):
       #print("ch2")
        for row in soup.find_all('tr'):
            for srow in row.find_all('td',attrs ={"class":"brdrgtgry", "width":"24%"}):
                for sroww in srow.find_all('a',{"class":"bl_12"}):
                   # print(sroww.text)
                    names.append(sroww.text)
                    
            templist =[]
            for hi in row.find_all('td', attrs={"align":"right","class":"brdrgtgry"}):

                aa=hi.text
                #print(aa)
                templist.append(float(aa.replace(",","")))
           # print("#############################################################")
            if len(templist)==4:
                lastprice.append(templist[0])
                changes.append(templist[1])
                percentChanges.append(templist[2])
                marketCaps.append(templist[3])
                templist =[]
             #   print("#")
    storechange.append([percentChanges,[time.time()]])
    pd.DataFrame({"Names": names, "Prices": lastprice, "Change": changes, "% Change": percentChanges})
#firsttime =storechange[0][0]
def alertsys(names):
    print("ji")
    firsttime =storechange[0][1][0]
    firstdata =storechange[0][0]
   # print(firsttime)
    
    #print(storechange[0][1])
    for i in storechange:
       # print(i[1][0]) #printing all the time
        sot = i[1][0]
      #  print(sot)
        print("diff of time ")
        kk =int(sot)-int(firsttime)
        print(kk)
 
        if((int(sot)-int(firsttime)) > 2):
            l1 = [i][0][0]
           # print(l1)
            l2 =firstdata
            firsttime = i[1][0]
            firstdata = l1
           # print("here")
            for ii in range(len(l2)):
                
                if((l2[ii] - l1[ii]) > 2):
                    print("stock of company"+names[ii]+"changed over by 2% , changing by "+str((l2[ii] - l1[ii])))
          
def turner():
    dif = 0
    mini = 20
    sec = mini * 60
    startt= time.time()
    while(dif<=sec):
        dataready()
        time.sleep(30)
        
        dif = time.time() -startt
        print(dif)
        print("in loop")
    print("out of loop")    
    
def runner():   
    tuner() 
    alertsys(names)
    
def main():
    aa=strftime("%a",localtime())
    print(type(aa))
    if (aa != 'sat' and aa != 'sun'):
        
        ti = int(strftime("%H", localtime()))
        if(ti >=9 and ti < 16):
            mi = int(strftime("%M", localtime()))
            if (ti == 9 and mi < 15):
                
                print("market about to start")
                sys.exit("-1")
            elif(ti==15 and mi >30):
                
                print("market closed now")
                sys.exit("-1")
            else:
                print("procced")
                runner()
        else:
            
            print("Market remains closed for this time")
            sys.exit("-1")
    else:
        
        print("Markets remains closed today")
        sys.exit("-1")
if __name__ == "__main__":
    main()

