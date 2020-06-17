lst = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(len(lst)):
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j + 1]:
            tmp = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = tmp

print(lst)
