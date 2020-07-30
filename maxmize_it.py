# You are given a funtion and a series of lists with a pre-determined number of elements
# the challenge was to find the largest sum of squares

from itertools import product
looper, value = list(map(int, input().split()))
nums = []
for _ in range(looper):
    row = map(int, input().split()[1:])
    nums.append(map(lambda x: x**2%value, row))
    #print(list(map(lambda x: x**2%value, row)))
print(max(map(lambda x: sum(x)%value, product(*nums))))
