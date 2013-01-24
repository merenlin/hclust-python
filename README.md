hclust-python
=============

Comparison of different clustering packages in python 


Example data has been downloaded from open access Human Gene Expression Atlas
and represents typical data bioinformaticians work with. 
It is "Transcription profiling by array of brain in humans, chimpanzees and macaques,
and brain, heart, kidney and liver in orangutans" in tab-separated format. 
(http://www.ebi.ac.uk/gxa/experiment/E-TABM-84)


***************** Clustering and ML in Python resources ***************** 

Great material on clustering methods: 
http://www-users.cs.umn.edu/~kumar/dmbook/dmslides/chap8_basic_cluster_analysis.pdf

Summary of all algorithms for clustering (and other Unsupervised learning techniques that
Python has to offer)
http://scikit-learn.org/dev/unsupervised_learning.html 

Approach №1: 

Hclust using SciPy + Numpy packages

Working with structured arrays: http://www.scipy.org/Cookbook/Recarray
SciPy cluster: http://code.google.com/p/scipy-cluster/
Linkage function: http://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

Which method to choose? 
* ward's produces compact cluster
* average linkage - doesn't scale well,

shortcut: pylab! http://www.scipy.org/PyLab

Approach №2:
BioPython + TreeView


Approach №3:
fastcluster
