# classes: dealing with complex numbers

from math import pow
class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, no):
        a = self.real + no.real
        b = self.imag + no.imag
        if a<0 and b< 0:
            return f'-{abs(a):.2f}-{abs(b):.2f}i'
        elif a>= 0 and b < 0:
            return f'{abs(a):.2f}-{abs(b):.2f}i'
        elif a < 0 and b >= 0:
            return f'-{abs(a):.2f}+{abs(b):.2f}i'
        elif a>= 0 and b >= 0:
            return f'{abs(a):.2f}+{abs(b):.2f}i'
    
    def __sub__(self,no):
        a = self.real - no.real
        b = self.imag - no.imag
        if a<0 and b< 0:
            return f'-{abs(a):.2f}-{abs(b):.2f}i'
        elif a>= 0 and b < 0:
            return f'{abs(a):.2f}-{abs(b):.2f}i'
        elif a < 0 and b >= 0:
            return f'-{abs(a):.2f}+{abs(b):.2f}i'
        elif a>= 0 and b >= 0:
            return f'{abs(a):.2f}+{abs(b):.2f}i'

    def __mul__(self, no):
        a = self.real * no.real - self.imag * no.imag
        b = self.real * no.imag + self.imag * no.real
        if a<0 and b< 0:
            return f'-{abs(a):.2f}-{abs(b):.2f}i'
        elif a>= 0 and b < 0:
            return f'{abs(a):.2f}-{abs(b):.2f}i'
        elif a < 0 and b >= 0:
            return f'-{abs(a):.2f}+{abs(b):.2f}i'
        elif a>= 0 and b >= 0:
            return f'{abs(a):.2f}+{abs(b):.2f}i'
        
    def __truediv__(self, no):
        x = no.real**2 + no.imag**2
        a = (self.real*no.real +self.imag*no.imag)/x
        b = (-no.imag*self.real + self.imag * no.real)/x
        if a<0 and b< 0:
            return f'-{abs(a):.2f}-{abs(b):.2f}i'
        elif a>= 0 and b < 0:
            return f'{abs(a):.2f}-{abs(b):.2f}i'
        elif a < 0 and b >= 0:
            return f'-{abs(a):.2f}+{abs(b):.2f}i'
        elif a>= 0 and b >= 0:
            return f'{abs(a):.2f}+{abs(b):.2f}i'
    
    def mod(self):
        a = pow(self.real**2 + self.imag**2, 0.5)
        return f'{abs(a):.2f}+0.00i'

# class 2_ find the torsional angle

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points((self.x - no.x), (self.y - no.y) , (self.z - no.z))

    def dot(self, no):
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

    def cross(self, no):
        return Points((self.y*no.z)-(no.y*self.z), (self.z *no.x)-(no.z * self.x), (self.x * no.y)- (no.x * self.y))
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

