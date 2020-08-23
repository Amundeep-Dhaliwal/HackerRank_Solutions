# sWAP cASE

def swap_case(s):
    z = ''
    for c in s:
        if c.isupper()==True:
            z+= c.lower()
        else:
            z+=c.upper()
    return z
	
# string split and join

def split_and_join(line):
    # write your code here
    x = line.split()
    y = '-'.join(x)
    return y

# what your name?

def print_full_name(a, b):
    print("Hello "+a+' '+b+'! You just delved into python.')

# mutations 

def mutate_string(string, position, character):
    return string[:position]+character+ string[position+1:]

# find a string

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if string[i:i+len(sub_string)] == sub_string:
                count += 1
                continue
    return count

# string validators

print(any(map(str.isalnum, s)))
print(any(map(str.isalpha, s)))
print(any(map(str.isdigit, s)))
print(any(map(str.islower, s)))
print(any(map(str.isupper, s)))

# text alignment 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

 #Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

# #Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# #Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# text wrap 
import textwrap
def wrap(string, max_width):
    return (textwrap.fill(string,max_width))

# designer door mat

length, width = map(int, input().split())
pattern = [('.|.'*(2*i+1)).center(width, '-') for i in range(length//2)]
print('\n'.join(pattern+['WELCOME'.center(width,'-')]+pattern[::-1]))

# string formatting

def print_formatted(number):
    # your code goes here
    width = len('{0:b}'.format(number))
    for i in range(1,number +1):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i,width=width))

# alphabet rangoli

def print_rangoli(n):
    l = []
    for i in range(n):
        s= '-'.join('abcdefghijklmnopqrstuvwxyz'[i:n])
        l.append((s[::-1]+s[1:]).center(4*n-3, '-'))
    print('\n'.join(l[:0:-1]+l))

# capitalize 

def solve(s):
    for iterable in s.split():
        s = s.replace(iterable,iterable.capitalize())
    return s

# the minion game 

def minion_game(s):
    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += len(s) -i
        else:
            stusc += len(s)-i
    if kevsc> stusc:
        print('Kevin', kevsc)
    elif kevsc < stusc:
        print('Stuart', stusc)
    else:
        print('Draw')

# merge the tools

def merge_the_tools(s, n):
    for part in list(zip(*[iter(s)]*n)):
        d = dict()
        print(''.join([d.setdefault(c,c) for c in part if c not in d]))




