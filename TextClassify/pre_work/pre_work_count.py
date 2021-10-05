import os
import sys
import pickle
import numpy as np

sys.path.append('..')

import utils
import config

if __name__ == "__main__":
    with open(r"../data/idfCount.p", "rb") as f:
        idfCount=pickle.load(f)
    #print(idfCount)
    #input
    idfCountThres={}
    thres=config.numThres
    for key, value in idfCount.items():
        if value >= thres:
            idfCountThres[key]=value
    featureNum=len(idfCountThres)
    fileNum=config.fileNum
    x=np.zeros((fileNum, featureNum + 1))
    y=np.zeros((fileNum, 1))

    dataPath=config.dataPath
    i=0
    Dict=config.Dict
    for root, dirs, files in os.walk(dataPath):
        #print(root,dirs,files)
        for file in files:
            y[i]=Dict[root.split('/')[-1]]   
            filePath=os.path.join(root, file)
            fileCount, fileSet=utils.wordCount(filePath) #fileCount记的是每篇文章中出现的单词及其次数
            total=sum(fileCount.values())
            #print(fileSet)
            #print(fileCount.values())
            #print(file,total)
            #print(idfCountThres.items())
            j=0
            #print(idfCountThres.items())
            #input()
            for key, value in sorted(idfCountThres.items(), key=lambda x: x[1]):
                if key in fileCount:
                    #print(key)
                    #x[i, j]=(fileCount[key] / total) * np.log10(fileNum / value) * 1e5
                    x[i, j]=fileCount[key]*100
                    #print(i,j,x[i,j],x[i][j])
                else:
                    x[i,j]=0
                j += 1
            #input()
            x[i, j]=0
            i += 1
        print(i)
    print(y)
    print(x[1])
    np.savetxt(r'../data/x.txt',x,fmt='%s',newline='\n')
    print("(x,0)",np.size(x,0),"(x,1)",np.size(x,1))
    np.save(r'../data/x_.npy', x)
    #np.savetxt('../data/x.txt',x,fmt='%s',newline='\n')
    #np.save(r'../data/y.npy', y)
    #np.savetxt('../data/y.txt',y,fmt='%s',newline='\n')
