import numpy as np
import random
from tqdm import tqdm 

k=5 #knn's k

len=19997
x=np.load(r'./data/dis.npy')
#x=np.load(r'./data/dis_.npy')

#np.savetxt('./data/near.txt',near,fmt='%s',newline='\n')
y=np.load(r'./data/y.npy')
#np.savetxt('./data/y.txt',y,fmt='%s',newline='\n')
find=np.zeros((len))
cate=np.zeros((len))
init_num=np.zeros((len))
def init():
    for i in range(0,len-1):
        ran=random.randint(1,10)
        if ran%2:
        #if ran>2:
            find[i]=1
            init_num[i]=1
            cate[i]=y[i]
            #print(cate[i])

x_copy=np.load(r'./data/x_copy.npy')
'''
print(x_copy[1448])
exit()
'''
#x_copy=np.load(r'./data/x_copy_.npy')

'''
x=np.load(r'./data/dis.npy')
x_copy=np.load(r'./data/x_copy.npy')

#x_copy=np.transpose(x_copy)

if(np.all(x[0])==np.all(x_copy[0])):
    print("yes")

k=int(input())
print([x[k]])
print([x_copy[k]])

exit()
'''
init()

#x_copy=[[3,2,4],[1,5,4],[3,3,2]]

'''

x_copy=x
print(type(x_copy))
#for i in tqdm(range(0,len-1)):
x_copy=np.sort(x_copy)
print()
print(x[1005])
print(x_copy[1005])
np.save(r'./data/x_copy.npy',x_copy)
exit()
'''
for i in tqdm(range(0,len-1)):
    if find[i]:
        continue

    cnt=0
    cnt1=0

    record=[]
    j=0
    while j<len: # in range(0,len-1):
        j+=1
        if cnt==k:
            break
        
        if x[i][j-1] == x_copy[i][min(cnt1,len-1)]:
        #if x[i][j-1] == x_copy[i][len-1-min(cnt1,len-1)]:
            cnt1+=1
            if i==(j-1):
                continue
            if find[j-1]:
                '''
                if i>1300:
                    print(x_copy[i][len-1])
                    print(i,j-1,x[i][j-1],x_copy[i][min(cnt1-1,len-1)])
                    print(j-1,find[j-1],cate[j-1])
                    input()
                '''
                cnt+=1
                record+=[cate[j-1]]
                j=0
            else:
                continue
    
    if np.size(record)==0:
        cate[i]=-1
    else:
        '''
        
        cate[i]=np.argmax(np.bincount(record))
        find[i]=1
        
        if i>1300:
            print(record)
            input()
            print(cate[i])
        
        '''


print(cate)
tot=0
right=0
np.save(r'./data/cate.npy', cate)
np.savetxt("./data/cate.txt",cate,fmt='%f',newline='\n')
for i in range(0,len-1):
    if init_num[i]:
        continue
    else:
        tot+=1
        if cate[i]==y[i]:
            right+=1

print(right,tot,right/tot)


