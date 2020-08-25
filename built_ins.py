# zipped!

students, subjects = list(map(int, input().split()))
marks = []
for _ in range(subjects):
    *v, = map(float, input().split())
    marks.append(v)
for i in range(students):
    total = []
    for j in range(subjects):
        total.append(marks[j][i])
    print(sum(total)/len(total))

# Input()

x,y = map(int, input().split())
print(eval(input()) == y)

# python evaluation

eval(input())

# athelete sort

athletes, attr = map(int, input().split())
stats = [list(map(int, input().split())) for _ in range(athletes)]

#stats = [[10,2,5],[7,1,0],[9,9,9], [1,23,12], [6,5,9]]
index =  int(input())

for i in sorted(stats, key = lambda ath: ath[index]):
    print(' '.join(map(str, i)))

# any or all

input()
lis = list(map(int, input().split()))
if all(i>0 for i in lis) and any(str(i) == str(i)[::-1] for i in lis):
    print(True)
else:
    print(False)

# ginortS

inp = input()
upper = []
lower = []
odd = []
even = []
for i in inp:
    if i.isupper():
        upper.append(i) 
    elif i.islower():
        lower.append(i)
    elif int(i) % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
lower.sort()
upper.sort()
even.sort()
odd.sort()
print(''.join(lower+upper+odd+even))
