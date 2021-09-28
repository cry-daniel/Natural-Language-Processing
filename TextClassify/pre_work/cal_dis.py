import numpy as np
import sys

sys.path.append('..')

import utils
from tqdm import tqdm 
from scipy import sparse

x=np.load(r'../data/x.npy')    #size : 19997*18966 zeros(19997,18966)
y=np.load(r'../data/y.npy')    #size : 19997*1
#print(x)
x_trans=np.transpose(x)
len=np.size(x,0)
#dis=np.zeros((len,len))
dis=np.zeros((len,len))
'''
absmul=np.zeros(len)
a=np.array([[1,2,3],[4,5,6]])   #size : 2*3
b=np.zeros((3,2))
'''
#print(b)
#print(np.size(x,1),np.size(x,0))
#print(np.size(x_trans,1),np.size(x_trans,0))

sparse_x=sparse.csr_matrix(x)
sparse_x_trans=sparse.csr_matrix(x_trans)
print("start dis funtion")
dis=sparse_x.dot(x_trans)
print("function dise")
#print(np.size(dis,0),np.size(dis,1))
'''
absmul=sparse_x.sum(axis=1)
def caldis():
    for i in tqdm(range(0,np.size(x,0)-1)):
        for j in range(0,np.size(x,0)-1):
            if(dis[i][j]==0):
                dis[i][j]=-1
                continue
            if i==j:
                dis[i][i]=-1
            else:
                if(absmul[i]*absmul[j]):
                    dis[i][j]=dis[i][j](absmul[i]*absmul[j])
                    if dis[i][j]:
                        print(i,j,dis[i,j])
                else:
                    dis[i][j]=-1

if caldis():
    print("success")
    np.save(r'./data/dis.npy', dis)
else:
    print("failed")
'''
np.save(r'../data/dis.npy', dis)
print("finish")

near=np.zeros(np.size(dis,0))
#k=1

def find_knn():
    cnt=0
    for i in tqdm(range(np.size(dis,1))):
        minn=-1
        for j in range(np.size(dis,0)):
            if i==j:
                continue
            if dis[i][j]>minn:
                minn=dis[i][j]
                near[i]=j
        if minn==0:
            near[i]=i;
            cnt=cnt+1
            #print(i,"exception")
    print(cnt)

find_knn()  #找邻居

np.save(r'../data/near.npy', near)