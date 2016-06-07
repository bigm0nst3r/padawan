import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
import numpy as np
import types

train_df = pd.read_csv('train.csv', header=0)
test_df = pd.read_csv('test.csv', header=0)


featuresToUse = ["OutcomeType", "OutcomeSubtype", "AnimalType", "SexuponOutcome", "AgeuponOutcome", "Breed","Color"]
nonNumericColumns = ["OutcomeType", "OutcomeSubtype", "AnimalType", "SexuponOutcome", "Breed", "Color"]


# checking if there are nulls in age
# print train_df["AgeuponOutcome"].isnull().any()

# correct age column in the dataframe

def year_removal(x):
    y = x
    if x is None :
        return 1.0
    elif type(x)==types.FloatType:
        return x
    elif "day" in x:
        y = float(x.replace("days","").replace("day","").strip())/365
    elif "week" in x:
        y = float(x.replace("weeks","").replace("week","").strip()) * 7/365
    elif "month" in x:
        y = float(x.replace("months","").replace("month","").strip()) * 30/365
    elif "year" in x:
        y = (float(x.replace("years","").replace("year","").strip()))
    return '{0:.2f}'.format(y)

train_df["AgeuponOutcome"] = train_df["AgeuponOutcome"].apply(year_removal)


# converting non numberic features to numeric
le = LabelEncoder()
for feature in nonNumericColumns :
    train_df[feature] = le.fit_transform(train_df[feature])


print "Done..."
    