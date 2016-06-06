from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import pdb


dataset = pd.read_csv("train.csv")
target = dataset[[0]].values.ravel()

train = dataset.iloc[:,1:].values
test = pd.read_csv("test.csv").values

rf = RandomForestClassifier(n_estimators = 100)
rf.fit(train, target)
pred = rf.predict(test)
pdb.set_trace()

np.savetxt('submission_rand_forest.csv', np.c_[range(1,len(test)+1),pred], delimiter=',', header = 'ImageId,Label', comments = '', fmt='%d')

