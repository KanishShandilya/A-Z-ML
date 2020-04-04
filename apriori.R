#data preprocessing
dataset=read.csv('Market_Basket_Optimisation.csv',header=FALSE)
#install.packages('arules')
library(arules)

#Making sparse matrix
dataset=read.transactions('Market_Basket_Optimisation.csv',sep=',',rm.duplicates = TRUE)
summary(dataset)

#plotting 10 most buyed product
itemFrequencyPlot(dataset,topN=10)

#training data
rules=apriori(dataset,parameter = list(support=0.004,confidence=0.2))

#visualizing results
inspect(sort(rules,by='lift')[1:10])