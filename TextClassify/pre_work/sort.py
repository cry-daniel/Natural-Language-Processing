import numpy as np

x=np.load(r'../data/dis.npy')
x_copy=x
print(type(x_copy))
#for i in tqdm(range(0,len-1)):
x_copy=np.sort(x_copy)
print()
print(x[2])
print(x_copy[2])
np.save(r'../data/x_copy.npy',x_copy)
exit()