##########################################################
### Chapter 6 - Introduction to RNNs - using R  ##########
########## Humidity forecasting with RNNs#################
##########################################################

library("rattle.data")
library("rnn")

data(weatherAUS)
View(weatherAUS)

#extract only 1 and 14 clumn and first 3040 rows (Albury location)
data=weatherAUS[1:3040,c(1,14)]
summary(data)

data_cleaned <- na.omit(data) 
data_used=data_cleaned[1:3000]

x=data_cleaned[,1]
y=data_cleaned[,2]

head(x)
head(y)

X=matrix(x, nrow = 30)
Y=matrix(y, nrow = 30)

# Standardize in the interval 0 - 1
Yscaled = (Y - min(Y)) / (max(Y) - min(Y))
Y=t(Yscaled)

train=1:70
test=71:100

model <- trainr(Y = Y[train,],
                X = Y[train,],
                learningrate = 0.05,
                hidden_dim = 16,
                numepochs = 1000)

plot(colMeans(model$error),type='l',xlab='epoch',ylab='errors')

Yp <- predictr(model, Y[test,])

plot(as.vector(t(Y[test,])), col = 'red', type='l', 
     main = "Actual vs Predicted Humidity: testing set", 
     ylab = "Y,Yp")
lines(as.vector(t(Yp)), type = 'l', col = 'black')
legend("bottomright", c("Predicted", "Actual"), 
       col = c("red","black"), 
       lty = c(1,1), lwd = c(1,1))

############################################################