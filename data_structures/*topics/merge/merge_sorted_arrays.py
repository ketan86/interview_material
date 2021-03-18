def merge_arrays(lst1, lst2):
    m = len(lst1)
    n = len(lst2)
    if not m:
        return lst2
    if not n:
        return lst1
    sorted_list = list()
    i = 0
    j = 0
    while i <= m - 1 and j <= n - 1:
        if lst1[i] < lst2[j]:
            sorted_list.append(lst1[i])
            i += 1
        else:
            sorted_list.append(lst2[j])
            j += 1

    if i <= m - 1:
        sorted_list.extend(lst1[i:])
    if j <= n - 1:
        sorted_list.extend(lst2[j:])

    return sorted_list


print(merge_arrays([1, 3], [2, 4]))
