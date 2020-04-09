## 내장 함수
## docs.python.org/ko/3/libary

lst = [1, 2, 3, 4, 5]

x = abs(-1) # return 1
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