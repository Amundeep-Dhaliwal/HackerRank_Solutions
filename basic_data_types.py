# list comprehensions

x,y,z,n = (int(input()) for _ in range(4))

print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z + 1) if a + b + c < n])

# find the runner up score

z = max(arr)
while max(arr) == z:
	arr.remove(max(arr))
    
print(max(arr))

# nested lists

marksheet = []
for _ in range(0, int(input())):
	marksheet.append([input(), float(input())])
        
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

# finding the percentage

n = int(input())
student_marks = {}
for _ in range(n):
	name, *line = input().split()
	scores = list(map(float, line))
	student_marks[name] = scores
query_name = input()
    
query_scores = student_marks[query_name]
print(f'{(sum(query_scores) /len(query_scores)):.2f}')

# lists

l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)

# tuples 

print(hash(tuple(integer_list)))
