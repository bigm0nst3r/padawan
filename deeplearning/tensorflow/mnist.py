from __future__ import print_function

import numpy as np
import os, sys

from scipy import ndimage
from sklearn.linear_model import LogisticRegression

from six.moves.urllib.request import urlretrieve
from six.moves import cPickle as pickle

import pdb

image_size = 28
pixel_depth = 255


train_folders = [ '/home/sree/code/train/notMNIST_large/A', '/home/sree/code/train/notMNIST_large/B', '/home/sree/code/train/notMNIST_large/C', '/home/sree/code/train/notMNIST_large/D']

test_folders = ['/home/sree/code/train/notMNIST_small/A', '/home/sree/code/train/notMNIST_small/B', '/home/sree/code/train/notMNIST_small/C', '/home/sree/code/train/notMNIST_small/D']




def load_letter(folder, min_num_images):
  """
  Arguments:
  - `folder`:
  - `min_num_of_images`:
  """
  image_files = os.listdir(folder)
  dataset = np.ndarray(shape=(len(image_files), image_size, image_size), dtype=np.float32)
  image_index = 0
  print(folder)
  print(len(image_files))
  for image in image_files:
    image_file = os.path.join(folder, image)
#    pdb.set_trace()
    try :
#      print("Processing Image file", image_file)
      image_data = (ndimage.imread(image_file).astype(float) - pixel_depth/2) / pixel_depth
      if image_data.shape != (image_size, image_size):
        raise Exception('Unexpected image shape: %s' % str(image_data.shape))
        dataset[image_index, :, :] = image_data
        image_index += 1
    except IOError as e:
        print(e)
        print("I/o error")

  num_images = image_index
  dataset = dataset[0:num_images, :, :]
  if num_images < min_num_images:
    raise Exception('Many fewer images than expected: %d < %d' %
                    (num_images, min_num_images))
    print('Full dataset tensor:', dataset.shape)
    print('Mean:', np.mean(dataset))
    print('Standard deviation:', np.std(dataset))
  return dataset



def maybe_pickle(data_folders, min_num_images_per_class, force=False):
  dataset_names = []
  for folder in data_folders:
    set_filename = folder + '.pickle'
    dataset_names.append(set_filename)
    if os.path.exists(set_filename) and not force:
      # You may override by setting force=True.
      print('%s already present - Skipping pickling.' % set_filename)
    else:
      print('Pickling %s.' % set_filename)
      dataset = load_letter(folder, min_num_images_per_class)
      try:
        with open(set_filename, 'wb') as f:
          pickle.dump(dataset, f, pickle.HIGHEST_PROTOCOL)
      except Exception as e:
          print('Unable to save data to', set_filename, ':', e)
  return dataset_names



#train_datasets = maybe_pickle(train_folders, 45000)
#test_datasets = maybe_pickle(test_folders, 1800)



def make_arrays(nb_rows, img_size):
  if nb_rows:
    dataset = np.ndarray((nb_rows, img_size, img_size), dtype=np.float32)
    labels = np.ndarray(nb_rows, dtype=np.int32)
  else:
    dataset, labels = None, None
  return dataset, labels


def merge_datasets(pickle_files, train_size, valid_size = 0):
  num_classes = len(pickle_files)
  valid_dataset, valid_labels = make_arrays(valid_size, image_size)
  train_dataset, train_labels = make_arrays(train_size, image_size)
  vsize_per_class = valid_size // num_classes
  tsize_per_class = train_size // num_classes

  start_v, start_t = 0, 0
  end_v, end_t = vsize_per_class, tsize_per_class
  end_l = vsize_per_class + tsize_per_class

  for label, pickle_file in enumerate(pickle_files):
    try :
      with open(pickle_file, 'rb') as f:
        letter_set = pickle.load(f)
        np.random.shuffle(letter_set)
        if valid_dataset is not None:
          valid_letter = letter_set[:vsize_per_class, :, :]
          valid_dataset[start_v:end_v, :, :] = valid_letter
          valid_labels[start_v:end_v] = label
          start_v += vsize_per_class
          end_v += vsize_per_class
        train_letter = letter_set[vsize_per_class:end_l, :, :]
        train_dataset[start_t:end_t, :, :] = train_letter
        train_labels[start_t:end_t] = label
        start_t += tsize_per_class
        end_t += tsize_per_class
    except Exception , e:
      print("Failed to process file", pickle_file, e)
  return valid_dataset, valid_labels, train_dataset, train_labels
  


# randomize the dataset
def randomize(dataset, labels):
  permutation = np.random.permutation(labels.shape[0])
  shuffled_dataset = dataset[permutation,:,:]
  shuffled_labels = labels[permutation]
  return shuffled_dataset, shuffled_labels



train_size = 200000
valid_size = 10000
test_size = 10000

train_datasets = ['/home/sree/code/train/notMNIST_large/A.pickle', '/home/sree/code/train/notMNIST_large/B.pickle', '/home/sree/code/train/notMNIST_large/C.pickle', '/home/sree/code/train/notMNIST_large/D.pickle']

test_datasets = ['/home/sree/code/train/notMNIST_small/A.pickle', '/home/sree/code/train/notMNIST_small/B.pickle', '/home/sree/code/train/notMNIST_small/C.pickle', '/home/sree/code/train/notMNIST_small/D.pickle']


valid_dataset, valid_labels, train_dataset, train_labels = merge_datasets(train_datasets, train_size, valid_size)
_, _, test_dataset, test_labels = merge_datasets(test_datasets, test_size)


print("datasets merged...")
print(len(valid_dataset))

print("randomizing...")
train_dataset, train_labels = randomize(train_dataset, train_labels)
test_dataset, test_labels = randomize(test_dataset, test_labels)
valid_dataset, valid_labels = randomize(valid_dataset, valid_labels)