import numpy as np
import math
import random 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
ns=20
#numpy kullanarak iris data setini çektik.
filename = 'C:/Users/damla/Desktop/iris.csv'
raw_data = open(filename, 'rt')
data = np.loadtxt(raw_data, delimiter=",") #virgüle göre verileri ayırdık.

fig = plt.figure()
plt.plot(data[:,0],"r--") 
plt.title("İris kümeleri 'sepal length in cm' çizimi")
plt.xlabel("veri numarası")
plt.ylabel("sepal length in cm")
plt.show()
fig = plt.figure()
plt.plot(data[:,1],"r--") 
plt.title("İris kümeleri 'sepal width in cm' çizimi")
plt.xlabel("veri numarası")
plt.ylabel("sepal width in cm")
plt.show()
plt.plot(data[:,2],"r--")
plt.title("İris kümeleri 'petal length in cm' çizimi")
plt.xlabel("veri numarası")
plt.ylabel("petal length in cm")
plt.show()
plt.plot(data[:,3],"r--") 
plt.title("İris kümeleri 'petal width in cm' çizimi")
plt.xlabel("veri numarası")
plt.ylabel("petal width in cm")
plt.show()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:,1],data[:,2],data[:,3],c='r')
plt.title("iris verisinin çizimi")
plt.show()

#komşuluk fonk tanımı

def komsuluk(index,sigma):
    h=[]
    for j in range(ns):
        h.append(math.exp((-((d[j][index])**2))/(2*(sigma**2))))
    return h


#ögrenme kümesi için kümelerin ilk 30ar terimini aldık.
train=[]
train.extend(data[0:30])
train.extend(data[50:80])
train.extend(data[100:130])

#test kümesi için son 20 değeri ekledik
test=[]
test.extend(data[30:50])
test.extend(data[80:100])
test.extend(data[130:150])
#nöron ağırlıklarını ve konumunu başka bir dosyada oluşturup çektik
w=np.load('agırlık2.npy')
noron=np.load('noron2.npy')

d=np.eye(ns) #nöron mesafelerini tutmak amacıyla kare matris oluşturduk
for i in range(ns):
    for j in range(ns):
        d[i][j]=math.sqrt((noron[i][0]-noron[j][0])**2+(noron[i][1]-noron[j][1])**2) #nöronlar arası uzaklık

##algoritma başlangıcı
#test kümesi oluşturulacak buraya o gelecek
sigma=[50,50]
sigma1=[50,50]
kazanan=[]
do=0
iter=0
lr=lr0=0.4
while do<500:
    index=[] # kazanan nöron indexini tutmak için boş liste oluşturduk
    for j in range(len(train)): #test kümesindeki her veri için dönecek
        index.append(0)
        sigma.append(0)
        iccarpim=[]
        sigma[j+1]=sigma[0]*math.exp((-j)/sigma[1])
        for i in range(ns):
            iccarpim.append(w[i].dot(train[j])) #i. nöron ile iç çarpım
            #iç çarpımı büyük olan nöronun indexini index listesine ekliyor.
            a= iccarpim.index(max(iccarpim))
            index[j]=a
        hij=komsuluk(index[j],sigma[j])

        for k in range(ns):
            w[k]=w[k]+(lr*hij[k]*(train[j]-w[k]))
        lr=lr0*math.exp((-j)/sigma[j])
        
    kazanan.append(index)
    if len(kazanan)!=1:
        if kazanan[-1]==kazanan[-2] :
            do+=1
    iter+=1
    print(iter)
print(kazanan[-1])

kazanant=[]
do=0
iter=0
index1=[]
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
    hij=komsuluk(index1[j],sigma[j])  
kazanant.append(index1)
print(kazanant)
