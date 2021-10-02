import numpy as np

y=np.load('../data/y.npy')
res=np.load('../data/res.npy',allow_pickle=True)

#print(np.size(y),y[2],res[2],y[2]==res[2])

right=0

for i in range(0,np.size(y)):
    if y[i]==res[i]:
        right+=1

tot=int(np.size(y)/2)

right-=tot

print(right,tot,right/tot*100,"%")