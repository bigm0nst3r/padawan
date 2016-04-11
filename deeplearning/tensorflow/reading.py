
import numpy as np
from six.moves import cPickle as pickle  

import pdb

pickle_file = 'notMNIST.pickle'

with open(pickle_file, 'rb') as f:
    save = pickle.load(f)
    train_dataset = save['train_dataset']
    train_labels = save['train_labels']
    train_labels = save['train_labels']
    test_labels = save['test_labels']
    valid_dataset = save['valid_dataset']
    valid_labels = save['valid_labels']
    del save

np.unique(train_labels)
    
    