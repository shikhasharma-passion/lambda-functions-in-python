# map

def cube(x):
    return x**3

def square(m):
    return m**2

# print(cube(4))
numbers= [1,3,4,5,6,0]
mapp = list(map(cube , numbers ))
print(mapp)

num = (3,4,5,6,7,89,9)
tup = tuple(map(cube ,num))
print(tup)

output = list (map(square,numbers))
print(output)

# bina cube fx baye bhi kr skte hai 

neww = list(map(lambda x: x*x*x, num))
print(neww)

# filter 

def filterring(g):
    return g>4
# print(num)

def even(n):
    return n%2==0
# print(numbers)

filterr = list(filter(even,numbers))
print(filterr)
filterUse = list(filter(filterring , num))
print(filterUse)


