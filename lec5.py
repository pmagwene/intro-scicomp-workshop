import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1000)

	
def plot_clusters(data,clusters,k):
    cmap = plt.get_cmap('spectral')
    fig = plt.figure()
    ax = fig.add_axes((0,0,2,2))
    ax.scatter(data[:,0],data[:,1],c=clusters,cmap=cmap,alpha=1)
    
def plot_pca(data,pca,transform):
	
	fig = plt.figure()
	fig.set_size_inches(8,16)
	
	ax = fig.add_subplot(2,1,1)
	ax.scatter(x = data[:,0],y = data[:,1],alpha=.2)
	a1 = ax.arrow(0,0,1.75*np.abs(pca.components_[0,0]),1.75*np.abs(pca.components_[0,1]),width=.05,head_width=0.2, head_length=0.2,fc='r', ec='r',label="component 1")
	a2 = ax.arrow(0,0,.5*pca.components_[1,0],.5*pca.components_[1,1],head_width=0.2, width=.05,head_length=0.2,fc='g', ec='g',label="component 2")
	ax.legend((a1,a2),("component 1","component 2"),loc="best")

	ax = fig.add_subplot(2,1,2)
	ax.scatter(x = transform[:,0],y = transform[:,1],alpha=.2)
	ax.set_xlabel("component 1")
	ax.set_ylabel("component 2")
	mi = min([ax.get_xlim()[0],ax.get_ylim()[0]])
	ma = max([ax.get_xlim()[1],ax.get_ylim()[1]])
	ax.set_xlim([mi,ma])
	ax.set_ylim([mi,ma])

#hierarchical clustering

hierarchical_data = np.concatenate(
	(np.random.multivariate_normal(mean = [-1,-1],cov=[[1,0],[0,1]],size=10),
	np.random.multivariate_normal(mean = [1,1],cov=[[1,0],[0,1]],size=10))
	)


# k-means

cluster1 = np.random.multivariate_normal(mean = [-1.5,0],cov=[[1,0],[0,1]],size=500)
cluster2 = np.random.multivariate_normal(mean = [1.5,0],cov=[[1,0],[0,1]],size=500)
cluster3 = np.random.multivariate_normal(mean = [0,3],cov=[[1,0],[0,1]],size=500)
kmeans_data = np.concatenate((cluster1,cluster2,cluster3))


# PCA

pca_data = np.random.multivariate_normal(mean = [0,0],
                                     cov =[[1,.75],
                                           [.75,1]], size = 1000)
                                           
_pca_data_1 = np.random.multivariate_normal(mean = [0,0,0],
                                     cov =[[1,.5,0],
                                           [.5,1,0],
                                           [0,0,.05]], size = 1000)

_pca_data_2 = np.random.multivariate_normal(mean = [0,0,0],
                                     cov =[[1,0,-0.5],
                                           [0,.05,0],
                                           [-.5,0,1]], size = 1000)

_pca_data_3 = np.random.multivariate_normal(mean = [0,0,0],
                                     cov =[[.05,0,0],
                                           [0,1,.5],
                                           [0,.5,1]], size = 1000)

pca_data_2 = np.concatenate((_pca_data_1,_pca_data_2,_pca_data_3))


