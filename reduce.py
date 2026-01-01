# for using reduce fx we need to import it.

# This program uses reduce() to repeatedly apply the mysum function and add all the numbers in the list to get a single total sum.
from functools import reduce
numbers = [2,4,6,8,9,1]
def mysum(x,y):
    return x+y

sum = reduce(mysum, numbers)
print(sum)
