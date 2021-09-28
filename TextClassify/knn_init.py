import numpy as np
from tqdm import tqdm 

near=np.load(r'./data/near.npy')
np.savetxt('./data/near.txt',near,fmt='%s',newline='\n')
y=np.load(r'./data/y.npy')
np.savetxt('./data/y.txt',y,fmt='%s',newline='\n')
'''
cate=np.zeros(np.size(near))

for i in range(0,np.size(near)):
    if i%100==0:
        near[i]=i
        cate[i]=y[i]

def find(x):     #并查集
    x=int(x)
    if near[x]==x:
        return x
    else:
        near[x]=find(near[x])
        return near[x]

for i in range(0,np.size(near)):
    find(i)

print(near)

'''