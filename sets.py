# introduction

def average(array):
    return sum(set(array))/len(set(array))
	
# no idea 

n, m = list(map(int,input().split()))
sc_ar = input().split()
A= set(input().split())
B = set(input().split())
happiness = 0
for i in sc_ar:
    happiness += (i in A)-(i in B)
print(happiness)

# symmetric difference

a = input()
seta = set(map(int, input().split()))
c = input()
setb = set(map(int, input().split()))
setc = seta.difference(setb)
setd=(setb.difference(seta))
setc.update(setd)
for i in sorted(setc):
    print(i)
	
# set .add() method 

country = set()
for _ in range(int(input())):
    country.add(input())
print(len(country))

# set .discard(), .remove() & .pop()

input()
uniq = set(map(int,input().split()))
for _ in range(int(input())):
    raw = input()
    if raw == 'pop':
        uniq.pop()
    else:
        op, val = raw.split()
        if op == 'remove':
            uniq.remove(int(val))
        else:
            uniq.discard(int(val))
print(sum(uniq))

# set .union() operation 

input()
A= set(map(int, input().split()))
input()
B= set(map(int, input().split()))
print(len(A.union(B)))

# set .intersection() operation 


input()
A= set(map(int, input().split()))
input()
B= set(map(int, input().split()))
print(len(A.intersection(B)))

# set .difference() operation

num1, st1, num2, st2 = (set(input().split()) for i in range(4))
print(len(st1.difference(st2)))

# set .symmetric_difference() operation

num1, st1, num2, st2 = (set(input().split()) for i in range(4))
print(len(st2.symmetric_difference(st1)))

# set mutations 

input()
numset = set(list(map(int, input().split())))
for _ in range(int(input())):
    op, num = input().split()
    nums = list(map(int, input().split()))
    getattr(numset,op)(nums)
    
print(sum(numset))

# the captain's room

from collections import Counter
family_size = int(input())
rooms = list(map(int, input().split()))
counts = Counter(rooms)
families = (len(rooms)-1)/family_size
uniq = set(rooms)
for i in rooms:
    if counts[i] == 1:
        print(i)

# check subset

for _ in range(int(input())):
    input()
    A = set(map(int,input().split()))
    input()
    B = set(map(int,input().split()))
    print(A.issubset(B))
	
# check strict superset

A = set(map(int,input().split()))
loops = int(input())
count = 0
for _ in range(loops):
    B = set(map(int,input().split()))
    if A.issuperset(B):
        count += 1
if count == loops:
    print(True)
else:
    print(False)
