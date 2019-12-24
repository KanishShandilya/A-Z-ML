#importing dataset
dataset=read.csv('50_Startups.csv')

#Encoding categorical data
dataset$State=factor(dataset$State,
                     levels=c('New York','California','Florida'),
                     labels=c(1,2,3))

#Spliting data

library(caTools)
split=sample.split(dataset$Profit,SplitRatio = 0.8)
training_set=subset(dataset,split==TRUE)
test_set=subset(dataset,split==FALSE)

#Feature Scaling will be taken care by fit method

#Fitting our model to training set

regressor=lm(formula=Profit ~ .,
             data=training_set)
#Profit ~ . means it is the linear combination of all independent variables
#We can alse write it as-Profit~ R>D>Spend+Administration+Marketing.Spend+State

#Predicting The test set results

y_pred=predict(regressor,newdata = test_set)

#Backward Elimination
regressor=lm(formula=Profit ~ R.D.Spend+Administration+Marketing.Spend+State,
             data=dataset)
summary(regressor)
#Removing State as both State1 And State2 are not significant at all
regressor=lm(formula=Profit ~ R.D.Spend+Administration+Marketing.Spend,
             data=dataset)
summary(regressor)
#Repeating
regressor=lm(formula=Profit ~ R.D.Spend+Marketing.Spend,
             data=dataset)
summary(regressor)
#Repeating
regressor=lm(formula=Profit ~ R.D.Spend,
             data=dataset)
summary(regressor)
