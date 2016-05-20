from __future__ import print_function
import numpy as np
import tensorflow as tf
from six.moves import cPickle as pickle
from six.moves import range
import pdb

pickle_file = 'notMNIST.pickle'

# dimentions will be 20000 * 784 * 1
# 20000 training points
# each of which there are 784 points [28 * 28]
# every point is represented by 1 featue - grayscale intensity

with open(pickle_file, 'rb') as f:
  save = pickle.load(f)
  train_dataset = save['train_dataset']
  train_labels = save['train_labels']
  valid_dataset = save['valid_dataset']
  valid_labels = save['valid_labels']
  test_dataset = save['test_dataset']
  test_labels = save['test_labels']
  del save  # hint to help gc free up memory
  print('Training set', train_dataset.shape, train_labels.shape)
  print('Validation set', valid_dataset.shape, valid_labels.shape)
  print('Test set', test_dataset.shape, test_labels.shape)
  print("After reading...")

    
image_size = 28
num_labels = 10

print("shape of the dataset is now : ", train_dataset.shape)
print("20000 data points each one with 28*28")


# reformatting the dataset into a more adopted shape
def reformat(dataset, labels):
  dataset = dataset.reshape((-1, image_size * image_size)).astype(np.float32)
  # Map 0 to [1.0, 0.0, 0.0 ...], 1 to [0.0, 1.0, 0.0 ...]
  labels = (np.arange(num_labels) == labels[:,None]).astype(np.float32)
  return dataset,labels

# convert 2D array into a  one dimentional space : (28 * 28) -> 784
    
train_dataset, train_labels = reformat(train_dataset, train_labels)
valid_dataset, valid_labels = reformat(valid_dataset, valid_labels)
test_dataset, test_labels = reformat(test_dataset, test_labels)


print('Training set', train_dataset.shape, train_labels.shape)
print('Validation set', valid_dataset.shape, valid_labels.shape)
print('Test set', test_dataset.shape, test_labels.shape)
print("shape of the dataset is now : ", train_dataset.shape)


# computation defined gets stored as graph nodes
train_subset = 10000
graph = tf.Graph()

with graph.as_default():
    tf_train_dataset = tf.constant(train_dataset[:train_subset, :])
    tf_train_labels = tf.constant(train_labels[:train_subset])
    tf_valid_dataset = tf.constant(valid_dataset)
    tf_test_dataset = tf.constant(test_dataset)

    # weight matrix also should be of size 784 : weight of ith feature for jth classifier
    weights = tf.Variable(tf.truncated_normal([image_size * image_size, num_labels]))
    biases = tf.Variable(tf.zeros([num_labels]))

# Multiplies matrix `a` by matrix `b`, producing `a` * `b`.
# The inputs must be two-dimensional matrices, with matching inner dimensions,
# possibly after transposition.
    logits = (tf.matmul(tf_train_dataset, weights) + biases)

#    Computes softmax cross entropy between `logits` and `labels`.
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits, tf_train_labels))
    optimizer = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

    train_prediction = tf.nn.softmax(logits)
    valid_prediction = tf.nn.softmax(tf.matmul(tf_valid_dataset, weights) + biases)
    test_prediction = tf.nn.softmax(tf.matmul(tf_test_dataset, weights) + biases)

num_steps = 801

def accuracy(predictions, labels):
    return (100.0 * np.sum(np.argmax(predictions, 1) == np.argmax(labels, 1))/ predictions.shape[0])
        

# Running the tensorflow graph
# with tf.Session(graph=graph) as session:
#    # initialize all variables
#    tf.initialize_all_variables().run()
#    print('Initialized')
#    for step in range(num_steps):
#        _, l, predictions = session.run([optimizer, loss, train_prediction])
#        if (step % 100 == 0):
#            print('Loss at step %d: %f' % (step, l))
#            print('Training accuracy: %.1f%%' % accuracy(predictions, train_labels[:train_subset, :]))
#                           # Calling .eval() on valid_prediction is basically like calling run(), but
#                           # just to get that one numpy array. Note that it recomputes all its graph
#                           # dependencies.
#            print('Validation accuracy: %.1f%%' % accuracy(valid_prediction.eval(), valid_labels))

#    print('Test accuracy: %.1f%%' % accuracy(test_prediction.eval(), test_labels))
   
