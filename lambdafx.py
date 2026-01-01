def double(x):
 return x * 2
print("Result of def fx:", double(5))
d = lambda x:x * 2
print("Result of lambda fx:",d(10))
cube = lambda a : a*a*a
avg = lambda m, y : (m+y)/2
print("result of lambda fx cube:", cube(20))
print("result of lambda fx avg:",avg(3,5))


# passing fx to fx
def cube(v):
    return v**3
def fun(fx, value):
    return 5, fx(value)
print("result of passing fx to fx:", fun(cube,5))


# lambda fx to calcute the product of two numbers

l = lambda x,y: x*y
print("result of lambda fx to calcute the product of two numbers:", l(3,5))
# lamba with printing st
nul = lambda x, y : print(f'Result of lambda fx ans with printing st.: {x} *  {y} = {x * y}')
nul(9,7)

# direct call

(lambda m,n : print(f'Result of lambda fx direct call in single line: {m} * {n} = {m * n}'))(3,5)