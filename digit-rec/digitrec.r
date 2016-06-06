library(caTools)
digits = read.csv('train.csv', header=TRUE)
split = sample.split(digits$label, SplitRatio=.7)
train_data = subset(digits, split==TRUE)
test_data = subset(digits, split==FALSE)

library(randomForest)
train_data$label = factor(train_data$label)
test_data$label = factor(test_data$label)
randomForest = randomForest(label ~ ., data=train_data, nodesize=10, ntree=200, do.trace=TRUE)
randomForestPredict = predict(randomForest, newdata=test_data)
randomForestTable = table(test_data$label, randomForestPredict)


prediction_Data = read.csv('test.csv')
randomForestPredict = predict(randomForest, newdata=prediction_Data)
out = levels(randomForestPredict)[randomForestPredict]
write(out, 'prediction.csv')
