# itertools .product() method

from itertools import product
first= list(map(int,input().split()))
second =list(map(int, input().split()))
for tup in list(product(first,second)):
    print(tup,end = ' ', sep=' ')

# itertools .permutations()

from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')

# itertools .combinations()

from itertools import combinations
s,n = input().split()
for i in range(1,int(n)+1):
    for j in combinations(sorted(s),i):
        print(''.join(j))

# itertools .combinations_with_replacement()

from itertools import combinations_with_replacement
s,n = input().split()
for i in (combinations_with_replacement(sorted(s),int(n))):
    print(''.join(i))

# compress the string!

from itertools import groupby
s = input()
for a,b in groupby(s):
    tup=(len(list(b)),int(a))
    print(tup, end = ' ')

# iterables and iterators

from itertools import combinations
input()
combos = list(combinations(input().split(), int(input())))
count = 0
for i in combos:
    if 'a' not in i:
        count += 1 
print(round((len(combos)- count)/len(combos),4))

# maximize it!

from itertools import product
looper, value = list(map(int, input().split()))
nums = []
for _ in range(looper):
    row = map(int, input().split()[1:])
    nums.append(map(lambda x: x**2%value, row))
    #print(list(map(lambda x: x**2%value, row)))
print(max(map(lambda x: sum(x)%value, product(*nums))))
