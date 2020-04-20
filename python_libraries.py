## 내장 함수
## docs.python.org/ko/3/libary

lst = [1, 2, 3, 4, 5]

x = abs(-1) # return 1
class test():
    def __abs__(self):
        print("hello")

te = test()
print(abs(te))


x = all(lst) # return True if all elements of iterable is True
'''
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
'''
x = any(lst) # return True if any element of iterable is True
'''
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
'''
x = ascii("안녕하세요")
print(x)

class temp:
    x = 5
    @classmethod
    def do(arg1, arg2, arg3):
        print(arg1)
        print(arg2)
        print(arg3)

temp.do(1, 2)

print(temp.__dict__)



class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """ Get the current voltage."""
        return self._voltage

    @voltage.setter
    def voltage(self, value):
        self._voltage = value

    @voltage.deleter
    def voltage(self):
        del self._voltage

p = Parrot()
print(p.voltage)
p.voltage = 5000000
print(p.voltage)
del p.voltage
try:
    print(p.voltage)
except:
    print("NO VOLTAGE")
#p.voltag = 100000
#print(p.voltage)

def zip2(*iterables):
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
            result = []
            for it in iterators:
                    elem = next(it, sentinel)
                    if elem is sentinel:
                            return
                    result.append(elem)
            yield tuple(result)

lst1 = [1, 2, 3, 4, 5]
lst2 = ['a', 'b', 'c']

print(zip2(lst1, lst2))

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped))
x2, y2 = zip(*zip(x, y))
x ==
