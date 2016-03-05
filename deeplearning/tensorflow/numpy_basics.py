import numpy as np


__author__ = 'Sreejith S'


# shuffling a 2d array
# important - read arrays with float values as float and int values as int

a = np.array([[1,2,3],[4,5,6],[7,8,9],[3,5,7],[5,8,2]])
print("a initialized with type", type(a))

# creating an ndarray from the array
#first argument is a tupe with the array dimentions
b = np.ndarray((len(a), 3), dtype=int, buffer = a)


#shuffling the elements in the array
print("Shuffling elements in array b")
np.random.shuffle(b)
print(b)


# taking a subset of the arrayp
print("from bth 1st row to third row")
print(b[1:4,:])
print("from bth 1st column to third column of every row")
print(b[:,1:3])

