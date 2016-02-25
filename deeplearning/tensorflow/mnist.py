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
  for image in image_files:
    image_file = os.path.join(folder, image)
    try :
      print("Traning Image file", image_file)
      image_data = (ndimage.imread(image_file).astype(float) - pixel_depth/2) / pixel_depth
      if image_data.shape != (image_size, image_size):
        raise Exception('Unexpected image shape: %s' % str(image_data.shape))
      dataset[image_index, :, :] = image_data
      image_index += 1
    except IOError as e:
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

train_folders = [ '/home/sree/code/train/notMNIST_largeA', '/home/sree/code/train/notMNIST_largeB', '/home/sree/code/train/notMNIST_largeC', '/home/sree/code/train/notMNIST_largeD']

train_datasets = maybe_pickle(train_folders, 45000)
#test_datasets = maybe_pickle(test_folders, 1800)
pdb.set_trace()
