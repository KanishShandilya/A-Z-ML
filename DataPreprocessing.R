# Data Preprocessing

# Importing the dataset

dataset = read.csv('Data.csv')


# Taking care of missing data

dataset$Age = ifelse(is.na(dataset$Age),

                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),

                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),

                ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),

                        dataset$Salary)
dataset$Country=factor(dataset$Country,
                       levels=c('France','Spain','Germany'),
                       labels=c(0,1,2))
dataset$Purchased=factor(dataset$Purchased,
                       levels=c('No','Yes'),
                       labels=c(0,1))
#spliting test and train data
#install.packages('caTools')
library(caTools)
split=sample.split(dataset$Purchased,SplitRatio=0.8)
trainingset=subset(dataset,split==TRUE)
testset=subset(dataset,split==FALSE)
#Feature Scaling
trainingset[,2:3]=scale(trainingset[,2:3])
testset[,2:3]=scale(testset[,2:3])