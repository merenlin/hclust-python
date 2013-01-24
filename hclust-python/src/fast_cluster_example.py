import numpy as np
from matplotlib.pyplot import show
from fastcluster import *
from hcluster import dendrogram 
# Loading the data
data = np.genfromtxt("../../data/ExpRawData-E-TABM-84-A-AFFY-44.tab",names=True,usecols=tuple(range(1,30)),dtype=float, delimiter="\t")
print len(data)
data_array = data.view((np.float, len(data.dtype.names)))
print len(data_array)
print len(data_array.transpose())
#data_link = linkage(data_array.transpose(), method='single', metric='euclidean', preserve_input=True)
data_link = linkage(data_array[1:1000], method='single', metric='euclidean', preserve_input=True)
dendrogram(data_link)
show()