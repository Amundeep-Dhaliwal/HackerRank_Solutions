# the aim of this challenge was to print the addition, subtraction, multuplication, division and the modulus of two complex numbers
# all results are printed to two decimal places

import math

from math import pow

class Complex(complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, no):
        return complex(self.real+no.real, self.imag + no.imag)
    def __sub__(self, no):
        return complex(self.real-no.real, self.imag - no.imag)
    def __mul__(self, no):
        return complex(self.real*no.real-self.imag*no.imag, self.real*no.imag+self.imag*no.real)
    
    def __truediv__(self, no):
        try:
            return self.__mul__(complex(no.real, -1*no.imag)).__mul__(complex(1.0/(no.mod().real)**2,0))
        except ZeroDivisionError as e:
            print(e)
            return None
    def mod(self):
        return complex(pow(self.real**2+self.imag**2, 0.5),0)
    def __str__(self, precision =2):
        return str(("%."+"%df"%precision)%float(self.real)+('+' if self.imag >= 0 else '-')+str(("%."+"%df"%precision)%float(abs(self.imag)))+'i')
    

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
