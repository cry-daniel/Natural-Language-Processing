import json

fmm=1
bmm=2

b = open(r"./data/words.txt", "r",encoding='UTF-8')
out = b.read()
out = json.loads(out)

#print(out)

def find_str(str,length,FMM_or_BMM): # 1 -> FMM ; 2 -> BMM
    if length==0:
        return 0
    if FMM_or_BMM==fmm:
        str_f=str[0:length]
        #print(str_f)
        if str_f in out:
            return length
        else:
            return find_str(str,length-1,fmm)
    elif FMM_or_BMM==bmm:
        length_=len(str)
        str_f=str[length_-length:length_]
        #print(str_f)
        #input()
        if str_f in out:
            return length
        else:
            return find_str(str,length-1,bmm)





def write(res,FMM_or_BMM):
    word=list()
    #print(type(seg))
    for i in res:
        word.append(i)
        #print(word)
    #print(word)
    word = json.dumps(word,ensure_ascii=False)
    #print(word)
    if FMM_or_BMM==fmm:
        a = open(r"./res/FMM.txt", "w",encoding='UTF-8')
    else:
        a = open(r"./res/BMM.txt", "w",encoding='UTF-8')
    a.write(word)
    a.close()