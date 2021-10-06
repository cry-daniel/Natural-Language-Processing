import numpy
import utils

max_len=5

with open('./data/article.txt','r',encoding='utf-8') as f:
  str = f.read()
str=str.replace('\n','')

print(str)

res=[]

while str:
    temp=utils.find_str(str,max_len,utils.bmm)
    length_=len(str)
    if temp==0:
        res.append(str[length_-1])
        str=str[:length_-1]
        continue
    res.append(str[length_-temp:length_])
    str=str[:length_-temp]
    '''
    print(res)
    print(str)
    input()
    '''

res_=[]
length=len(res)

for i in range(0,length):
    res_.append(res[length-i-1])

utils.write(res_,utils.bmm)

print("The result is shown below : ")
for i in range(0,len(res_)):
    print(res_[i]+'/',end='')
print()