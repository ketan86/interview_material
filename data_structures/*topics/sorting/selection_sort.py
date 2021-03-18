# pylint: skip-file
# Big(O) - n^2


def selection_sort(arr):
    n = len(arr) - 1
    # go over the arr till second last element
    for i in range(n - 1):
        # go over the arr from next element of i till last element to
        # see if i'th element is less. If less, swap
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
        print(arr)
    return arr


print(selection_sort([4, 3, 5, 2, 1, 6]))
