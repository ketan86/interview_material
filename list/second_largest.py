def findSecondMaximum(lst):
    n = len(lst)
    if n < 2:
        return
    first = second = float('-inf')
    for i in lst:
        if i > first:
            second = first
            first = i
        elif i > second and i != first:
            second = i
    return second


print(findSecondMaximum([9, 2, 3, 6, 8]))
