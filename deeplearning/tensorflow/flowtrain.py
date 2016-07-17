from six.moves import cPickle as pickle
from six.moves import range

import tensorflow as tf

import numpy as np

pickle_file = 'notMNIST.pickle'

with open(pickle_file, "rb") as f:
  save = pickle.load(f)
  train_dataset = save['train_dataset']
  train_labels = save['train_labels']
  valid_dataset = save['valid_dataset']
  valid_labels = save['valid_labels']
  test_dataset = save['test_dataset']
  test_labels = save['test_labels']

  del save

# reformatting for training
image_size = 28
num_labels = 10

def resize(dataset, labels):
  """
  
  Arguments:
  - `dataset`:
  - `labels`:
  """
  dataset = dataset.reshape((-1, image_size * image_size)).astype(np.float32)
  labels = (np.arange(num_labels) == labels[:,None]).astype(np.float32)
  return dataset,labels

train_dataset, train_labels = resize(train_dataset, train_labels)  
valid_dataset, valid_labels = resize(test_dataset, test_labels)
test_dataset, test_labels = resize(valid_dataset, valid_labels)


# simple gradient descent
# subsetting the train dataset
train_subset = 10000
graph = tf.Graph()




# Taking ncols and nrows in the range (nrow_start : nrow_end) and (ncol, start)
# ndarry[nrow_start : nrow_end, ncol, start]



with graph.as_default():
  tf_train_dataset = tf.constant(train_dataset[:train_subset, :])
  tf_train_labels = tf.constant(train_labels[:train_subset])

  tf_valid_dataset = tf.constant(valid_dataset)
  tf_test_dataset = tf.constant(test_dataset)

  # our weights - values from a truncated normal distribution
  weights = tf.Variable(tf.truncated_normal([image_size * image_size, num_labels]))
  # all zeroes
  biases = tf.Variable(tf.zeros([num_labels]))

  # bias + th1*x1 + th2*x2 + ...
  logits = tf.matmul(tf_train_dataset, weights) + biases
  # We compute
  # the softmax and cross-entropy (it's one operation in TensorFlow, because
  # it's very common, and it can be optimized). We take the average of this
  # cross-entropy across all training examples: that's our loss
  loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits, tf_train_labels))

  optimizer = tf.train.GradientDescentOptimizer(0.8).minimize(loss)

  train_prediction = tf.nn.softmax(logits)
  valid_prediction = tf.nn.softmax(tf.matmul(tf_valid_dataset, weights) + biases)
  test_prediction = tf.nn.softmax(tf.matmul(tf_test_dataset, weights) + biases)



num_steps = 801

def accuracy(predictions, labels):
    return (100.0 * np.sum(np.argmax(predictions, 1) == np.argmax(labels, 1))
              / predictions.shape[0])



with tf.Session(graph=graph) as session:
    tf.initialize_all_variables().run()
    print('Initialized')

    for step in range(num_steps):
      _, l, predictions = session.run([optimizer, loss, train_prediction])

      print('Loss at step %d: %f' % (step, l))
      print('Training accuracy: %.1f%%' % accuracy(predictions, train_labels[:train_subset, :]))

      print('Validation accuracy: %.1f%%' % accuracy(valid_prediction.eval(), valid_labels))     

    
    

  






      