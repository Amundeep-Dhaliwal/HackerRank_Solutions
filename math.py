# polar coordinates
	
import cmath

def mod_phaser(a):
    print(abs(a))
    print(cmath.phase(a))

c = complex(input())
mod_phaser(c)

# find angle MBC

import math
AB = int(input())
BC = int(input())
print(str(int(round(math.degrees(math.atan2(AB,BC)))))+u"\N{DEGREE SIGN}")

# triangle quest 2 

for i in range(int(input())):
    print([1,121,12321,1234321,123454321,12345654321,1234567654321,123456787654321,12345678987654321,12345678987654321][i])

# the code below prints the right angle triangle of numbers upside down

countDownFrom = int(input())
while countDownFrom > 1:
    for start, stop, step in ((1,countDownFrom,1), (countDownFrom,0,-1)):
        for number in range(start, stop, step):
            print(number, end = '')
    print('')
    countDownFrom -= 1
    if countDownFrom == 1:
        print(1)

# mod divmod 

n = int(input())
m = int(input())
print(n//m)
print(n%m)
print(divmod(n,m))

# power - mod power

n =int(input())
m =int(input())
k =int(input())
print(pow(n,m))
print(pow(n,m,k))

# integers come in all sizes 

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(pow(a,b) + pow(c,d))

# triangle quest 

for i in range(1,int(input())): 
    print([1,22,333,4444,55555,666666,7777777,88888888,999999999][i-1])
