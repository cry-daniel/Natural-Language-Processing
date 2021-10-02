import numpy as np
import sys
import os
from scipy import sparse
from tqdm import tqdm
import config

#sys.path.append('.')

dataPath=config.dataPath
print(dataPath)
input()
for root, dirs, files in os.walk(dataPath):
    print(root)
    print(dirs)
    print(files)
    input()
    for file in tqdm(files):
        print(root)
        print(file)
        filePath=os.path.join(root, file)
        print(filePath)
        input()
exit()

import utils,config
test=[[1,3,4,2],
[2,1,4,3],
[3,2,4,4],
[4,1,1,2]]

print(test[0][2])

te=test

test=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

print(te)

exit()
'''
len=4

test=[[1,3,4,2],
[2,1,4,3],
[3,2,4,4],
[4,1,1,2]]
print(test[1])

i=0

while i < 10:
    print(i)
    i+=1
    for j in range(1,10):
        #print(j)
        if 1 in range(0,3):
            i=1
'''
y=np.load(r'./data/y.npy')
np.savetxt("./data/y.txt",y,fmt='%f',newline='\n')

x=np.load(r'./data/x.npy')
#print(x)

dis=np.load(r'./data/dis.npy')
dis_=np.load(r'./data/x_copy.npy')

print(dis[1448])
print()
print(dis_[1448])

test=[[1.0e-4,3,4,2],[5.1,1,4,3],[3.4e-14,2,4,4],[4,1,1,2]]
test=np.array(test)
print(type(test))
#print(test)
test=np.sort(test)
print(test)
np.savetxt("./data/test.txt",test,fmt='%f',newline='\n')

exit()

#'''
'''

a=[[1,2,3],[4,5,6]]
b=[[1,3,3],[4,4,6]]
d=sparse.csc_matrix(a[1])
e=sparse.csc_matrix(b[1])
f=d-e
f_=f.transpose()
print(d-e)
print(f)
print(f.dot(f_).data[0])
exit()
'''
#np.savetxt("./data/a.txt",a,fmt='%f',newline='\n')
#cate=np.load("./data/cate.npy")
#np.savetxt("./data/cate.txt",cate,fmt='%f',newline='\n')
#y=np.load("./data/y.npy")
#np.savetxt("./data/y.txt",y,fmt='%f',newline='\n')

#x_copy=np.load("./data/x_copy.npy")
#np.savetxt("./data/x_copy.txt",x_copy,fmt='%f',newline='\n')

#print(y,cate)
'''
cate=np.zeros(4)
record=[]
print(np.size(record))
record+=[3.0]
record+=[2.0,1.0,3.0]
cate[2]=np.argmax(np.bincount(record))
print(cate)

for i in range(1,10):
    #print(i)
    for j in range(1,10):
        #print(j)
        if 1 in (record[0:3]):
            if 1==1:
                #print("x")
                i=1
'''