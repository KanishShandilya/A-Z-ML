#Simple Linear Regression

#importing dataset
dataset=read.csv('Salary_Data.csv')

#Spliting Data
library(caTools)
split=sample.split(dataset$Salary,SplitRatio=0.8)
training_set=subset(dataset,split==TRUE)
test_set=subset(dataset,split==FALSE)
#Feature Scaling Won't be Needed

#Fitting simple Regression To training set

regressor=lm(formula=Salary~YearsExperience,
             data=training_set)
#Predicting Data 

y_pred=predict(regressor,newdata=test_set)
#Visualizing Training set data
#install.packages('ggplot2')
library(ggplot2)
ggplot()+
  geom_point(aes(x=training_set$YearsExperience,y=training_set$Salary),
             colour='red')+
  geom_line(aes(x=training_set$YearsExperience,y=predict(regressor,newdata = training_set)
                ),colour='blue')+
  ggtitle('Salary vs Experience')+
  xlab('Experience')+
  ylab('Salary')
#Visualizing Test Results
ggplot()+
  geom_point(aes(x=test_set$YearsExperience,y=test_set$Salary),colour="red")+
  geom_line(aes(x=training_set$YearsExperience,y=predict(regressor,newdata = training_set))
            ,colour='blue')+
  ggtitle('Salary vs Experience')+
  xlab('Years Of Experience')+
  ylab('Salary')