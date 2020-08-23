# Hello world solution

print("Hello, World!")

# python if-else

n = int(input().strip())

if (n%2) == 1:
	print('Weird')
elif (n%2) == 0 and 2<=n<=5:
	print('Not Weird')
elif (n%2) == 0 and 6 <= n <= 20:
	print('Weird')
elif (n%2) == 0 and 20 < n <=100:
	print('Not Weird')

# arithmetic operators

a = int(input())
b = int(input())

print(a+b)
print(a-b)
print(a*b)

# python division

a = int(input())
b = int(input())

print(a//b)
print(a/b)


# loops 

n = int(input())

for i in range(n):
	print(i**2)
	

# write a function 

def is_leap(year):
	if year%4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
	
# print funtion

n = int(input())

for i in range(1, n+1):
	j = ''.join(i)
