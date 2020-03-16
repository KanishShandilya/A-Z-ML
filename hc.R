#importing dataset
dataset=read.csv('Mall_Customers.csv')
dataset=dataset[4:5]

#Using Dendrogram to find optimal no of clusters
dendrogram=hclust(dist(dataset,method='euclidean'),method = 'ward.D')
plot(dendrogram)

#Fitting data to model
hc=hclust(dist(dataset,method='euclidean'),method='ward.D')
y_hc=cutree(hc,5)

#Visualizing Results
library(cluster)
clusplot(dataset,
         y_hc,
         lines=0,
         shade=TRUE,
         color=TRUE,
         labels=2,
         plotchar=FALSE,
         span=TRUE)