import sys
li=[]
di="hi"
print dir(li)
print dir(di)
print dir(sys)
print li.__doc__
print di.__doc__
print sys.__doc__

def f(): pass

class cl():
    def fun():
        pass

ob=cl()

print type(cl)
print type(ob)
print type(ob.fun)
print type(f)
print type(sys)

print id(1)
print id("hi")
print id(di)
print id(cl)
print id([])
print id(sys)
print id(ob.fun)
print id(f)

print dict.__name__
print callable(f)
print callable(cl)
print callable(ob)
print isinstance(ob, cl)
print isinstance(ob, object)
print isinstance(2, int)