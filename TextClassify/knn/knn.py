import numpy as np
import random
from tqdm import tqdm
from sklearn.neighbors import KNeighborsClassifier

x=np.load('../data/x_.npy')
y=np.load('../data/y.npy')

#print(x.shape)
#print(y.shape)

sum_=0

temp_=np.zeros(19997)

for i in range (0,19997):
    temp_[i]=random.randint(1,10)%5

for l in range(0,5):
    cnt=0
    for i in range(0,19997):
        if temp_[i]==l:
            cnt+=1
    training_data=np.zeros([19997-cnt,18966])
    test_data=np.zeros([cnt,18966])
    training_labels=np.zeros([19997-cnt,1])
    test_labels=np.zeros([cnt,1])
    #print("cnt = ",cnt)
    temp1=0
    temp2=0
    for i in tqdm(range(0,19997)):
        if temp_[i]==l:
            test_data[temp1]=x[temp1]
            test_labels[temp1]=y[temp1]
            temp1+=1
        else:
            training_data[temp2]=x[temp2]
            training_labels[temp2]=y[temp2]
            temp2+=1
    '''
    test_data=test_data
    test_labels=test_labels.transpose()
    training_data=training_data
    training_labels=training_labels.transpose()
    '''
    #print(test_labels)
    #print(training_data.shape)
    #print(training_labels.shape)
    print("Training !")
    nbrs=KNeighborsClassifier(n_neighbors=5,metric='euclidean')
    nbrs.fit(training_data,training_labels)
    KNeighborsClassifier(algorithm='auto',leaf_size=30,metric='euclidean',metric_params=None,n_neighbors=5,p=2,weights='uniform')
    print("Testing !")
    #print("cnt = ",cnt)
    predict_labels=nbrs.predict(test_data)
    #print(predict_labels)
    for i in range(0,cnt):
        if predict_labels[i]==test_labels[i]:
            sum_+=1
    print("Tests done !")

print(sum_,19997,sum_*100/19997,'%')
