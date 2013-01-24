import numpy as np
import matplotlib.pyplot as plt
from hcluster import pdist, linkage, dendrogram,squareform # same as import them from scipy

data = np.genfromtxt("../../data/ExpRawData-E-TABM-84-A-AFFY-44.tab",names=True,usecols=tuple(range(1,30)),dtype=float, delimiter="\t")

data_array = data.view((np.float, len(data.dtype.names)))
data_array = data_array[1:1000].transpose()

data_dist = pdist(data_array) # computing the distance

data_link = linkage(data_dist) # computing the linkage

# just plot the dendrogram.
dendrogram(data_link,labels=data.dtype.names)
plt.savefig('../../results/dendrogram.png')

# or plot the heatmap too!

# Compute and plot first dendrogram.
fig = plt.figure(figsize=(8,8))
# x ywidth height
ax1 = fig.add_axes([0.05,0.1,0.2,0.6])
Y = linkage(data_dist, method='single')
Z1 = dendrogram(Y, orientation='right',labels=data.dtype.names) # adding/removing the axes
ax1.set_xticks([])

# Compute and plot second dendrogram.
ax2 = fig.add_axes([0.3,0.71,0.6,0.2])
Z2 = dendrogram(Y)
ax2.set_xticks([])
ax2.set_yticks([])

#Compute and plot the heatmap
axmatrix = fig.add_axes([0.3,0.1,0.6,0.6])
idx1 = Z1['leaves']
idx2 = Z2['leaves']
D = squareform(data_dist)
D = D[idx1,:]
D = D[:,idx2]
im = axmatrix.matshow(D, aspect='auto', origin='lower', cmap=plt.cm.YlGnBu)
axmatrix.set_xticks([])
axmatrix.set_yticks([])

# Plot colorbar.
axcolor = fig.add_axes([0.91,0.1,0.02,0.6])
plt.colorbar(im, cax=axcolor)

fig.savefig('../../results/heatmap.png')