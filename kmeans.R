#import dataset
dataset=read.csv('Mall_Customers.csv')
X=dataset[4:5]

#Finding optimal no. of clusters
wcss=vector()
for (i in 1:10) wcss[i]=sum(kmeans(X,i)$withinss)

plot(1:10,wcss,type='b')

#Making model
kmeans=kmeans(X,5,iter.max=300,nstart=10)

#Visulaizing lcusters
install.packages('cluster')
library(cluster)
clusplot(X,
         kmeans$cluster,
         lines=0,
         plotchar=FALSE,
         color=TRUE,
         span=TRUE)