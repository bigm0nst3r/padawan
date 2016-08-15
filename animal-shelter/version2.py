import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
import types
import pdb

raw_train_input = pd.read_csv('train.csv', header=0)

print "Headers are : " , list(raw_train_input.columns.values)
train_features_to_use = ["OutcomeType", "AnimalType", "DateTime", "SexuponOutcome", "AgeuponOutcome", "Breed","Color"]

# preprocessing functions #

def get_year(x):
  return float(x[0:4])

def get_month(x):
  return float(x[5:7])

def to_year(x):
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
# ending preprocessing functions

#Keep only necessary rows
raw_train_df = raw_train_input[train_features_to_use]

#Preprocessing columns
raw_train_df["AgeuponOutcome"] = raw_train_df["AgeuponOutcome"].apply(to_year)    
raw_train_df["Year"] = raw_train_df["DateTime"].apply(get_year)
raw_train_df["Month"] = raw_train_df["DateTime"].apply(get_month)

#dropping datetime column
raw_train_df = raw_train_df.drop("DateTime", 1)

non_numeric_features = ["OutcomeType", "AnimalType", "SexuponOutcome", "Breed", "Color"]
# converting non numberic features to numeric
le = LabelEncoder()
for feature in non_numeric_features:
      raw_train_df[feature] = le.fit_transform(raw_train_df[feature])
      pdb.set_trace()

      
