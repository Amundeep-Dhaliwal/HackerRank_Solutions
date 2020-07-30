# this is a eloquent solution to print a right angle triangle of numbers

for i in range(int(input())):
    print([1,121,12321,1234321,123454321,12345654321,1234567654321,123456787654321,12345678987654321,12345678987654321][i])

# the code below prints the triangle of numbers upside down and is not constrained

countDownFrom = int(input())
while countDownFrom > 1:
    for start, stop, step in ((1,countDownFrom,1), (countDownFrom,0,-1)):
        for number in range(start, stop, step):
            print(number, end = '')
    print('')
    countDownFrom -= 1
    if countDownFrom == 1:
        print(1)
