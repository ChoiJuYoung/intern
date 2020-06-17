def quick(lst, _left, _right):
    if _left >= _right:
        return
    
    pivot = _left

    left = _left + 1
    right = _right

    while True:
        while right > left and lst[right] > lst[pivot]:
            right -= 1
        while left < right and lst[left] < lst[pivot]:
            left += 1

        if left == right:
            if lst[left] < lst[pivot]:
                tmp = lst[pivot]
                lst[pivot] = lst[left]
                lst[left] = tmp
            break
        else:
            tmp = lst[left]
            lst[left] = lst[right]
            lst[right] = tmp

    quick(lst, _left, left-1)
    quick(lst, left, _right)


lst = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

quick(lst, 0, len(lst) - 1)

print(lst)