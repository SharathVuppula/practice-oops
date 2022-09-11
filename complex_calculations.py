import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real  =  real
        self.imaginary =  imaginary
    def __add__(self, no):
        r = Complex(0,0)
        r.real = self.real + no.real
        r.imaginary  =  self.imaginary + no.imaginary
        return r
    def __sub__(self, no):
        r = Complex(0,0)
        r.real = self.real - no.real
        r.imaginary  =  self.imaginary - no.imaginary
        return r
    def __mul__(self, no):
        r = Complex(0,0)
        r.real = (self.real * no.real) - (self.imaginary * no.imaginary)
        r.imaginary  =  (self.real * no.imaginary) + (self.imaginary * no.real)
        return r
    def __truediv__(self, no):# a+bi / c +di = (ac + bd)/(c2 +d2) + (bc -ad)/(c2 + d2) i  
        r = Complex(0,0)
        r.real = (self.real * no.real + self.imaginary * no.imaginary)/ (math.pow(no.real,2) + math.pow(no.imaginary,2))
        r.imaginary  =  (self.imaginary * no.real - self.real * no.imaginary)/ (math.pow(no.real,2) + math.pow(no.imaginary,2))
        return r

    def mod(self):
        r = Complex(0,0)
        temp = (self.real * self.real) + (self.imaginary * self.imaginary)
        temp = math.sqrt(temp)
        r.real = temp
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
    