

import numpy as np




__author__ = "Sreejith Sreekumar <sreejith.sreekumar@247-inc.com>"

scores = [3.0, 1.0, 0.2]


def softmax(x):
    """
    increase in score value => increase in probability


    ? what are these values in x

    what is the score value that the vector is of class 0, or class 1, or class2
    
    
    
    Arguments:
    - `x`:
    """
    return np.exp(x)/np.sum(np.exp(x))
    


print(softmax(scores))    
print(sum(softmax(scores)))


