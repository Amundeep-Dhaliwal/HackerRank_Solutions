# map and the lambda function

cube = lambda x: x**3
def fibonacci(n):
    a= 0 
    b = 1
    lis = [] 
    for _ in range(n):
        lis.append(a)
        c = a + b 
        a = b
        b = c
    return lis

# validating email addresses with a filter

import re
def fun(s):
    return re.match(r"[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", s)

# reduce function

def product(fracs):
    t = reduce(lambda x, y: x*y, fracs)# complete this line with a reduce statement
    return (t.numerator, t.denominator)

