
import matplotlib.pyplot as plt

import numpy as np


def softmax(scores):
  """
  """
  nr = np.exp(scores)
  dr = np.sum(nr, axis=0)
  return nr/(dr)


# increasing the size of outputs
# confidence of the classifier increases
# difference in probabilities
scores  = np.array([3.0,1.0,2.0]) / 10
print softmax(scores)

scores  = np.array([3.0,1.0,2.0]) * 10
print softmax(scores)


# scores
# plotting curves
#x = np.arange(-2.0, 6.0, 0.1)
# x = scores
# scores = np.vstack([x , np.ones_like(x), 2 * np.ones_like(x)])

# plt.plot(x , softmax(scores).T, linewidth=2)
# plt.show()

