y = 2


foo = {'1':1,'2':2,'3':3,'4':4,'5':5},{'1':2,'2':3,'3':4,'4':5,'5':6}

list1= {"first":"test", "second": "best", "third": "worst", "fourth": "name","fifth":"game"}
list2 = {"first": "checking", "second": "best", "third" : "foo", "fourth": "word", "fifth": "less"}
list3 = {"first": "award", "second": "best", "third": "pertain", "fourth": "lane", "fifth": "grain"}

foo2 = []
foo2.append(list1)
foo2.append(list2)
foo2.append(list3)

'''
g = lambda x: x*2, foo

print g
'''

sum = lambda x, y:   x + y  #  def sum(x,y): return x + y

test = lambda x, y, z: "x: " + str(x) + " y: " + str(y) + " z: " + str(z)
print test(6,7,8)

def getvaluenolambda(key):
    return key["first"]


keylamb = lambda k: k["second"]
print keylamb(list1)

#foo2 = sorted(foo2, key = getvaluenolambda(foo2))

#foo2 = sorted(foo2, key = lambda k: k["first"])

foo2 = sorted(foo2, key = getvaluenolambda)

for x in range (0, len(foo2)):
     print foo2[x]


foofunction = lambda y:y+1

print foofunction(2)


p = property(fset=lambda self: self._p, doc="The node's parent")