#importing daraset

dataset=read.csv('Wine.csv')

#Spliting dataset
library(caTools)

split=sample.split(dataset$Customer_Segment,SplitRatio = 0.8)
training_set=subset(dataset,split==TRUE)
test_set=subset(dataset,split==FALSE)

#Feature Scaling
training_set[-14]=scale(training_set[-14])
test_set[-14]=scale(test_set[-14])

#install.packages('caret')
library(caret)
library(e1071)

#pca

pca=preProcess(x=training_set[-14],method='pca',pcaComp=2)
training_set=predict(pca,training_set)
test_set=predict(pca,test_set)

#putting labels at  last colm
training_set=training_set[c(2,3,1)]
test_set=test_set[c(2,3,1)]

#Making model
classifier=svm(formula=Customer_Segment ~ .,
               data=training_set,
               type='C-classification',
               kernel='linear')

y_pred=predict(classifier,test_set[-3])

cm=table(test_set[,3],y_pred)