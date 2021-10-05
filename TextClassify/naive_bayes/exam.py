import numpy as np

tot=19997

y=np.load('../data/y.npy')
res0=np.load('../data/res0.npy',allow_pickle=True)
res1=np.load('../data/res1.npy',allow_pickle=True)
res2=np.load('../data/res2.npy',allow_pickle=True)
res3=np.load('../data/res3.npy',allow_pickle=True)
res4=np.load('../data/res4.npy',allow_pickle=True)
#print(np.size(y),y[2],res[2],y[2]==res[2])

wrong=0

for i in range(0,np.size(y)):
    temp=res0[i]+res1[i]+res2[i]+res3[i]+res4[i]
    if y[i]*5!=temp:
        wrong+=1

right=tot-wrong

print(right,tot,right/tot*100,"%")