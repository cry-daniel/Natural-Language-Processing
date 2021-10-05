import numpy as np
import random
from tqdm import tqdm

x=np.load(r'../data/x_.npy')
#y=np.load(r'../data/y.npy')

y_=np.load(r'../data/y.npy')

'''
a=[[1,2,3],[4,5,6]]

print(len)
print(np.sum(a[0]))
exit(0)
'''

len=np.size(x,0) #19997
width=np.size(x,1) #18966

temp_=np.zeros(len)


for i in tqdm(range(0,len)):
    temp_[i]=random.randint(1,10)%5

np.savetxt('../data/temp_.txt',temp_,fmt='%s',newline='\n')

tot=0
right=0

for l in range(0,5):
    
    print("test NO.",l+1,":")

    print("init")

    y=y_.copy()

    for i in range(0,len):
        if temp_[i]==l:
            y[i]=21
            
    #np.save('../data/init.npy',init)

    y=list(y)

    c=np.zeros(25)

    for i in range(0,np.size(y)):
        y[i]=int(y[i])
        #print(type(y[i]))
        c[y[i]]+=1

    for i in range(0,20):
        #print(c[i])
        c[i]/=np.size(y)
        #print(c[i])

    tk=np.zeros([25,width])

    print("learn")

    for i in tqdm(range(0,len)): #19997
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

    for i in tqdm(range(0,width)): #18966
        temp=np.sum(x[i])
        #print(temp)
        #input()
        for j in range(0,21):
            if temp==0:
                continue
            tk[j][i]/=temp


    for i in tqdm(range(0,len)):
        if temp_[i]==l:
            maxx=-1e7
            cate=21
            for j in range(0,21):
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

            y[i]=cate
            #print(i,y[i],y_[i])
            #input()
        else:
            continue

    print("test")

    np.save('../data/res'+str(l)+'.npy',y)
    np.savetxt('../data/res'+str(l)+'.txt',y,fmt='%s',newline='\n')