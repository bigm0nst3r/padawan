
# functional programming methods

input = range(1,11)

# 1. map
def cube(x):
  return x*x*x

print map(cube, input)

# using a lambda function instead of passing function argument
print map(lambda x : x*x, input)


# 2. filter
print filter(lambda x: x> 5, input)

# 3.reduce
# intersection is a reduce operation
input1 = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
print reduce(set.intersection, map(set, input1))







