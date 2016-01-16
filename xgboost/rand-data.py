import numpy as np
import xgboost as xgb



# loading data into a data structure
data = np.random.rand(5,10)
labels = np.random.randint(2, size=5)
dtrain = xgb.DMatrix(data, label=labels)
dtrain.save_binary("train_data.buffer")



# setting boosting parameters
param = {
    'bst:max_depth':2, 'bst:eta':1, 'silent':1, 'objective':'binary:logistic'
}
param['nthread'] = 4


# multiple evaluation metrics can be mentioned
param['eval_metric'] = 'auc'

# training the dataset
num_iterations = 10
bst = xgb.train(param, dtrain, num_iterations)
bst = xgb.Booster({'nthread':4})

data = np.random.rand(7, 10)
dtest = xgb.DMatrix(data)

ypred = bst.predict(dtest,ntree_limit=2)
print(ypred)

xgb.plot_importance(bst)