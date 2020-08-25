# collections.Counter() 

from collections import Counter
number_shoes = int(input())
shoe_sizes = dict(Counter(list(map(int,input().split()))))
num_cust = int(input())
money_made = 0
while num_cust>0:
    num_cust -=1
    size, cost = list(map(int,input().split()))
    if size not in shoe_sizes.keys() or shoe_sizes[size] == 0:
        continue
    money_made += cost
    shoe_sizes[size] -= 1
print(money_made)

# DefaultDict Tutorial

from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(lambda: -1)

for i in range(1, n+1): 
    word = input()
    d[word] = d[word] + ' ' + str(i) if word in d else str(i)

for _ in range(m):
    print(d[input()])

# Collections.namedtuple()

n = int(input())
i = 0
total = 0
lis = input().split()
for index, head in enumerate(lis):
    if head == 'MARKS':
        col = index
while i < n:
    row = input().split()
    total += int(row[col])
    i += 1 
print(f'{total/n:.2f}')

# Collections.OrderedDict()

from collections import OrderedDict
n = int(input())
i = 0
dic = OrderedDict()
while i < n:
    lis = input().split()
    name = ' '.join(lis[:-1])
    price = int(lis[-1])
    if name not in dic.keys():
        dic[name] = price
    else:
        dic[name] += price
    i +=1
for name, quant in dic.items():
    print(name, quant)

# Word Order

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())

# Collections.deque()

from collections import deque
n = int(input())
m = 0
d = deque()
while m < n:
    string = input()
    try:
        op, val = string.split()
        if op == 'append':
            d.append(int(val))
        elif op == 'appendleft':
            d.appendleft(int(val))
        m += 1
        continue
    except:
        pass
    if string == 'pop':
        d.pop()
    elif string == 'popleft':
        d.popleft()
    m += 1
print(' '.join(list(map(str,d))))

# company logo 

from collections import Counter

for l, n in (Counter(sorted(input())).most_common(3)):
    print(l,n)

# piling up

for _ in range(int(input())):
    input()
    lst = [int(i) for i in input().split()]
    min_list = lst.index(min(lst))
    left = lst[:min_list]
    right = lst[min_list+1:]
    if (left == sorted(left,reverse=True)) and right == sorted(right):
        print('Yes')
    else:
        print('No')
