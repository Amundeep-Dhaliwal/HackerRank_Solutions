# Standardize mobile numbers using decorators

import re
def wrapper(f):
    def inner(l):
        # complete the function
        valid = []
        for s in l:
            if len(s) == 10:
                s = '+91 '+s[:5]+' '+s[5:]
                valid.append(s)
            elif s[:3] == '+91':
                s = '+91 '+s[3:8]+' '+s[8:]
                valid.append(s)
            elif s[:2] == '91':
                s = '+91 '+s[2:7]+' '+s[7:]
                valid.append(s)
            elif s[0] == '0':
                s = '+91 '+s[1:6]+' '+s[6:]
                valid.append(s)
        return f(valid)

    return inner

# Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        speople = sorted(people, key = lambda x: int(x[2]))
        names = []
        for person in speople:
            names.append(f(person))
        return names
    return inner

