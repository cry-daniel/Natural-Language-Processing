import numpy as np
import sys
#from sklearn.metrics import pairwise_distances

sys.path.append('..')

import utils
from tqdm import tqdm 
from scipy import sparse

x=np.load(r'../data/x.npy')    #size : 19997*18966 zeros(19997,18966)
y=np.load(r'../data/y.npy')    #size : 19997*1
#print(np.size([x[1]],0),np.size([x[1]],1))
#print(x)
x_trans=np.transpose(x)
len=np.size(x,0)
len_=np.size(x,1)
dis=np.zeros((len,len))

absmul=np.zeros(len)

#print(np.size(x,1),np.size(x,0))
#print(np.size(x_trans,1),np.size(x_trans,0))


sparse_x=sparse.csr_matrix(x)
sparse_x_trans=sparse.csr_matrix(x_trans)
print("start dis funtion")
dis=sparse_x.dot(x_trans)
print("function dis")
print(np.size(dis,0),np.size(dis,1))
'''
np.save(r"../data/dis_.npy",dis)
exit()
'''
'''

for i in tqdm(range(0,len-1)):
    for j in range(i+1,len-1):
        
        b=sparse.csc_matrix(x[i])
        c=sparse.csc_matrix(x[j])
        a=b-c
        a_=a.transpose()
        temp=a.dot(a_).data
        #print(temp[0])
        dis[i][j]=temp[0]
        dis[j][i]=temp[0]
        #input()
        
        #dis[i][j]=pairwise_distances([x[i]],[x[j]])

'''
absmul=sparse_x.sum(axis=1)
def caldis():
    for i in tqdm(range(0,np.size(x,0)-1)):
        for j in range(i,np.size(x,0)-1):
            #print(dis[i][j])
            #print(absmul[i]*absmul[j])
            #input()

            if(dis[i][j]==0):
                dis[i][j]=-1
                continue
            if i==j:
                dis[i][i]=-1
            else:
                if(absmul[i]*absmul[j]):
                    dis[i][j]/=np.sqrt((absmul[i]*absmul[j]))
                    #print(dis[i][j])
                    #input()
                    dis[j][i]=dis[i][j]
                    #if dis[i][j]:
                    #    print(i,j,dis[i,j])
                else:
                    dis[i][j]=-1

if caldis():
    print("success")
    np.save(r'../data/dis.npy', dis)
else:
    print("failed")

np.save(r'../data/dis.npy', dis)
#np.savetxt('../data/dis.txt',dis,fmt='%s',newline='\n')
print("finish")
exit()
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