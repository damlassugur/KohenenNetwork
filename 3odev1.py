import math
import numpy as np
import random 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


ns=20
#komsuluk fonksiyon tanımı
def komsuluk(index,sigma):
    h=[]
    for j in range(ns):
        h.append(math.exp((-((d[j][index])**2))/(2*(sigma**2))))
    return h
#dosyadan çekilen nokta kümeleri kullanıldı.

n1=np.load('n1.npy')
n2=np.load('n2.npy')
n3=np.load('n3.npy')

fig = plt.figure()

ax = fig.add_subplot(111,projection='3d')
ax.scatter(n1[:,0],n1[:,1],n1[:,2],c='r')
ax.scatter(n2[:,0],n2[:,1],n2[:,2],c='blue')
ax.scatter(n3[:,0],n3[:,1],n3[:,2],c='purple')
plt.title('Nokta kümelerinin çizimi')
train=np.load('train1.npy')
test=np.load('test1.npy')

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter(train[:,0],train[:,1],train[:,2],c='r')
plt.title('Ogrenme kumesi çizimi')
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter(test[:,0],test[:,1],test[:,2],c='blue')
plt.title('Test kumesi çizimi')
#plt.show()
w=np.load('agırlık.npy')
noron=np.load('noron4.npy')
print('baslangıc nöron agırlıkları \n',w)

d=np.eye(ns) #nöron mesafelerini tutmak amacıyla kare matris oluşturduk
for i in range(ns):
    for j in range(ns):
        d[i][j]=math.sqrt((noron[i][0]-noron[j][0])**2+(noron[i][1]-noron[j][1])**2) #nöronlar arası uzaklık

##algoritma başlangıcı
sigma=[4,4]
kazanan=[]
do=0 #durdurma koşulu için değişken tanımı
iter=0
lr=lr0=0.5 #ögrenme hızı
while do<1:
    index=[] # kazanan nöron indexini tutmak için boş liste oluşturduk
    for j in range(len(train)): #test kümesindeki her veri için dönecek
        index.append(0)
        sigma.append(0)
        iccarpim=[]
        sigma[j]=sigma[0]*math.exp((-j)/sigma[1]) #sigma değerinin iterasyon numaralarına göre güncellenmesi
        for i in range(ns):
            iccarpim.append(w[i].dot(train[j])) #i. nöron ile iç çarpım
            #iç çarpımı büyük olan nöronun indexini index listesine ekliyor.
            a= iccarpim.index(max(iccarpim))
            index[j]=a
        hij=komsuluk(index[j],sigma[j])

        for k in range(ns):
            w[k]=w[k]+lr*hij[k]*(train[j]-w[k]) #nöron ağırlıkları komşuluk değerine göre güncelleniyor

        lr=lr0*math.exp((-j)/sigma[j]) #öğrenme hızı iterasyonlar ilerledikçe azalıyor
        
    kazanan.append(index)
    if len(kazanan)!=1:
        if kazanan[-1]==kazanan[-2] : #durdurma koşulunu sınamak için kazanan son iki nöron dizisini karşılaştırıyor
            do+=1
    iter+=1
    print(iter)
print(kazanan[-1])
sigma1=[4,4]
kazanant=[]
do=0
iter=0
index1=[]
#test algoritmesı
for j in range(len(test)):
    index1.append(0)
    sigma1.append(0)
    iccarpim=[]
    sigma1[j]=sigma1[0]*math.exp((-j)/sigma1[1])
    for i in range(ns):
        iccarpim.append(w[i].dot(test[j])) #i. nöron ile iç çarpım
        #iç çarpımı büyük olan nöronun indexini index listesine ekliyor.
        a= iccarpim.index(max(iccarpim))
        index1[j]=a
    hij=komsuluk(index1[j],sigma1[j])
    
kazanant.append(index1)
print(kazanant)
print("nöron sayısı:",ns)
print('ogrenim sonrası nöron ağırlıkları \n',w)
print('ogrenme hızı:',lr0)




