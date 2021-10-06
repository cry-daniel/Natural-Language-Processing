import numpy
import utils

max_len=5

with open('./data/article.txt','r',encoding='utf-8') as f:
  str = f.read()
str=str.replace('\n','')

print(str)

res=[]

while str:
    temp=utils.find_str(str,max_len,FMM_or_BMM=1)
    if temp==0:
        res.append(str[0])
        str=str[1:]
        continue
    res.append(str[0:temp])
    str=str[temp:]
    '''
    print(res)
    print(str)
    input()
    '''

utils.write(res,utils.fmm)

print("The result is shown below : ")
for i in range(0,len(res)):
    print(res[i]+'/',end='')
print()