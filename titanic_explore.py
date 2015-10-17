#!/usr/bin/python


from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold

import pandas

titanic = pandas.read_csv("train.csv")
print(titanic.describe())

#print "---- Age column ----"
#print titanic["Age"].head(5)


print "Replacing the missing age values with median..."
titanic["Age"]  = titanic["Age"].fillna(titanic["Age"].median())

#print "---describe 2---"
#print titanic.describe()


# filter male - > 1-0 encoding
titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1


# converting the values in the field "embarked"
#print(titanic["Embarked"].unique())


# encoding field "emabarked"
titanic["Embarked"] = titanic["Embarked"].fillna("S")
titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2


#############################################################################
################################  Algorithm #################################
#############################################################################


# linear regression coupled with 3-fold cross validation


alg = LinearRegression()
predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]


kf = KFold(titanic.shape[0], n_folds=3, shuffle=True, random_state=1)
predictions = []




# iloc is a function in pandas to get rows by index
# eg :  titanic.head(25)[predictors].iloc[rowIndex,:3]
# first 25 rows - get only those columns which come under predictors
# - get first 3 rows (range of rows)


for train, test in kf:
#    train and test gives the index of splits - i am not sure of this
    train_predictors = (titanic[predictors].iloc[train,:])
#    target column values from the train dataset
    train_target =  titanic["Survived"].iloc[train]
    alg.fit(train_predictors, train_target)
    test_predictions = alg.predict(titanic[predictors].iloc[test,:])
#predictions is a list of arrays - arrays of predictions    
    predictions.append(test_predictions)


# concatenate the predictions on the 0th axis
predictions = np.concatenate(predictions, axis=0)
predictions[predictions > 0.5] = 1
predictions[predictions <= 0.5] = 0

accuracy = sum(predictions[predictions == titanic["Survived"]]) / len(predictions)

### scikit learn's logistic regression
alg = LogisticRegression(random_state=1)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=3)
print(scores.mean())


