def findSum(lst, value):
    n = len(lst)
    if not n:
        return []
    for i in range(n - 1):
        for j in range(i + 1, n):
            if value - lst[i] == lst[j]:
                return [i, j]
    return []


print(findSum([1, 21, 3, 14, 5, 60, 7, 6], 81))
