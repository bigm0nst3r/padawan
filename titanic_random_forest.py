
#!/usr/bin/python

from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier

predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

titanic["Age"]  = titanic["Age"].fillna(titanic["Age"].median())


# titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
# titanic.loc[titanic["Sex"] == "female", "Sex"] = 1


# titanic["Embarked"] = titanic["Embarked"].fillna("S")
# titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
# titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
# titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2


kf = KFold(titanic.shape[0], n_folds=3, shuffle=True, random_state=1)

alg = RandomForestClassifier(random_state=1, n_estimators=10, min_samples_split=2, min_samples_leaf=1)

scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=3)
print(scores.mean())


# changing paramters of the random forest for better accuracy