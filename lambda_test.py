from functools import reduce
from datetime import datetime

def add(a, b):
    return a + b

print(add(2, 3))

lambdaAdd = lambda a, b: a + b

print(lambdaAdd(2, 3))


l = list(range(1, 11))
print(l)

m = list(map(lambda n: n * n, l))
print(m)

f = list(filter(lambda n: n % 2 == 0, l))
print(f)

r = reduce(lambda n, m: n * m, l)
print(r)



lst = [b'a', b'b', b'c']

start = datetime.now()
for _ in range(100000):
    lst1 = list(map(lambda e: e.decode('utf-8'), lst))
end = datetime.now()
print(str(end - start))
print(lst1)

start = datetime.now()
for _ in range(100000):
    lst2 = [lbl.decode('utf-8') for lbl in lst]
end = datetime.now()
print(str(end - start))
print(lst2)