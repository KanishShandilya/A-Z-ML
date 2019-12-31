#importing dataset
dataset=read.csv('Position_Salaries.csv')

dataset=dataset[2:3]

#No spliting of dataset(it's small)
#Fitting Linear Regression To dataset
lin_reg=lm(formula=Salary~.,
           data=dataset)

#Fitting Polynomial Regression To dataset
dataset$Level1=dataset$Level^2
dataset$Level2=dataset$Level^3
dataset$Level3=dataset$Level^4

poly_reg=lm(formula=Salary~.,
            data=dataset)

#Visualising Linear Regression Results
library(ggplot2)
ggplot()+
  geom_point(aes(x=dataset$Level,y=dataset$Salary),colour='red')+
  geom_line(aes(x=dataset$Level,y=predict(lin_reg,newdata=dataset)),
            colour='blue')
#Visulising plynomial Regression plots
ggplot()+
  geom_point(aes(x=dataset$Level,y=dataset$Salary),colour='red')+
  geom_line(aes(x=dataset$Level,y=predict(poly_reg,newdata=dataset)),
            colour='blue')
#Predicting values
#Linear Model
#data.frame() creates a dataframe to predicta single value
predict(lin_reg,newdata=data.frame(Level=6.5))
#Polynomial Model
predict(poly_reg,newdata=data.frame(Level=6.5,Level1=6.5^2,
                                    Level2=6.5^3,Level3=6.5^4))