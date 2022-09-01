from re import X
import pandas as pd

result = calisanDataFrame = pd.read_csv("calisan_data.csv")

#Function chaining
result = calisanDataFrame.isnull().sum().sum()
result = calisanDataFrame.head()
result = calisanDataFrame.tail()

# matris = calisanDataFrame.values #Matrise çevirdik
# result = matris[0][0]
result = type(calisanDataFrame)
result = calisanDataFrame.columns
result = calisanDataFrame["Isimler"]

#DATAFRAME ATTRIBUTES
result = calisanDataFrame.dtypes
result = calisanDataFrame.describe() #Önemli
result = calisanDataFrame.columns
result = calisanDataFrame.shape
result = calisanDataFrame.info() #En önemlisi

#ACCES COLUMNS IN DATA FRAME

result = calisanDataFrame["Maas"] # Bu daha geçerli
calisanDataFrame.rename(columns={"Isimler":"isimler","Soyisimler":"Soy Isim"},inplace=True) # Sutün ve indeks değiştir


result = calisanDataFrame[["DogumTarihi","Maas"]]


#MAASLARIN TOPLAMINI BULALIM
maasSerisi = calisanDataFrame["Maas"]

#method halinde
maasToplam = maasSerisi.sum()



#algoritmik şekilde
maasToplam = 0
for i in maasSerisi:
    maasToplam+=i


#KULLANICI ADI SUTÜNÜ EKLE:

#method haline
# calisanDataFrame["KullanıcıAdi"] = calisanDataFrame["isimler"]+calisanDataFrame["Soy Isim"]

#Algoritmik şekilde
kullaniciAdi = []

for i in range(0,len(calisanDataFrame)):
    kullaniciAdi.append(calisanDataFrame["isimler"][i]+calisanDataFrame["Soy Isim"][i])

calisanDataFrame["Kullanici Adi"] = kullaniciAdi
calisanDataFrame.drop(["Kullanici Adi"],axis = 1,inplace=True)


calisanDataFrame.insert(loc = 2,column = "kullaniciAdi",value=kullaniciAdi)
result = calisanDataFrame.info()
result = calisanDataFrame["Maas"]

def zamYap(x):
    return x+1000
yeniMaas= calisanDataFrame["Maas"].apply(zamYap)

calisanDataFrame["Maas"] = yeniMaas
result = calisanDataFrame["Maas"]

result = calisanDataFrame["Departman"].value_counts()

print(result)
