import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
import types

train_df = pd.read_csv('train.csv', header=0)
test_df = pd.read_csv('test.csv', header=0)


featuresToUse = ["OutcomeType", "AnimalType", "SexuponOutcome", "AgeuponOutcome", "Breed","Color"]
testFeatures = ["AnimalType", "SexuponOutcome", "AgeuponOutcome", "Breed","Color"]

nonNumericColumnsTrain = ["OutcomeType", "OutcomeSubtype", "AnimalType", "SexuponOutcome", "Breed", "Color"]
nonNumericColumnsTest = ["AnimalType", "SexuponOutcome", "Breed", "Color"]


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
test_df["AgeuponOutcome"] = test_df["AgeuponOutcome"].apply(year_removal)


# converting non numberic features to numeric
le = LabelEncoder()
for feature in nonNumericColumnsTrain :
    train_df[feature] = le.fit_transform(train_df[feature])
for feature in nonNumericColumnsTest :
    test_df[feature] = le.fit_transform(test_df[feature])


train_df = train_df[featuresToUse]
test_df = test_df[testFeatures]
print "Done..."

features = ["AnimalType", "SexuponOutcome", "AgeuponOutcome", "Breed","Color"]
labels = ["OutcomeType"]

trainData = train_df[features]
trainLabels = train_df[labels]

testData = test_df[features]


trainData['AnimalType'] = trainData['AnimalType'].astype(float)
trainData['SexuponOutcome'] = trainData['SexuponOutcome'].astype(float)
trainData['AgeuponOutcome'] = trainData['AgeuponOutcome'].astype(float)
trainData['Breed'] = trainData['Breed'].astype(float)
trainData['Color'] = trainData['Color'].astype(float)


testData['AnimalType'] = testData['AnimalType'].astype(float)
testData['SexuponOutcome'] = testData['SexuponOutcome'].astype(float)
testData['AgeuponOutcome'] = testData['AgeuponOutcome'].astype(float)
testData['Breed'] = testData['Breed'].astype(float)
testData['Color'] = testData['Color'].astype(float)

gbm = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.05).fit(trainData, trainLabels)
print gbm
print "Model Building..."

predictions = gbm.predict(testData)
submission = pd.DataFrame({ 'Prediction': predictions})


def change_format(x):
    _map = {0: 'Return_to_owner', 1:'Euthanasia', 2: 'Adoption', 3: 'Transfer', 4:'Died'}
    return _map[x]

submission["Reason"] = submission["Prediction"].apply(change_format)




