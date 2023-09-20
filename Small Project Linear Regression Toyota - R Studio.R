library(forecast)
library(caret)
#Part 1
#### Data Partitioning

## import data - Toyota data
## specify the file path based on where you put the data file
toyota_df<-read.csv("C:/Users/santi/Downloads//ToyotaCorolla.csv")

## create training and validation data sets
train_ind<-sample(rownames(toyota_df), dim(toyota_df)[1]*0.6)
valid_ind<-setdiff(rownames(toyota_df),train_ind)
train<-toyota_df[train_ind, ]
valid<-toyota_df[valid_ind, ]

#Part 2
##Run linear Regression Model
mymodel <-  lm(Price~Age_08_04+KM+Automatic,data=train)
#Regression Results
summary(mymodel)

#In class part 3 ---
predicted_values<- predict(mymodel,new_data=valid)
### Prediction performance (prediction error - the smaller the better)
accuracy(predicted_values, valid$Price)


 

