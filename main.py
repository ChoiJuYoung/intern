from datetime import datetime

lst = [1, 2, 3, 4, 5]

start = datetime.now()

for _ in range(100000):
    su = 0

    for x in lst:
        su += x

end = datetime.now()
print("SUM: " + str(su))
print(str(end - start))

start = datetime.now()

for _ in range(100000):
    su = sum(lst)
    
end = datetime.now()

print("SUM: " + str(su))
print(str(end - start))