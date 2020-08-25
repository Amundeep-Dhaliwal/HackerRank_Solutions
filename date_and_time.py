# calendar module

import calendar

month, date, year = list(map(int, input().split()))

no = (calendar.weekday(year, month, date))
if no == 0:
    print('MONDAY')
elif no == 1:
    print('TUESDAY')
elif no == 2:
    print('WEDNESDAY')
elif no == 3:
    print('THURSDAY')
elif no == 4:
    print('FRIDAY')
elif no == 5:
    print('SATURDAY')
elif no == 6:
    print('SUNDAY')

# time delta

from datetime import datetime
fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs(datetime.strptime(input(), fmt)- datetime.strptime(input(),fmt)).total_seconds()))
