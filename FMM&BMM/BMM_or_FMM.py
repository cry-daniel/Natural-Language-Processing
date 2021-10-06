import json

b = open(r"./res/FMM.txt", "r",encoding='UTF-8')
out = b.read()
FMM = json.loads(out)
b.close()

b = open(r"./res/BMM.txt", "r",encoding='UTF-8')
out = b.read()
BMM = json.loads(out)
b.close()

fmm_len=len(FMM)
bmm_len=len(BMM)

#print(FMM==BMM)

if fmm_len>bmm_len:
    print("res/BMM.txt is better.")
elif fmm_len<bmm_len:
    print("res/FMM.txt is better.")
else:
    cnt_fmm=cnt_bmm=0
    for i in range(0,len(FMM)):
        if len(FMM[i])==1:
            cnt_fmm+=1
        if len(BMM[i])==1:
            cnt_bmm+=1
    if cnt_fmm==cnt_bmm:
        print("Those two are equal.")
    elif cnt_fmm>cnt_bmm:
        print("res/BMM.txt is better.")
    else:
        print("res/FMM.txt is better.")
