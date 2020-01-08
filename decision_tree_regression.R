#importing dataset
dataset=read.csv('Position_Salaries.csv')
dataset=dataset[2:3]

#Feature Scaling and Spliting won't be needed

#Fitting Models
library(rpart)
regressor=rpart(formula=Salary ~ .,
                data=dataset,
                control=rpart.control(minsplit=1))

#predictig Data
y_pred=predict(regressor,data.frame(Level=6.5))

#Visualizing plot
library(ggplot2)
x_grid=seq(min(dataset$Level),max(dataset$Level),0.01)
ggplot()+
  geom_point(aes(x=dataset$Level,y=dataset$Salary),colour='red')+
  geom_line(aes(x=x_grid,y=predict(regressor,data.frame(Level=x_grid))),
            colour='blue')