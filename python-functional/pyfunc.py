
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


