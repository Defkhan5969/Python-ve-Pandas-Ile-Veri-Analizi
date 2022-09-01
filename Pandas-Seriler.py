import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
myList = [1,1,3,4,5,6]
myStrList = ["a","b","c","d","d","a"] #Tekrarlayan eleman içerebilir
result = pd.Series(myList)


seri= pd.Series(myList,index=myStrList)
result= seri[1] #İndeksi ara dedik


dogsDict = {"rex":"golden","alpha":"dogs","lupo":"poweranian"}

result = pd.Series(dogsDict)

#ATTRIBUTES

myList = [1,1,3,4,5,6]
seri = pd.Series(myList)
result = seri.T
result = seri.dtype
result = seri.is_unique # Değerlerde tekrarlayan eleman var mı? 
result = seri.size

#METHODS

result =  seri.head()
result =  seri.describe() #Serinin ortalaması std'si min değer maks değer vs
result =  seri.head()
result =  seri.max()
result =  seri.min()

pd.Series(data=myList,copy=True)

calisanlar = ["ahmet","deniz","selin","cem","efe"]
maaslar = [4000,5000,4500,3500,4000]

result = seri = pd.Series(data=calisanlar,index=maaslar)

#CSV OKUMA


kriptoSeri = pd.read_csv("siyaset.csv")

result = kriptoSeri.head()

günler = [None,"Sali","Carsamba","Persembe","Cuma","Cumartesi","Pazar"]

günlerSon= []
havaDurumu = []
for i in range(0,100):
    havaDurumu.append(np.random.randint(0,40))
    günlerSon.append(günler[i%len(günler)])

dictionary = {"günler":günlerSon}
dataFrame = pd.DataFrame(dictionary)#Böyle de eklersin
dataFrame["hava durumu"] = havaDurumu#Böyle de eklersin

dataFrame.to_csv("Son Hali.csv",index_label=False)
 
result = seri= pd.read_csv("Son Hali.csv",usecols=["hava durumu"],squeeze=True)#Seri Yaptık

result = seri.describe()


#PYTHON BUILT-IN FUNCTIONS-GÖMÜLÜ FONKSİYONLAR
result = len(seri)
result = dict(seri)
result = type(seri)


#SORTING SERIES
result = sorted(seri,reverse=True)  # gömülü sıralam için
result = seri.sort_values(ascending=True,inplace=True) # gömülü değil data frame döndüdür
result = seri

result = seri.sort_index()

#SIMILATIRIES BETWEEN AND PYTHON LIST

myList= [1,2,3,4]

result = seri[2]
result = seri[20:]

result = seri

günlerSerisi = pd.Series(günlerSon)
result = günlerSerisi

result = seri = pd.Series(index=günlerSon,data=havaDurumu)
result = seri[[None,"Sali"]]
result = seri.get(["Pazartesi","Sali"]) #Diğer Bir Yol

result = günlerSerisi.count() # Null olmayanları getirir
result = len(günlerSerisi) #Alayı gelir
result = len(günlerSerisi)-günlerSerisi.count()

#MAX AND MIN

randListe = range(0,100)
maksSayı = randListe[0]
for i in randListe:
    if i >maksSayı:
        maksSayı=i
    
result = maksSayı

ranSeries = pd.Series(randListe)

result = ranSeries.max()

#İndeks bul max ve min olanını

result = ranSeries.idxmax()

#APPLY() METHODU

def çarp(eleman):
    
    return eleman*2
def convertToString(eleman):
    if eleman ==1:
        return "bir"
    elif eleman ==2:
        return "iki"

# result = seri.apply(çarp)
result = seri.apply(convertToString)

#MAP METHODU:

calisanlar = ["ahmet","busra","cuneyt","deniz","efe","ferhat","gizem"]
calisanlarSerisi = pd.Series(calisanlar)

kuraSonucu = {"ahmet":5,"busra":2,"cuneyt":1,"deniz":6,"efe":3,"ferhat":4,"gizem":0}
kuraSerisi = pd.Series(kuraSonucu)
result = kuraSerisi.map(calisanlarSerisi)

print(result)

