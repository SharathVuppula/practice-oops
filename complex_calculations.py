import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real  =  real
        self.imaginary =  imaginary
    def __add__(self, no):
        r = self.real + no.real
        im  =  self.imaginary + no.imaginary
        return '{} {}' .format(r,im)
    def __sub__(self, no):
        r = self.real - no.real
        im  =  self.imaginary - no.imaginary
        return (r,im)
    def __mul__(self, no):
        r = (self.real * no.real) - (self.imaginary * no.imaginary)
        im  =  (self.real * no.imaginary) + (self.imaginary * no.real)
        return (r,im)
    def __truediv__(self, no):
        r = self.real / no.real
        im  =  self.imaginary / no.imaginary
        return (r,im)

    def mod(self):
        r = (self.real * self.real) + (self.imaginary * self.imaginary)
        r = math.sqrt(r)
        return r
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
    