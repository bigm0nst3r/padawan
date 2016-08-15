import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
import types

tmpFeature = ""
raw_train_df = pd.read_csv('train.csv', header=0)
# raw_test_df = pd.read_csv('test.csv', header=0)


train_features_to_use = ["OutcomeType", "AnimalType", "SexuponOutcome", "AgeuponOutcome", "Breed","Color"]
test_features_to_use = ["AnimalType", "SexuponOutcome", "AgeuponOutcome", "Breed","Color"]

non_numeric_columns_train = ["OutcomeType", "OutcomeSubtype", "AnimalType", "SexuponOutcome", "Breed", "Color"]
non_numeric_columns_test = ["AnimalType", "SexuponOutcome", "Breed", "Color"]


# checking if there are nulls in age
# print raw_train_df["AgeuponOutcome"].isnull().any()

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

raw_train_df["AgeuponOutcome"] = raw_train_df["AgeuponOutcome"].apply(year_removal)
# raw_test_df["AgeuponOutcome"] = raw_test_df["AgeuponOutcome"].apply(year_removal)




# # converting non numberic features to numeric
# le = LabelEncoder()
# for feature in non_numeric_columns_train :
#     raw_train_df[feature] = le.fit_transform(raw_train_df[feature])
# for feature in non_numeric_columns_test :
#     raw_test_df[feature] = le.fit_transform(raw_test_df[feature])


# raw_train_df = raw_train_df[train_features_to_use]
# raw_test_df = raw_test_df[test_features_to_use]
# print "Done..."

# features = ["AnimalType", "SexuponOutcome", "AgeuponOutcome", "Breed","Color"]
# labels = ["OutcomeType"]

# trainData = raw_train_df[features]
# trainLabels = raw_train_df[labels]

# testData = raw_test_df[features]


# trainData['AnimalType'] = trainData['AnimalType'].astype(float)
# trainData['SexuponOutcome'] = trainData['SexuponOutcome'].astype(float)
# trainData['AgeuponOutcome'] = trainData['AgeuponOutcome'].astype(float)
# trainData['Breed'] = trainData['Breed'].astype(float)
# trainData['Color'] = trainData['Color'].astype(float)


# testData['AnimalType'] = testData['AnimalType'].astype(float)
# testData['SexuponOutcome'] = testData['SexuponOutcome'].astype(float)
# testData['AgeuponOutcome'] = testData['AgeuponOutcome'].astype(float)
# testData['Breed'] = testData['Breed'].astype(float)
# testData['Color'] = testData['Color'].astype(float)

# gbm = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.05).fit(trainData, trainLabels)
# print gbm
# print "Model Building..."

# predictions = gbm.predict(testData)
# submission = pd.DataFrame({ 'Prediction': predictions})


# def change_format(x):
#     _map = {3: 'Return_to_owner', 2:'Euthanasia', 0: 'Adoption', 4: 'Transfer', 1:'Died'}
#     return _map[x]

# submission["Reason"] = submission["Prediction"].apply(change_format)


# def one_hot_encode(x):
#     global tmpFeature
#     if x is tmpFeature:
#         return 1
#     else:
#         return 0

# new_columns = ['Return_to_owner', 'Euthanasia', 'Adoption', 'Transfer', 'Died']

# for col in new_columns :
#     tmpFeature = col
#     submission[col] = submission["Reason"].apply(one_hot_encode)





