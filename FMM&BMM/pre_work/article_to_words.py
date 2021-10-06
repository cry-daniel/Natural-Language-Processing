from json import encoder
import jieba
import numpy
import json

with open('../data/article.txt','r',encoding='utf-8') as f:
  strings = f.read()
strings=strings.replace('\n','')
print(strings)

#strings = '今天天气好冷'
seg=jieba.cut(strings,cut_all=True)
word=list()
#print(type(seg))
for i in seg:
    word.append(i)
    #print(word)

print(word)
word = json.dumps(word,ensure_ascii=False)
print(word)
a = open(r"../data/words.txt", "w",encoding='UTF-8')
a.write(word)
a.close()
b = open(r"../data/words.txt", "r",encoding='UTF-8')
out = b.read()
out = json.loads(out)
print(out)
print(isinstance(out,list))
