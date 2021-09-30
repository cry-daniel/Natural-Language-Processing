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
            fileCount, fileSet=utils.wordCount(filePath)
            total=sum(fileCount.values())
            j=0
            for key, value in sorted(idfCountThres.items(), key=lambda x: x[1]):
                if key in fileCount:
                    x[i, j]=(fileCount[key] / total) * np.log10(fileNum / value) * 1e5
                j += 1

            x[i, j]=total / 10
            i += 1
        #print(i)
    print("(x,0)",np.size(x,0),"(x,1)",np.size(x,1))
    np.save(r'../data/x.npy', x)
    np.savetxt('../data/x.txt',x,fmt='%s',newline='\n')
    np.save(r'../data/y.npy', y)
    np.savetxt('../data/y.txt',y,fmt='%s',newline='\n')
