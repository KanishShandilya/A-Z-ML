dataset=read.csv('Social_Network_Ads.csv')
dataset=dataset[3:5]

library(caTools)
split=sample.split(dataset$Purchased,SplitRatio = 0.8)
training_set=subset(dataset,split==TRUE)
test_set=subset(dataset,split==FALSE)

install.packages('kernelab')
library(kernelab)
kpca=kpca()