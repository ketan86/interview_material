# pylint: skip-file
# Big(O) - n^2


def insertion_sort(arr):
    for i in range(len(arr)):
        j = i - 1
        while j >= 0:
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1
    return arr


print(insertion_sort([-5, 4, 2, 3, -4]))
