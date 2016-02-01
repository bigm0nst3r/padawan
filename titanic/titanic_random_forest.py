
#!/usr/bin/python

from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
import re
import pandas

from sklearn.feature_selection import SelectKBest,f_classif


# test comment
titanic = pandas.read_csv("train.csv")
titanic["Age"]  = titanic["Age"].fillna(titanic["Age"].median())
predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

# titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
# titanic.loc[titanic["Sex"] == "female", "Sex"] = 1


# titanic["Embarked"] = titanic["Embarked"].fillna("S")
# titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
# titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
# titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2

alg = RandomForestClassifier(random_state=1, n_estimators=10, min_samples_split=2, min_samples_leaf=1)

scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=3)
print(scores.mean())


# changing paramters of the random forest for better accuracy

alg = RandomForestClassifier(random_state=1, n_estimators=150, min_samples_split=4, min_samples_leaf=2)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=3)
print(scores.mean())


title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7, "Col": 7, "Mlle": 8, "Mme": 8, "Don": 9, "Lady": 10, "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2}


def getTitle(name):
    """
    Arguments:
    - `name`:
    """
    title = re.search(' ([A-Za-z]+)\.',name)
    if title:
        return title.group(1)
    return ""

titles = titanic["Name"].apply(getTitle)



    
selector = SelectKBest(f_classif, k=5)
selector.fit(titanic["predictors"],titanic["survived"])

alg.predict