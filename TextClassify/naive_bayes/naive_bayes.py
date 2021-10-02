import numpy as np
import random
from tqdm import tqdm

x=np.load(r'../data/x_.npy')
y=np.load(r'../data/y.npy')

y_=np.load(r'../data/y.npy')

'''
a=[[1,2,3],[4,5,6]]

print(len)
print(np.sum(a[0]))
exit(0)
'''

len=np.size(x,0) #19997
width=np.size(x,1) #18966


find=np.zeros(len) #find[i]=1 代表未找

print("init")

for i in tqdm(range(0,len-1)):
    temp=random.randint(1,10)
    if temp%2:
        y[i]=21
        find[i]=1


init=find.copy()

np.save('../data/init.npy',init)

y=list(y)

c=np.zeros(25)

for i in range(0,np.size(y)-1):
    y[i]=int(y[i])
    #print(type(y[i]))
    c[y[i]]+=1


for i in range(0,20):
    #print(c[i])
    c[i]/=np.size(y)
    #print(c[i])

tk=np.zeros([25,width])

print("learn")

for i in tqdm(range(0,len-1)): #19997
    tk[y[i]]+=x[i]
    #print(y[i],tk[y[i]])
    #input()
    '''
    for j in range(0,width-1): #18966
        tk[y[i]][j]+=x[i][j]
    '''

#print(tk[5])
#input()

#print(x[1])
#print(x[2])
#input()

for i in tqdm(range(0,width-1)): #18966
    temp=np.sum(x[i])
    #print(temp)
    #input()
    for j in range(0,20):
        if temp==0:
            continue
        tk[j][i]/=temp


for i in tqdm(range(0,len-1)):
    if find[i]:
        maxx=-1e7
        cate=21
        for j in range(0,20):
            temp=0.
            temp+=np.log10(c[j]+1)
            #print(j,-1,temp)
            for k in range(0,width-1):
                if tk[j][k]==0:
                    continue
                '''
                print(x[i][k],tk[j][k])
                print(x[i][k]*tk[j][k])
                print(np.log(x[i][k]*tk[j][k]+1))
                '''
                temp+=np.log10(x[i][k]*tk[j][k]+1)
            #print(j,temp)
            #input()
            
            if temp>maxx:
                maxx=temp
                cate=j
        find[i]=0
        y[i]=cate
        #print(i,y[i],y_[i])
        #input()
    else:
        continue

tot=0
right=0

print("test")

np.save('../data/res.npy',y)
np.savetxt('../data/res.txt',y,fmt='%s',newline='\n')

for i in tqdm(range(0,len-1)):
    if init[i]==0:
        continue
    else:
        tot+=1
        if y[i]==y_[i]:
            right+=1

print(right,tot,right/tot)