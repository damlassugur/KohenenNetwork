import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#3 sınıftan 200er nokta oluşturabilmek amacıyla farklı ortalama ve varyans değerlerine sahip gauss dağılımlarından faydalanılmıştır
mu1=1000
sigma1=500
mu2=2
sigma2=6
mu3=3
sigma3=7

#noktalar npy noktasına kaydedildi
#dosyadan çekilen nokta kümeleri kullanıldı.
def nokta(mu, sigma,x0,y0,z0):
    n1=[1 for i in range(200)]
    n2=[1 for i in range(200)]
    n3=[1 for i in range(200)]

    for i in range(200): #birinci nokta kümesi
        x=x0+random.gauss(mu,sigma)
        y=y0+random.gauss(mu,sigma)
        z=z0+random.gauss(mu,sigma)
        n1[i]=[x,y,z] 
    return np.array(n1)


n1=nokta(mu1,sigma1,10,10,-10)
n2=nokta(mu2,sigma2,-40,10,-10)
n3=nokta(mu3,sigma3,10,-20,10)

#np.save('n1.npy',n1)
#np.save('n2.npy',n2)
#np.save('n3.npy',n3)

train=[]
train.extend(n1[0:130])
train.extend(n2[0:130])
train.extend(n3[0:130])
test=[]
test.extend(n1[130:200])
test.extend(n2[130:200])
test.extend(n3[130:200])
#np.save('train1.npy', train)
#np.save('test1.npy', test)

fig = plt.figure()

ax = fig.add_subplot(111,projection='3d')
ax.scatter(n1[:,0],n1[:,1],n1[:,2],c='r')
ax.scatter(n2[:,0],n2[:,1],n2[:,2],c='blue')
ax.scatter(n3[:,0],n3[:,1],n3[:,2],c='purple')
plt.title('Belirlenmiş Nokta Kümesi')
plt.show()