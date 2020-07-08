# This function can be used to check whether a roman numeral between 1 and 4000 is valid

import re
def roman_numeral_check(n):
    thousand = 'M{0,3}'
    hundred = '(C[MD]|D?C{0,3})'
    ten = '(X[CL]|L?X{0,3})'
    digit= '(I[VX]|V?I{0,3})'
    print(bool(re.match(thousand+hundred+ten+digit+'$', n)))
