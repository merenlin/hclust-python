from Bio.Cluster import *
handle = open("../../data/ExpRawData-E-TABM-84-A-AFFY-44.tab")
record = read(handle)
record.data = record.data[1:3000]
genetree = record.treecluster(method='s')
genetree.scale()
exptree = record.treecluster(dist='u', transpose=1)
record.save("../../results/biopython_clustering", genetree, exptree)
