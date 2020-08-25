# exceptions

n = int(input())
i = 0
while i < n:
    try:
        a, b = list(map(int, input().split()))
    except ValueError as e:
        i +=1
        print('Error Code:',e)
        continue
    try:
        c = a//b
    except ZeroDivisionError as e:
        i +=1
        print('Error Code:',e)
        continue
    else:
        i +=1
        print(c)

# incorrect regex

import re
for i in range(int(input())):
    try:
        re.compile(input())
    except:
        print(False)
    else:
        print(True)
