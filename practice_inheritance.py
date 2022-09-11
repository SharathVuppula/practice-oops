class A:
    def meth1(self):
        print('This is from method 1')
class B:
    def meth2(self):
        print('This is from method 2')
class c(A,B):
    def meth3(self):
        print('This is from method 3')
    def meth4(self):
        print('This is from  method 4')

obj1 = c()
obj1.meth3()
obj2 = B()
obj2.meth2()

# s = 'String'
# for c in s:
    
# print(s)
c = 'A'
res = c.isupper()
print  (c.lower())
