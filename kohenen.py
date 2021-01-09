import math
import numpy as np
import random 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#nöronların konum değerlerini -1,1 arasında atıyoruz.
def noronolus():
    x=random.randint(-1,1)
    y=random.randint(-1,1)
    return [x,y]
ns= 20# nöron sayısı tanımladık
noron=[] #boş liste ile nöronların yer ve ağırlık bilgilerini tutacağız
w=[]
for i in range(ns):
    noron.append(0) #listeye sıfır ekleyerek indisli kullanabilmeyi sağladık
    noron[i]=noronolus() #fonksiyon ile oluşturduğumuz nöron yeri ve ağırlığı bilgisini listeye atadık.
    w.append([random.random(),random.random(),random.random(),random.random()])
noron=np.array(noron)
np.save('agırlık2.npy',w)
w=np.array(w)
np.save('noron2.npy',noron)
